"""
Data Grouping Utilities
=======================

Module
------
rayleigh.processing.grouping

Description
-----------
Provides functionality for:

* Loading Rayleigh datasets
* Applying filters
* Grouping results
* Combining wave statistics

This module is shared between:

* Single-study analysis
* Multi-study comparison analysis

Author
------
Lorenzo Zambelli

Version
-------
2.0.0
"""

from collections import defaultdict
import numpy as np

from utils.filters import passes_filter
from utils.utils import transform_key


def collect(
    data,
    filters,
    group_by,
    dt_mode="ppp",
    include_study=False,
):
    """
    Group processed wave data.

    Parameters
    ----------
    data : list
        Processed results.

        Single-study format:

        (
            meta,
            wave,
            m0
        )

        Comparison format:

        (
            study,
            meta,
            wave,
            m0
        )

    filters : dict
        Filter definitions.

    group_by : list[str]
        Variables used for grouping.

    dt_mode : str, optional
        dt transformation mode.

    include_study : bool, optional
        If True, study name becomes part
        of grouping key.

    Returns
    -------
    dict

        {
            key : {
                "wave": ndarray,
                "m0": float
            }
        }

    Examples
    --------
    >>> groups = collect(
    ...     data,
    ...     filters,
    ...     ["freq"]
    ... )

    >>> len(groups)
    12
    """

    groups = defaultdict(
        lambda: {
            "wave": [],
            "m0": [],
        }
    )

    for item in data:

        if include_study:

            study, meta, wave, m0 = item

        else:

            meta, wave, m0 = item

        if not all(
            passes_filter(
                meta.get(k),
                filters.get(k),
            )
            for k in filters
        ):
            continue

        key = transform_key(
            meta,
            group_by,
            dt_mode=dt_mode,
        )

        if include_study:

            key = (study,) + key

        groups[key]["wave"].append(wave)
        groups[key]["m0"].append(m0)

    for key in groups:

        groups[key]["wave"] = np.concatenate(
            groups[key]["wave"]
        )

        groups[key]["m0"] = float(
            np.mean(groups[key]["m0"])
        )

    return groups