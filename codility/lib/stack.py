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

