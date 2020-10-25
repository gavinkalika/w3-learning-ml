import numpy


def calculate_std_deviation(data_set):
    """
    This method calculates standard deviation
    :type data_set: int[]
    :rtype: None
    """

    std = numpy.std(data_set)
    mean = numpy.mean(data_set)
    var = numpy.var(data_set)

    print("Mean {0} and std dev {1} and variance {2}".format(mean, std, var))


data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
calculate_std_deviation(data)
