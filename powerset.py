def powerset(s):
    """
    s is a list --- return the power set
    """
    sset = set(s)
    nelems = len(sset)
    for i in xrange(nelems**2):
        print printSet(binaryToSet(addLeadingZero(map(int, list(bin(i))[2:]), nelems), sset))

def addLeadingZero(l, size):
    for i in xrange(size - len(l)):
        l.insert(0, 0)
    return l

def binaryToSet(number,s):
    return set(map(lambda (x,y): y, (filter(lambda (x,y): x == 1, zip(number, s)))))

def printSet(s):
    return "{" + ",".join(map(lambda x: str(x), s)) + "}"

powerset([1,2,3,4,5])
