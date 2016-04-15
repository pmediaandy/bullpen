#!/usr/bin/env python

def solution(A):
    #print A
    N = len(A)
    M = N + 1
    S = (1 + M) * M / 2
    #print S
    for n in A:
        S -= n
    #print S
    return S

if __name__ == '__main__':
    print solution([]) == 1
    print solution([2, 3, 1, 5]) == 4

