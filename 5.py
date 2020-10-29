import numpy
import matplotlib.pyplot as plt


def display_histogram():
    """
    Creates a random histogram
    :rtype: None
    """

    x = numpy.random.uniform(0.0, 5.0, 100000)

    plt.hist(x, 100)
    plt.show()


display_histogram()
