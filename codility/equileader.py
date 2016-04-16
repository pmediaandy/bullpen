#!/usr/bin/env python

def show(S):
    #print S
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

def leader(A):
    #show(A)
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

def solution(A):
    show(A)
    N = len(A)
    if N == 1:
        return 0 
    if N == 2:
        if A[0] != A[1]:
            return 0
        else:
            return 1
    cnt = 0
    for i in xrange(1, N, 2):
        X = A[0:i]
        Y = A[i:]
        show(X)
        show(Y)
        LX = leader(X)
        LY = leader(Y)
        if LX != -1 and LY != -1 and LX == LY:
            cnt += 1
    return cnt

if __name__ == '__main__':
    print solution([4, 4, 2, 5, 3, 4, 4, 4]) == 3
    print solution([4]) == 0
    print solution([4, 3]) == 0
    print solution([4, 4]) == 1
    print solution([4, 3, 4, 4, 4, 2]) == 2

