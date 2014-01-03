def findBestLine(points):
    """
    give a list of points in a plane (2d), find the line that goes through
    the most of them
    """

    lines = {}
    for i in xrange(len(points)):
        for j in xrange(i+1, len(points)):
            p1, p2 = points[i], points[j]
            line = lineThroughPoints(p1,p2)
            if lines.has_key(line):
                lines[line] = lines[line].union(set([p1,p2]))
            else:
                lines[line] = set([p1,p2])

    bestLine = 0
    numPoints = 0
    for (line,pts) in lines.iteritems():
        if len(pts) > numPoints:
            numPoints = len(pts)
            bestLine = line

    return bestLine

def lineThroughPoints(p1, p2):
    (x1,y1) = p1
    (x2,y2) = p2
    if (x1 < x2):
        m = float(y2-y1)/(x2 - x1)
        b = round(y1 - m*x1, 9)
    elif (x1 > x2):
        m = float(y1 - y2)/(x1 - x2)
        b = round(y1 - m*x1, 9)
    else:
        m = float("inf")
        b = None

    return (m,b)

print(findBestLine([(1,2),(2,3),(3,4),(4,5),(1,3),(1,4),(12,11),(10,9),(-4,-7),(-8,-2)]))


# MENTAL CHECK
# (x1, y1) = (2,1)
# (x2, y2) = (3,2)
# m = (2-1)/(3-2) = 1
# b = 1 - 2 = -1
# check: when x = 0, y = -1 (true)
