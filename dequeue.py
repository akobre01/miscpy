class Dequeue:

    _array = []

    def insert(self, e):
        self._array.append(e)

    def head(self):
        return self._array.pop(0)

    def peek(self):
        return self._array[0]

    def peekLast(self):
        return self._array[-1]

    def eject(self):
        return self._array.pop()

    def length(self):
        return len(self._array)


d = Dequeue()
d.insert(1)
assert(d.peek() == d.peekLast())
d.insert(1)
assert(d.peek() == d.peekLast())
d.insert(2)
d.insert(3)
assert(d.eject() == 3)
assert(d.eject() == 2)
assert(d.head() == 1)
assert(d.head() == 1)
assert(d.length() == 0)
