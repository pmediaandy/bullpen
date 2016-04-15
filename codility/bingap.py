#!/usr/bin/env python

def solution(N):
    d = []
    while N > 0:
        d.append(N % 2)
        N = N >> 1
    mm = 0
    d.reverse()
    #print d
    for i in xrange(len(d)):
        if d[i] == 1:
            gap = 0
            stop = False
            for j in xrange(i + 1, len(d)):
                if d[j] == 0:
                    gap += 1
                elif d[j] == 1:
                    stop = True
                    break
            if stop == True:
                mm = max(mm, gap)
                i = j - 1
    #print mm
    return mm

if __name__ == '__main__':
    print solution(9) == 2
    print solution(16) == 0
    print solution(2147483647) == 0
    print solution(529) == 4
    print solution(20) == 1
    print solution(15) == 0
    print solution(1041) == 5
