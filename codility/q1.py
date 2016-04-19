#!/usr/bin/env python

def show(S):
    #print S
    pass

def max_slice(A):
    show(A)
    N = len(A)
    S = []
    sum = 0 
    for i in range(0, N): 
        S.append(sum + A[i])
        sum = sum + A[i]
    #show(S)
    mm = -1
    for i in xrange(N):
        for j in xrange(i, N):
            ss = S[j] - S[i] + A[i]
            show('%d %d = %d' % (i, j, ss))
            mm = max(ss, mm)
    show(mm)
    return mm

def solution(A):
    show(A)
    N = len(A)
    if N == 0:
        return 0
    i = 0
    K = []
    mm = 0
    while True and i < N:
        if A[i] < 0:
            if len(K) > 0:
                ss = max_slice(K)
                mm = max(mm, ss)
                K = []
            i += 1
        else:
            K.append(A[i])
            i += 1
    if len(K) > 0:
        ss = max_slice(K)
        mm = max(mm, ss)
        K = []
    show(mm)
    return mm

if __name__ == '__main__':
    print solution([]) == 0
    print solution([1]) == 1
    print solution([1, 2, -3, 4, 5, -6]) == 9
    print solution([-8, 3, 0, 5, -3, 12]) == 12
    print solution([-1, 2, 1, 2, 0, 2, 1, -3, 4, 3, 0, -1]) == 8
    print solution([-1]) == 0 
    print solution([1, -1, 2]) == 2 
    print solution([1, 1, -1, 2]) == 2 
    print solution([1, 2, -1, 2]) == 3 
    print solution([1, 2, -1, 4]) == 4 
    print solution([1, 2, -1, 1, 1, 1, 1, 1]) == 5 
    print solution([-1, 1, 1, -1]) == 2 

