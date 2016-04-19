#!/usr/bin/env python

def show(S):
    #print S
    pass

def solution(A):
    show(A)
    N = len(A)
    mm = (-2147483647 - 1)
    for i in xrange(N):
        for j in xrange(i, N):
            ss = A[i] + A[j] + (j - i)
            show('%d %d = %d' % (i, j, ss))
            mm = max(ss, mm)
    show(mm)
    return mm

if __name__ == '__main__':
    print solution([1, 3, -3]) == 6
    print solution([-8, 4, 0, 5, -3, 6]) == 14
    print solution([1]) == 2
    print solution([2]) == 4
    print solution([-2]) == -4
    print solution([-2, 3]) == 6

