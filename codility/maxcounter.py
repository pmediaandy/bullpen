#!/usr/bin/env python

def get_max(A):
    mm = -1
    for x in A:
        mm = max(x, mm)
    return mm

max_count = 0

def count(num, C):
    global max_count
    if C[num - 1] + 1 > max_count:
        max_count = C[num - 1] + 1
    C[num - 1] += 1
    return C

def solution(N, A):
    global max_count
    max_count = 0
    LA = len(A)
    mc = [0] * N
    seq_cnt = 0
    for i in xrange(LA):
        if A[i] <= N:
            mc = count(A[i], mc)
            seq_cnt += 1
        elif A[i] == N + 1:
            if seq_cnt > 0:
                mc = [max_count] * N
                seq_cnt = 0
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

