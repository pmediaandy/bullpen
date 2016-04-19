#!/usr/bin/env python

def show(S):
    #print S
    pass

A = []

def make_table():
    global A
    if len(A) > 0:
        return
    show('make table')
    for i in xrange(20):
        for j in xrange(20):
            nn = 2**i * 3**j
            A.append(nn)
    A.sort()
    show(len(A))
    show(A)
    return A

def solution(N):
    show(N)
    make_table()
    global A
    return A[N]

if __name__ == '__main__':
    print solution(4) == 6
    print solution(7) == 12
    print solution(0) == 1

