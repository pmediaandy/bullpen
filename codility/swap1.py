#!/usr/bin/env python

def solution(A):
    N = len(A)
    print A
    D = sorted(A)
    print D
    d = 0
    for i in range(0, N):
        if A[i] != D[i]:
            d += 1
    if d == 2:
        return True
    return False


if __name__ == '__main__':
    assert solution([1, 3, 5, 3, 7]) == True
    assert solution([1, 3, 5, 3, 4]) == False
    assert solution([1, 6, 3, 4, 3, 7]) == True
    assert solution([1, 6, 5, 3, 3, 4, 7]) == False
    assert solution([6, 3, 4, 2, 7]) == True

