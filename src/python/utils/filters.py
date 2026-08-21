"""
Filtering Utilities
===================

Module
------
utils.filters

Description
-----------
Reusable filtering helpers used across validation,
Rayleigh, spectral and plotting projects.

A filter may be:

* None
* exact value
* tuple(lower, upper)
* list
* set

Author
------
Lorenzo Zambelli

Version
-------
1.0.0
"""

from __future__ import annotations


def passes_filter(
    value,
    condition,
) -> bool:
    """
    Check whether a value satisfies a filter condition.

    Parameters
    ----------
    value : Any
        Metadata value being tested.

    condition : Any
        Filter definition.

        Supported formats:

        None
            Always passes.

        tuple(lower, upper)
            Inclusive range filter.

        list
            Allowed values.

        set
            Allowed values.

        scalar
            Exact match.

    Returns
    -------
    bool
        True if the value satisfies the condition.

    Examples
    --------
    >>> passes_filter(5, (1, 10))
    True

    >>> passes_filter(15, (1, 10))
    False

    >>> passes_filter(
    ...     "A",
    ...     ["A", "B"]
    ... )
    True

    >>> passes_filter(
    ...     "C",
    ...     ["A", "B"]
    ... )
    False

    Version
    -------
    1.0.0
    """

    if condition is None:
        return True

    if value is None:
        return False

    # ------------------------------------------
    # multi-value filter
    # ------------------------------------------

    if isinstance(condition, (list, set)):
        return value in condition

    # ------------------------------------------
    # range filter
    # ------------------------------------------

    if isinstance(condition, tuple):

        lower, upper = condition

        if lower is not None and value < lower:
            return False

        if upper is not None and value > upper:
            return False

        return True

    # ------------------------------------------
    # exact match
    # ------------------------------------------

    return value == condition


def apply_filters(
    metadata: dict,
    filters: dict,
) -> bool:
    """
    Apply an entire filter dictionary to metadata.

    Parameters
    ----------
    metadata : dict
        Metadata dictionary.

    filters : dict
        Filter definitions.

    Returns
    -------
    bool
        True if all filters pass.

    Examples
    --------
    >>> metadata = {
    ...     "angle": 45,
    ...     "depth": 25
    ... }

    >>> filters = {
    ...     "angle": (30, 90),
    ...     "depth": (20, 30)
    ... }

    >>> apply_filters(
    ...     metadata,
    ...     filters
    ... )
    True

    Version
    -------
    1.0.0
    """

    return all(
        passes_filter(
            metadata.get(key),
            filters.get(key),
        )
        for key in filters
    )


def filter_data(
    data,
    filters,
    metadata_index=0,
):
    """
    Filter a collection of results.

    Parameters
    ----------
    data : iterable
        Collection of result tuples.

    filters : dict
        Filters to apply.

    metadata_index : int
        Tuple index containing metadata.

    Returns
    -------
    list
        Filtered records.

    Examples
    --------
    >>> filtered = filter_data(
    ...     results,
    ...     filters
    ... )

    Version
    -------
    1.0.0
    """

    output = []

    for item in data:

        metadata = item[metadata_index]

        if apply_filters(
            metadata,
            filters,
        ):
            output.append(item)

    return output
    
def format_filters(filters: dict) -> str:
    """
    Convert a filter dictionary into a compact,
    filename-safe string representation.

    Parameters
    ----------
    filters : dict
        Dictionary containing filter definitions.

    Returns
    -------
    str
        Formatted filter string.

    Examples
    --------
    >>> format_filters(
    ...     {
    ...         "angle": (30, 90),
    ...         "depth": (22.5, 50)
    ...     }
    ... )
    'angle30-90_depth22.5-50'

    >>> format_filters({})
    'nofilter'

    Notes
    -----
    Output is primarily intended for:

    - filenames
    - plot titles
    - report identifiers
    - cache names

    Version
    -------
    1.0.0
    """

    parts = []

    for key, value in filters.items():

        if value is None:
            continue

        if isinstance(value, tuple):

            lower, upper = value

            if lower is not None and upper is not None:

                parts.append(
                    f"{key}{lower}-{upper}"
                )

            elif lower is not None:

                parts.append(
                    f"{key}{lower}+"
                )

            elif upper is not None:

                parts.append(
                    f"{key}0-{upper}"
                )

        else:

            parts.append(
                f"{key}{value}"
            )

    return (
        "_".join(parts)
        if parts
        else "nofilter"
    )