import numpy
from scipy import stats


def calculate_mean(data_set):
    """
    This method calculates mean
    :type data_set: int[]
    :rtype: None
    """

    x = numpy.mean(data_set)  # calculate mean

    print(x)


def calculate_median(data_set):
    """
    This method calculates median
    :type data_set: int[]
    :rtype: None
    """

    x = numpy.median(data_set)

    print(x)


def calculate_mode(data_set):
    """
    This method calculates mode
    :type data_set: int[]
    :rtype: None
    """

    x = stats.mode(data_set)

    # print(type(x))
    print(x.mode[0])


data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
calculate_mean(data)

calculate_median(data)

calculate_mode(data)
