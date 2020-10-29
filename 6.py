import numpy
import matplotlib.pyplot as plt


def display_histogram():
    """
    Creates a random histogram
    :rtype: None
    """

    # mean value is 5
    # the std devation is 1
    # Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
    # 100000 random values.
    x = numpy.random.normal(5.0, 1.0, 100000)

    plt.hist(x, 100)
    plt.show()


display_histogram()
