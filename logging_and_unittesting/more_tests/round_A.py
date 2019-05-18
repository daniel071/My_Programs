def round_number_a(n):
    if type(n) == float or type(n) == int:
        return round(n)

    else:
        raise TypeError("n must be an integer or float!")
