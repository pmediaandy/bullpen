#!/usr/bin/env python

def is_triangle(s, t, v):
    return s + t > v and t + v > s and s + v > t

def solution(A):
    #print A
    N = len(A)
    if N < 3:
        return 0
    A.sort()
    #print A
    for i in xrange(2, N):
        if is_triangle(A[i-2], A[i-1], A[i]):
            return 1
    return 0

if __name__ == '__main__':
    print solution([]) == 0
    print solution([1]) == 0
    print solution([1, 2]) == 0
    print solution([10, 2, 5, 1, 8, 20]) == 1
    print solution([10, 50, 5, 1]) == 0

