def mod11(list, max_weight=7):

    """Implements Modulus 11 check digit algorithm.

    It's a variation of the HP's Modulus 11 algorithm.
    Requires the sequence to be calculated in a list of
    integers.
    The HP's Modulus 11 algorithm can be accessed through
    the following link:
    http://docs.hp.com/en/32209-90024/apds02.html

    """

    sum = 0
    weight = 2

    # Iterates through the list from right to left,
    # +multiplying each value for it's weight. If
    # +the weight reaches max_weight, then it is
    # +restarted to 2.
    for item in reversed(list):
        sum += item * weight
        weight += 1

        if weight > max_weight:
            weight = 2

    mod = 11 - sum % 11

    # HP's Modulus 11 algorithm says that a 10
    # +result is invalid and a 11 result is equal
    # +to 0. So, both values are returned as 0.
    if mod > 9:
        return 0

    else:
        return mod
