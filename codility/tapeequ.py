#!/usr/bin/env python

def solution(A):
    #print A
    N = len(A)
    S = []
    sum = 0
    for i in xrange(N):
        S.append(sum + A[i])
        sum += A[i]
    #print S
    mm = 2147483647
    for i in xrange(1, N):
        left = S[i - 1]
        right = S[N - 1] - S[i - 1]
        diff = abs(left - right)
        mm = min(mm, diff)
    return mm

if __name__ == '__main__':
    print solution([3, 1]) == 2
    print solution([3, 1, 2, 4, 3]) == 1

