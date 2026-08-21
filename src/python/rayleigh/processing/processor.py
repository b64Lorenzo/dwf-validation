"""
Rayleigh Signal Processing
==========================

Module
------
rayleigh.processing.processor

Description
-----------
Functions responsible for:

* Metadata extraction
* Wave extraction
* Signal processing
* Rayleigh data preparation

This module contains analysis-specific logic and
should not be moved to the shared utils package.

Author
------
Lorenzo Zambelli

Version
-------
2.0.0
"""

from __future__ import annotations

import re

import numpy as np

from numba import njit

from utils.io import read_db

from rayleigh.config import (
    FOLDER_RE,
)


# ============================================================
# METADATA EXTRACTION
# ============================================================

def extract_depth(name: str):
    """
    Extract probe depth from a signal name.

    Parameters
    ----------
    name : str

        Example:

            WaveElev_22.5m

    Returns
    -------
    float | None

    Examples
    --------
    >>> extract_depth("WaveElev_22.5m")
    22.5
    """

    match = re.search(
        r"([0-9.]+)m",
        name,
    )

    return (
        float(match.group(1))
        if match
        else None
    )


def extract_position(name: str):
    """
    Extract hydrodynamic position identifier.

    Parameters
    ----------
    name : str

    Returns
    -------
    str | None

    Examples
    --------
    HC
    +1xHC
    -1xHC
    +2xHC
    -2xHC
    """

    if "-2xhalfHydCenter" in name:
        return "-2xHC"

    if "-halfHydCenter" in name:
        return "-1xHC"

    if "2xhalfHydCenter" in name:
        return "+2xHC"

    if "halfHydCenter" in name:
        return "+1xHC"

    if "HydCenter" in name:
        return "HC"

    return None


# ============================================================
# WAVE EXTRACTION
# ============================================================

@njit
def extract_wave(signal):
    """
    Extract individual wave heights.

    A wave height is computed as:

        crest - trough

    using local peak and trough detection.

    Parameters
    ----------
    signal : ndarray

    Returns
    -------
    ndarray

        Extracted wave heights.
    """

    n = len(signal)

    mean_value = np.mean(signal)

    signal -= mean_value

    peaks = []
    troughs = []

    for i in range(1, n - 1):

        if signal[i - 1] < signal[i] >= signal[i + 1]:

            peaks.append(i)

        elif signal[i - 1] > signal[i] <= signal[i + 1]:

            troughs.append(i)

    if len(peaks) < 2:
        return np.empty(0)

    if len(troughs) < 2:
        return np.empty(0)

    heights = np.empty(
        len(peaks)
    )

    count = 0
    trough_index = 0

    for peak in peaks:

        while (
            trough_index < len(troughs)
            and troughs[trough_index] < peak
        ):
            trough_index += 1

        if trough_index == 0:
            continue

        if trough_index >= len(troughs):
            continue

        tb = troughs[trough_index - 1]
        ta = troughs[trough_index]

        trough_value = min(
            signal[tb],
            signal[ta],
        )

        heights[count] = (
            signal[peak]
            - trough_value
        )

        count += 1

    return heights[:count]


# ============================================================
# PROCESS FILE
# ============================================================

def process_file(csv_path):
    """
    Process a simulation result file.

    Extracts:

    * Metadata
    * Wave heights
    * Signal variance

    Parameters
    ----------
    csv_path : pathlib.Path

    Returns
    -------
    list

        [
            (
                metadata,
                wave_heights,
                m0
            )
        ]
    """

    try:

        folder = csv_path.parent.name

        match = FOLDER_RE.search(
            folder
        )

        if not match:
            return []

        meta = {
            key: float(value)
            for key, value
            in match.groupdict().items()
        }

        meta["angle"] = int(
            meta["angle"]
        )

        meta["pan"] = int(
            meta["pan"]
        )

        db = read_db(
            csv_path
        )

        if db is None:
            return []

        results = []

        for key in db.keys:

            signal_name = key.name

            # ====================================
            # WAVE SIGNALS ONLY
            # ====================================

            if "WaveElev" not in signal_name:
                continue

            try:

                signal_obj = db[key]

            except Exception:

                continue

            if signal_obj is None:
                continue

            if signal_obj.data is None:
                continue

            signal = np.asarray(
                signal_obj.data
            ).reshape(-1)

            if signal.size < 10:
                continue

            # ====================================
            # WAVE EXTRACTION
            # ====================================

            wave = extract_wave(
                signal.copy()
            )

            if wave.size == 0:
                continue

            # ====================================
            # METADATA
            # ====================================

            meta_ext = meta.copy()

            meta_ext["depth"] = (
                extract_depth(
                    signal_name
                )
            )

            meta_ext["pos"] = (
                extract_position(
                    signal_name
                )
            )

            results.append(
                (
                    meta_ext,
                    wave,
                    np.var(signal),
                )
            )

        return results

    except Exception:

        return []