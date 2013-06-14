from heapq import nlargest
from math  import factorial

def bell(n):
    """
    compute the n+1 Bell number (starting at zero)
    Bell numbers can be computed using the following recursion:
    B_{n+1} = \sum_{i=0}^{n} {n \choose i} * B_{i}
    """
    assert(type(n) == int)

    def nextBell(bellnums):
        """Given a sequence of Bell numbers compute the next one"""

        N = len(bellnums)
        combs = [ factorial(N-1) / (factorial(i) * factorial(N-1-i))
                  for i in range(N) ]
        bellnums.append(sum(map(lambda (x, y): x * y, zip(combs, bellnums))))
        return bellnums

    bellnums = [1]        # base case
    for i in range(n):
        bellnums = nextBell(bellnums)
    return bellnums[-1]

def partitions(elems):
    """
    Returns a generator that, when called, returns another paritition of
    the elements in elems.  This will eventually return all partitions of
    the elements (the number of partitions is a Bell number--see above)

    The method used here generates an encoding that assigns elements to
    partitions. The encoding has the same number of items as elems. The
    item at index i in the encoding is an integer that maps elems[i] to a
    partition
    """

    def code2partition(elems, encoding):
        """
        given a set of elements and an encoding, return a list of lists
        that partitions the elements (according to the encoding)
        """

        partition = [ list() for _ in xrange(len(elems)) ]
        for i in xrange(len(encoding)):
            partition[encoding[i]].append(elems[i])

        return partition

    def incrementEncoding(encoding, digit = -1):
        """
        try to increment the number at index digit in the encoding
        if you are successful, return the new encoding, otherwise
        return false

        basically you need to check a few things:
        1) the digit you want to increment is not already bigger than all
        other digits (cause the encoding 1,1,2 is equivalent to 1,1,3)
        2) the digit you want to increment is within the appropriate range
        (if you translate an encoding to an integer, the largest encoding
        should be {1,2,...,N-1})
        """

        if digit == -1:
            digit = len(encoding) - 1

        if encoding[digit] < digit:
            largest = nlargest(2, encoding)
            if largest[0] == largest[1] or encoding[digit] != max(largest):
                encoding[digit] += 1
                return encoding

        # if you can't increase the digit, set it back to zero and move to the
        # next digit
        encoding[digit] = 0
        return incrementEncoding(encoding, digit-1)

    N = len(elems)
    encoding = [0] * N        # base case: all elems in the same partition
    for i in xrange(bell(N)):
        partitions = code2partition(elems, encoding)
        encoding   = incrementEncoding(encoding)
        yield(partitions)
