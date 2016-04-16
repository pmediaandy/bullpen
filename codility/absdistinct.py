#!/usr/bin/env python

def show(S):
    #print S
    pass

def find_distinct(A):
    N = len(A)
    cnt = 1
    for i in xrange(1, N):
        if A[i] != A[i - 1]:
            cnt += 1
    show(cnt)
    return cnt 

def solution(A):
    show(A)
    N = len(A)
    if N == 1:
        return 1
    zidx = -1
    for i in xrange(N):
        if A[i] >= 0:
            zidx = i
            break
    if zidx <= 0:
        return find_distinct(A)
    L = A[0:zidx]
    L.reverse()
    L = map(lambda x: abs(x), L)
    R = A[zidx:]
    show(L)
    show(R)
    X = []
    r_idx = 0
    l_idx = 0
    while l_idx < len(L) and r_idx < len(R):
        if R[r_idx] <= L[l_idx]: 
            X.append(R[r_idx])
            r_idx += 1
        else:
            X.append(L[l_idx])
            l_idx += 1
        show(X)
    if l_idx < len(L):
        for i in xrange(l_idx, len(L)):
            X.append(L[i])
    if r_idx < len(R):
        for i in xrange(r_idx, len(R)):
            X.append(R[i])
    show(X)
    return find_distinct(X);

if __name__ == '__main__':
    print solution([1]) == 1
    print solution([1, 2, 3, 4]) == 4
    print solution([-1, 2, 3, 4]) == 4
    print solution([-1, 1, 3, 4]) == 3
    print solution([2, 2, 3, 3, 4]) == 3
    print solution([-5, -3, -1, 0, 3, 6]) == 5
    print solution([0, 3, 6]) == 3

