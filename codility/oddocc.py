#!/usr/bin/env python

def solution(A):
    #print A
    N = len(A)
    M = {}
    for x in A:
        if x not in M:
            M[x] = 1
        else:
            M[x] += 1
    #print M
    for x in M.keys():
        if M[x] % 2 == 1:
            return x
    return -1 

if __name__ == '__main__':
    print solution([9, 3, 9]) == 3
    print solution([3, 9, 3]) == 9
    print solution([2, 2, 4]) == 4
    print solution([9, 3, 9, 3, 9, 7, 9]) == 7

