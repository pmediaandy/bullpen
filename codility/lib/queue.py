#!/usr/bin/env python

class queue:
    def __init__(self):
        self.vec = []

    def put(self, v):
        self.vec.append(v)

    def get(self):
        return self.vec.pop(0)

    def size(self):
        return len(self.vec)

if __name__ == '__main__':
    q = queue()
    for i in range(10):
        q.put(i)
    print q.vec
    while q.size() > 0:
        print '%d, size = %d' % (q.get(), q.size())
