#!/usr/bin/env python

def show(S):
    print S
    pass

class stack:
    def __init__(self):
        self.vec = []

    def push(self, v):
        self.vec.append(v)

    def pop(self):
        return self.vec.pop()

    def size(self):
        return len(self.vec)

def solution(A):
    show(A)
    N = len(A)
    s = stack()
    cc = None
    for num in A:
        s.push(num)
        if s.size() >= 2:
            if s.vec[-1] != s.vec[-2]:
                s.pop()
                s.pop()
        if s.size() > 0:
            cc = s.vec[0]
        else:
            cc = None
    cnt = 0
    for i in xrange(N):
        if A[i] == cc:
            cnt += 1
    if cnt > N // 2:
        return cc
    return -1


def solution_slow(A):
    N = len(A)
    C = {}
    for num in A:
        if num in C:
            C[num] = C[num] + 1
        else:
            C[num] = 0
    for num in C.keys():
        if C[num] > N/2:
            return num
    return -1

if __name__ == '__main__':
    print solution([4 , 2 , 2 , 3 , 2 , 4 , 2 , 2 , 6 , 4]) == -1
    print solution([1, 1, 1, 50, 1]) == 1
    print solution([1]) == 1

