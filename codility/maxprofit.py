#!/usr/bin/env python

def show(S):
    #print S
    pass

def solution(A):
    show(A)
    N = len(A)
    if N == 0:
        return 0
    if N == 1:
        return 0
    S = [0] * N
    acc = 0
    for i in xrange(N):
        S[i] = acc + A[i]
        acc += A[i]
    show(S)
    max_pro = 0
    for i in xrange(0, N):
        for j in xrange(i, N):
            show('%d %d' % (i, j))
            max_pro = max(max_pro, A[j] - A[i])
    show(max_pro)
    return max_pro

import random
#print(random.randint(0,9))

if __name__ == '__main__':
    print solution([23171 , 21011 , 21123 , 21366 , 21013 , 21367]) == 356
    print solution([]) == 0
    print solution([4]) == 0
    print solution([2, 1]) == 0
    print solution([8292, 2434, 1652, 2983, 6716, 1697, 9620, 8709, 5314, 8626, 4746, 3307, 6816, 8814, 8321, 997, 2792, 1551, 3369, 7453]) == 7968

    """
    K = [0] * 20
    for i in xrange(20):
        K[i] = random.randint(0, 10000)
    print K
    print solution_slow(K)
    """
