import numpy as np


def bootstrap_ci(
    data: np.ndarray,
    func,
    n_boot: int = 100,
) -> tuple[float, float]:
    """
    Estimate a confidence interval using bootstrap resampling.

    The bootstrap method repeatedly samples the original dataset
    with replacement and evaluates a user-specified statistic.
    The resulting distribution of statistics is used to estimate
    the confidence interval.

    Parameters
    ----------
    data : numpy.ndarray
        One-dimensional array containing the sample data.

    func : callable
        Statistical function to evaluate on each bootstrap sample.

        Common examples include:

        - numpy.mean
        - numpy.std
        - numpy.median
        - custom user defined functions

    n_boot : int, optional
        Number of bootstrap realizations.

        Larger values generally produce more stable confidence
        interval estimates at the cost of additional computation.

        Default is 100.

    Returns
    -------
    tuple[float, float]
        Lower and upper bounds of the 95% confidence interval.

        Returns:

        (
            lower_confidence_limit,
            upper_confidence_limit
        )

    Notes
    -----
    Sampling is performed with replacement.

    The confidence interval is computed using the percentile
    method:

    - Lower bound = 2.5th percentile
    - Upper bound = 97.5th percentile

    Examples
    --------
    Compute confidence interval for the mean:

    >>> data = np.array([1, 2, 3, 4, 5])

    >>> low, high = bootstrap_ci(
    ...     data,
    ...     np.mean,
    ...     n_boot=1000
    ... )

    >>> print(low, high)

    Compute confidence interval for the standard deviation:

    >>> low, high = bootstrap_ci(
    ...     data,
    ...     np.std
    ... )

    See Also
    --------
    numpy.mean
    numpy.std
    numpy.percentile

    Version
    -------
    1.0.0

    Author
    ------
    Lorenzo Zambelli
    """

    N = len(data)

    stats = np.empty(n_boot)

    for i in range(n_boot):

        sample = np.random.choice(
            data,
            size=N,
            replace=True
        )

        stats[i] = func(sample)

    return (
        np.percentile(stats, 2.5),
        np.percentile(stats, 97.5),
    )
    
    
def exceedance(data):
    """
    Compute exceedance probability distribution.

    Parameters
    ----------
    data : numpy.ndarray
        Input sample data.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]

        (
            sorted_data,
            exceedance_probability
        )

    Notes
    -----
    Exceedance probability is defined as:

        P(X > x)

    and is computed using:

        1 - i/N

    Examples
    --------
    >>> x, p = exceedance(data)
    """

    data = np.sort(data)

    n = len(data)

    probability = (
        1.0
        - np.arange(1, n + 1) / n
    )

    return data, probability