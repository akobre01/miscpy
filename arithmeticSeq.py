import sys

"""
This is code that reads in from stdin:
  1. a number representing the number of elements I'm about to see
  2. a list of numbers seperated by a space that represent an arithmetic sequence

an arithmetic sequence (here) is a sequence of numbers in which the difference
between any two sequential numbers is the same.  One of then numbers in the
sequence is missing and this code finds that number in linear time.
"""

nums = int(sys.stdin.readline())
seq = map(lambda x: int(x), (sys.stdin.readline()).split(" "))

# there must be at least 4 elements in the list, otherwise you won't know
# what the difference between elements is
diff1 = seq[0] - seq[1]
diff2 = seq[1] - seq[2]
diff3 = seq[2] - seq[3]

if diff1 == diff2:
    truediff = diff1
elif diff2 == diff3:
    truediff = diff2
else:
    truediff = diff3

for i in xrange(len(seq)-1):
    if seq[i] - seq[i+1] != truediff:
        toReturn = seq[i] - truediff

print(toReturn)
