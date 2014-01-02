def maxDiff(l):
    """
    pass in a list and find the maximum difference between any
    two elements, max(e_i - e_j), in the list such that i > j

    this algorithm operates in linear time
    """

    m = int("inf")
    diff = int("-inf")
    for e in l:
        if e < m:
            m = e

        if e - m > diff:
            diff = e - m

    return diff
