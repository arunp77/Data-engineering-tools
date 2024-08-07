import statistics as stats

def mean(data):
    """
    Calculate the mean (average) of a dataset.

    Parameters:
    data (list of float): The dataset for which the mean is to be calculated.

    Returns:
    float: The mean of the dataset.

    Raises:
    ValueError: If the dataset is empty.

    Examples:
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([10, 20, 30])
    20.0
    """
    if not data:
        raise ValueError('mean requires at least one data point')
    return stats.mean(data)


def median(data):
    """
    Calculate the median of a dataset.

    Parameters:
    data (list of float): The dataset for which the median is to be calculated.

    Returns:
    float: The median of the dataset.

    Raises:
    ValueError: If the dataset is empty.

    Examples:
    >>> median([1, 2, 3, 4, 5])
    3.0
    >>> median([1, 3, 3, 6, 7, 8, 9])
    6.0
    """
    if not data:
        raise ValueError('median requires at least one data point')
    return stats.median(data)

def mode(data):
    """
    Calculate the mode of a dataset.

    Parameters:
    data (list of float): The dataset for which the mode is to be calculated.

    Returns:
    float: The mode of the dataset. If there are multiple modes, returns the first one found.

    Raises:
    ValueError: If no mode is found (all values occur with the same frequency).

    Examples:
    >>> mode([1, 2, 2, 3, 4])
    2
    >>> mode([1, 1, 2, 2, 3, 3])
    1
    """
    if not data:
        raise ValueError('mode requires at least one data point')
    try:
        return stats.mode(data)
    except stats.StatisticsError as e:
        raise ValueError('No mode found: ' + str(e))

def variance(data):
    """
    Calculate the variance of a dataset.

    Parameters:
    data (list of float): The dataset for which the variance is to be calculated.

    Returns:
    float: The variance of the dataset.

    Raises:
    ValueError: If the dataset is empty or has less than two data points.

    Examples:
    >>> variance([1, 2, 3, 4, 5])
    2.5
    >>> variance([10, 20, 30])
    100.0
    """
    if len(data) < 2:
        raise ValueError('variance requires at least two data points')
    return stats.variance(data)

def standard_deviation(data):
    """
    Calculate the standard deviation of a dataset.

    Parameters:
    data (list of float): The dataset for which the standard deviation is to be calculated.

    Returns:
    float: The standard deviation of the dataset.

    Raises:
    ValueError: If the dataset is empty or has less than two data points.

    Examples:
    >>> standard_deviation([1, 2, 3, 4, 5])
    1.58
    >>> standard_deviation([10, 20, 30])
    10.0
    """
    if len(data) < 2:
        raise ValueError('standard deviation requires at least two data points')
    return stats.stdev(data)
