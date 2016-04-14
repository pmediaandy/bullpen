#!/usr/bin/env python

def solution(A):
    N = len(A)
    #print A
    S = []
    sum = 0
    for i in range(0, N):
        S.append(sum + A[i])
        sum = sum + A[i]
    #print S
    for i in range(0, N):
        if i == 0:
            left = 0
        else:
            left = S[i - 1]
        if i + 1 == N:
            right = 0
        else: 
            right = S[N - 1] - S[i]
        if left == right:
            #print '%d %d %d' % (i, left, right)
            return i
    return -1

if __name__ == '__main__':
    assert solution([-1, 3, -4, 5, 1, -6, 2, 1]) in [ 1, 3, 7 ]

