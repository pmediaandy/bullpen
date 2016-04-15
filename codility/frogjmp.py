#!/usr/bin/env python

def solution(X, Y, D):
    dist = Y - X
    if dist % D == 0:
        return dist / D
    return dist / D + 1

if __name__ == '__main__':
    print solution(10, 10, 3) == 0
    print solution(10, 20, 2) == 5
    print solution(10, 19, 2) == 5
    print solution(10, 21, 2) == 6
    print solution(10, 85, 30) == 3

