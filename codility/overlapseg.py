#!/usr/bin/env python

def show(S):
    print S
    pass

def solution(A, B):
    show(A)
    show(B)
    N = len(A)
    for i in xrange(1, N):
        for j in xrange(0, i):
            if B[i] == B [j]:
                show('%d %d' % (j, i))
            elif A[i] <= B[j] and A[i] >= A [j]:
                show('%d %d' % (j, i))
            elif A[j] <= B[i] and A[j] >= A [i]:
                show('%d %d' % (j, i))

if __name__ == '__main__':
    print solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]) == 3
    print solution([1, 3, 0, 6], [2, 4, 5, 7]) == 3

