#!/usr/bin/env python

def show(S):
    #print S
    pass

def solution(N):
    show(N)
    i = 1
    cnt = 0
    while i * i < N:
        if N % i == 0:
            cnt += 2
        i += 1
    if i * i == N:
        cnt += 1
    show(cnt)
    return cnt

if __name__ == '__main__':
    print solution(24) == 8
    print solution(9) == 3
    print solution(17) == 2

