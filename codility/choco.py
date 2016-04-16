#!/usr/bin/env python

def show(S):
    #print S
    pass

def solution(N, M):
    show('%d %d' % (N, M))
    V = [1] * N
    show(V)
    idx = M
    V[0] = 0
    cnt = 1
    while True:
        if V[idx % N] == 0:
            break
        V[idx % N] = 0
        cnt += 1
        idx += M
    show(cnt)
    return cnt

if __name__ == '__main__':
    print solution(10, 4) == 5
    print solution(1, 1) == 1
    print solution(3, 2) == 3

