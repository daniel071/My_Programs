import math


def round_number_b(n):
    if type(n) == float or type(n) == int:

        return math.trunc(n)

    else:
        raise TypeError("n must be an integer or float!")
