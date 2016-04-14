#!/usr/bin/env python

def solution(L):
    count = 0
    while L:
        count += 1
        L = L.next
    return count

if __name__ == '__main__':
    pass

