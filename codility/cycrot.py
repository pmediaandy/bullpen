#!/usr/bin/env python

def shift_one(A):
    last = A.pop()
    A.insert(0, last)
    #print A

def solution(A, K):
    #print A
    N = len(A)
    if N == 0:
        return []
    if K % N == 0:
        return A
    for i in xrange(K):
        shift_one(A)
    return A

if __name__ == '__main__':
    print solution([], 1) == []
    print solution([3, 8], 1) == [8, 3]
    print solution([3, 8], 2) == [3, 8]
    print solution([3, 8], 0) == [3, 8]
    print solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

