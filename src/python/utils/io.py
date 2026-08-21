"""
Input/Output Utilities
======================

Module
------
utils.io

Description
-----------
Reusable file loading and caching utilities used throughout
hydrodynamic validation and post-processing projects.

This module provides functionality for:

- Loading TimeDB databases.
- Fast CSV reading for Wave Elevation signals.
- Parallel loading of simulation result files.
- Disk-based caching of processed data.
- Reuse of processed results between analysis runs.

The functions in this module should remain completely
independent of any specific analysis type
(Rayleigh, Spectral, Validation, Boxplots, etc.).

Dependencies
------------
- numpy
- pymarin
- pathlib
- concurrent.futures
- tqdm

Author
------
Lorenzo Zambelli

Version
-------
1.0.0

Last Updated
------------
2026-07-27
"""

from concurrent.futures import ProcessPoolExecutor, as_completed

import logging
import numpy as np

from pymarin.io import read_timedb
from tqdm import tqdm


# ============================================================
# MODULE CACHE
# ============================================================

_MEMORY_CACHE = {}


def load_all(
    raw_csv_dirs,
    cache_file,
    process_file,
    logger=None,
    max_workers=4,
):
    """
    Load and cache processed simulation data.

    This function provides a generic loading workflow:

    1. Check in-memory cache.
    2. Check disk cache.
    3. Process raw files if necessary.
    4. Save cache.
    5. Return results.

    Parameters
    ----------
    raw_csv_dirs : list[pathlib.Path]
        Directories containing input CSV files.

    cache_file : pathlib.Path
        Cache file.

    process_file : callable
        Function used to process a single file.

        Expected signature:

        >>> process_file(path)

    logger : logging.Logger, optional
        Logger instance.

    max_workers : int, optional
        Number of worker processes.

    Returns
    -------
    list
        Processed results.

    Examples
    --------
    >>> results = load_all(
    ...     raw_csv_dirs=[folder],
    ...     cache_file=cache_file,
    ...     process_file=process_file,
    ... )
    """

    cache_key = str(cache_file)

    # ========================================================
    # IN-MEMORY CACHE
    # ========================================================

    if cache_key in _MEMORY_CACHE:

        if logger:
            logger.debug(
                "Using memory cache: %s",
                cache_file.name,
            )

        return _MEMORY_CACHE[cache_key]

    # ========================================================
    # DISK CACHE
    # ========================================================

    if cache_file.exists():

        if logger:
            logger.info(
                "Loading cache: %s",
                cache_file.name,
            )

        try:

            results = np.load(
                cache_file,
                allow_pickle=True,
            ).tolist()

            _MEMORY_CACHE[cache_key] = results

            if logger:
                logger.info(
                    "Loaded %d cached records.",
                    len(results),
                )

            return results

        except Exception as exc:

            if logger:
                logger.warning(
                    "Failed loading cache: %s",
                    cache_file.name,
                )

                logger.debug(
                    "Exception: %s",
                    exc,
                )

            cache_file.unlink(
                missing_ok=True,
            )

    # ========================================================
    # DISCOVER FILES
    # ========================================================

    files = []

    for directory in raw_csv_dirs:

        found = list(
            directory.rglob("*.csv")
        )

        files.extend(found)

        if logger:
            logger.debug(
                "%s -> %d files",
                directory,
                len(found),
            )

    if logger:
        logger.info(
            "Found %d CSV files.",
            len(files),
        )

    # ========================================================
    # PROCESS FILES
    # ========================================================

    results = []

    with ProcessPoolExecutor(
        max_workers=max_workers
    ) as executor:

        futures = [

            executor.submit(
                process_file,
                file,
            )

            for file in files
        ]

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Processing files",
        ):

            try:

                result = future.result()

            except Exception as exc:

                if logger:
                    logger.warning(
                        "Worker failed."
                    )

                    logger.debug(
                        "Exception: %s",
                        exc,
                    )

                continue

            if result:

                results.extend(result)

    # ========================================================
    # SAVE CACHE
    # ========================================================

    if logger:
        logger.info(
            "Saving cache: %s",
            cache_file.name,
        )

    np.save(
        cache_file,
        np.array(
            results,
            dtype=object,
        ),
        allow_pickle=True,
    )

    _MEMORY_CACHE[cache_key] = results

    if logger:
        logger.info(
            "Saved %d records.",
            len(results),
        )

    return results


def read_db(csv_path):
    """
    Read a TimeDB database file.

    This function wraps the PyMarin
    ``read_timedb()`` function and provides
    safe error handling.

    Parameters
    ----------
    csv_path : pathlib.Path
        Path to the TimeDB file.

    Returns
    -------
    TimeDB or None
        TimeDB object if reading succeeds.

        None if:
        - file is invalid
        - file cannot be opened
        - no signals are present

    Notes
    -----
    Any exceptions raised by PyMarin are caught
    and converted to None.

    Examples
    --------
    >>> db = read_db(
    ...     Path("results.csv")
    ... )

    >>> if db:
    ...     print(len(db.keys))

    Version
    -------
    1.0.0
    """

    try:

        db = read_timedb(str(csv_path))

        return db if db.keys else None

    except Exception:

        return None


def fast_read(csv_path):
    """
    Fast CSV reader for wave elevation analysis.

    This function is intended as a lightweight
    alternative to loading a full TimeDB.

    Only the following columns are read:

    - Time
    - WaveElev*

    All other columns are ignored.

    Parameters
    ----------
    csv_path : pathlib.Path
        Input CSV file.

    Returns
    -------
    tuple[numpy.ndarray, list[str]]
        Returns:

        (
            data,
            column_names
        )

        where:

        data :
            Numerical data array.

        column_names :
            Names of loaded columns.

    None
        Returned whenever:

        - file is empty
        - file is invalid
        - wave elevation columns are absent
        - loading fails

    Notes
    -----
    A quick file-size check is performed before
    attempting to read the CSV.

    Files smaller than 100 bytes are assumed to
    be empty or invalid.

    Examples
    --------
    >>> result = fast_read(
    ...     Path("waves.csv")
    ... )

    >>> if result is not None:
    ...     data, columns = result

    >>> print(columns)
    ['Time', 'WaveElev_22.5m']

    Version
    -------
    1.0.0
    """

    # --------------------------------------------------------
    # FAST EMPTY FILE CHECK
    # --------------------------------------------------------
    if csv_path.stat().st_size < 100:
        return None

    try:

        with open(csv_path, "r") as file:

            header = (
                file.readline()
                .strip()
                .split(",")
            )

        if len(header) < 2:
            return None

        usecols = [
            i
            for i, column in enumerate(header)
            if (
                column.lower().startswith("time")
                or "WaveElev" in column
            )
        ]

        if len(usecols) <= 1:
            return None

        data = np.loadtxt(
            csv_path,
            delimiter=",",
            skiprows=2,
            usecols=usecols,
        )

        if data.size == 0:
            return None

        column_names = [
            header[i]
            for i in usecols
        ]

        return (
            data,
            column_names,
        )

    except Exception:

        return None