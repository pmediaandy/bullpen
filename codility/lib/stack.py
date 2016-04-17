#!/usr/bin/env python

class stack:
    def __init__(self):
        self.vec = []

    def push(self, v):
        self.vec.append(v)

    def pop(self):
        return self.vec.pop()

    def size(self):
        return len(self.vec)

if __name__ == '__main__':
    s = stack()
    for i in range(10):
        s.push(i)
    print s.vec
    while s.size() > 0:
        print '%d: size = %d' % (s.pop(), s.size())
