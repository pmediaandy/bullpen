#!/usr/bin/env python

def get_max(A):
    mm = -1
    for x in A:
        mm = max(x, mm)
    return mm

def count(A, N):
    #print A
    C = [0] * N
    for n in A:
        C[n - 1] += 1
    #print C
    return C

def solution(N, A):
    LA = len(A)
    #print A
    mc = [0] * N
    B = []
    for i in xrange(LA):
        if A[i] <= N:
            B.append(A[i])
        elif A[i] == N + 1:
            if len(B) > 0:
                C = count(B, N)
                for j in xrange(N):
                    mc[j] += C[j]
                mm = get_max(mc)
                mc = [mm] * N
                B = []
                #print mc
    if len(B) > 0:
        C = count(B, N)
        for j in xrange(N):
            mc[j] += C[j]
        #print mc
    return mc

def solution_slow(N, A):
    C = [0] * (N + 1)
    mc = [0] * N
    for x in A:
        if x != N + 1:
            mc[x - 1] += 1
        else:
            m = get_max(mc)
            mc = [m] * N
    return mc

if __name__ == '__main__':
    print solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    print solution(5, [3, 4, 4, 6, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    print solution(5, [3, 4, 4, 6, 1, 6, 4, 4]) == [3, 3, 3, 5, 3]
    print solution(5, [3, 4, 4, 6, 3, 1, 6, 4, 4]) == [3, 3, 3, 5, 3]

