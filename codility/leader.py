#!/usr/bin/env python

def solution(A):
    N = len(A)
    C = {}
    for num in A:
        if num in C:
            C[num] = C[num] + 1
        else:
            C[num] = 0
    for num in C.keys():
        if C[num] > N/2:
            return num
    return -1 

if __name__ == '__main__':
    print solution([4 , 2 , 2 , 3 , 2 , 4 , 2 , 2 , 6 , 4])
    print solution([1, 1, 1, 50, 1])

