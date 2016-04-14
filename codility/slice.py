#!/usr/bin/env python

def solution(A, S):
    #print A
    N = len(A)
    sum = 0
    B = []
    for i in range(0, N):
        B.append(sum + A[i])
        sum += A[i]
    #print B
    mm = -1
    for i in range(0, N):
        for j in range(i, N):
            d = B[j] - B[i] + A[i]
            if d == S:
                mm = max(mm, j - i + 1)
    return mm

if __name__ == '__main__':
    assert solution([1 , 0 , -1 , 1 , 1 , -1 , -1], 2) == 5

