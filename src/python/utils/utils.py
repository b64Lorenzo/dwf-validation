"""
General Utility Functions
=========================

Module
------
utils.utils

Description
-----------
Collection of lightweight utility functions used throughout
analysis and validation projects.

The functions in this module provide:

- Time window formatting
- Numeric formatting
- Sorting helpers
- Order-of-magnitude calculations
- Time step transformations
- Points-per-period calculations
- Group key generation

These utilities are intentionally generic and should remain
independent from any specific analysis workflow.

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

from __future__ import annotations

import numpy as np


def format_time_window(
    time_window: tuple[float | None, float | None]
) -> str:
    """
    Convert a time window into a filename-friendly string.

    Parameters
    ----------
    time_window : tuple(float | None, float | None)
        Time window specified as:

        (
            start_time,
            end_time
        )

        Use None to indicate no bound.

    Returns
    -------
    str
        Formatted string representation.

    Examples
    --------
    >>> format_time_window((None, None))
    'timemin-max'

    >>> format_time_window((100, 500))
    'time100-500'

    >>> format_time_window((None, 600))
    'timemin-600'

    Version
    -------
    1.0.0
    """

    t0, t1 = time_window

    t0_str = "min" if t0 is None else f"{t0:g}"
    t1_str = "max" if t1 is None else f"{t1:g}"

    return f"time{t0_str}-{t1_str}"


def clean(value):
    """
    Round a numerical value to three significant digits.

    Useful when generating labels, filenames and plot
    annotations while avoiding excessive precision.

    Parameters
    ----------
    value : float | int | None
        Input value.

    Returns
    -------
    float | None
        Rounded value.

    Examples
    --------
    >>> clean(0.10000001)
    0.1

    >>> clean(0.0098765)
    0.00988

    >>> clean(None)
    None

    Version
    -------
    1.0.0
    """

    if value is None:
        return None

    return float(f"{value:.3g}")


def fmt(value) -> str:
    """
    Convert a value into a compact display string.

    Used primarily for:

    - Plot legends
    - Axis labels
    - Metadata display
    - Figure annotations

    Parameters
    ----------
    value : Any
        Value to format.

    Returns
    -------
    str
        Formatted string.

    Examples
    --------
    >>> fmt(0.123456)
    '0.12'

    >>> fmt(10.0)
    '10'

    >>> fmt(None)
    'None'

    Version
    -------
    1.0.0
    """

    if value is None:
        return "None"

    if isinstance(value, float):
        return f"{value:.2g}"

    return str(value)


def sort_key(item):
    """
    Generate a sorting key for grouped data.

    Any None value is converted to negative infinity,
    ensuring missing values appear first when sorting.

    Parameters
    ----------
    item : tuple
        Grouped item in the form:

        (
            group_key,
            data
        )

    Returns
    -------
    tuple
        Sorting key suitable for use with sorted().

    Examples
    --------
    >>> sort_key(((1, 2), {}))
    (1, 2)

    >>> sort_key(((None, 2), {}))
    (-inf, 2)

    Version
    -------
    1.0.0
    """

    group = item[0]

    return tuple(
        -np.inf if value is None else value
        for value in group
    )


def order_of_magnitude(value):
    """
    Compute the order of magnitude of a positive value.

    Parameters
    ----------
    value : float | int | None

    Returns
    -------
    float | None

        Returns:

        10^floor(log10(value))

    Examples
    --------
    >>> order_of_magnitude(0.034)
    0.01

    >>> order_of_magnitude(123)
    100

    >>> order_of_magnitude(None)
    None

    Version
    -------
    1.0.0
    """

    if value is None or value <= 0:
        return None

    return 10 ** np.floor(np.log10(value))


def points_per_period(meta: dict) -> int | None:
    """
    Calculate the number of temporal samples per wave period.

    Parameters
    ----------
    meta : dict
        Metadata dictionary containing:

        - dt
        - freq

    Returns
    -------
    int | None

        Number of points per period:

        N = 2*pi / (freq * dt)

    Examples
    --------
    >>> meta = {
    ...     "dt": 0.1,
    ...     "freq": 0.5
    ... }

    >>> points_per_period(meta)
    126

    Notes
    -----
    Returned value is rounded to the nearest integer.

    Version
    -------
    1.0.0
    """

    dt = meta.get("dt")
    freq = meta.get("freq")

    if dt is None or freq is None:
        return None

    if dt <= 0 or freq <= 0:
        return None

    return int(round(
        2 * np.pi / (freq * dt)
    ))


def transform_dt(
    meta: dict,
    mode: str = "ppp",
):
    """
    Transform a time step value into a grouping value.

    Parameters
    ----------
    meta : dict
        Metadata dictionary.

    mode : str, optional
        Transformation mode.

        Supported values:

        - raw
        - order
        - ppp

    Returns
    -------
    float | int | None

    Modes
    -----
    raw
        Return dt directly.

    order
        Return order of magnitude of dt.

    ppp
        Return points per period.

    Examples
    --------
    >>> transform_dt(meta, "raw")

    >>> transform_dt(meta, "order")

    >>> transform_dt(meta, "ppp")

    Version
    -------
    1.0.0
    """

    dt = meta.get("dt")

    if mode == "raw":
        return dt

    if mode == "order":

        if dt is None or dt <= 0:
            return None

        return 10 ** np.floor(
            np.log10(dt)
        )

    if mode == "ppp":
        return points_per_period(meta)

    return dt


def transform_key(
    meta: dict,
    group_by: list[str],
    dt_mode: str = "ppp",
) -> tuple:
    """
    Generate a grouping key from metadata.

    Parameters
    ----------
    meta : dict
        Metadata dictionary.

    group_by : list[str]
        Metadata fields used for grouping.

    dt_mode : str, optional
        dt transformation mode.

    Returns
    -------
    tuple
        Immutable grouping key.

    Examples
    --------
    >>> transform_key(
    ...     meta,
    ...     ["freq", "dt"]
    ... )

    (0.5, 126)

    Version
    -------
    1.0.0
    """

    output = []

    for key in group_by:

        if key == "dt":

            value = transform_dt(
                meta,
                mode=dt_mode,
            )

        else:

            value = meta.get(key)

        output.append(value)

    return tuple(output)


def get_dt_label(
    dt_mode: str = "ppp",
) -> str:
    """
    Return a human-readable label describing the chosen
    time step transformation mode.

    Parameters
    ----------
    dt_mode : str

        Supported values:

        - raw
        - order
        - ppp

    Returns
    -------
    str

    Examples
    --------
    >>> get_dt_label("raw")
    'dt [s]'

    >>> get_dt_label("order")
    'dt (order)'

    >>> get_dt_label("ppp")
    'Points per period'

    Version
    -------
    1.0.0
    """

    labels = {
        "raw": "dt [s]",
        "order": "dt (order)",
        "ppp": "Points per period",
    }

    return labels.get(
        dt_mode,
        "dt",
    )