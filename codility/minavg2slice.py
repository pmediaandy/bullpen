#!/usr/bin/env python

# https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/

def solution_fast(A):
    min_avg_value = (A[0] + A[1])/2.0   # The mininal average
    min_avg_pos = 0     # The begin position of the first
                        # slice with mininal average

    for index in xrange(0, len(A)-2):
        # Try the next 2-element slice
        if (A[index] + A[index+1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index+1] + A[index+2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1] + A[index+2]) / 3.0
            min_avg_pos = index

    # Try the last 2-element slice
    if (A[-1]+A[-2])/2.0 < min_avg_value:
        min_avg_value = (A[-1]+A[-2])/2.0
        min_avg_pos = len(A)-2

    return min_avg_pos

def solution(A):
    #print A
    N = len(A)
    S = [0] * N
    sum = 0
    for i in xrange(N):
        S[i] = sum + A[i]
        sum += A[i]
    #print S
    mm = 2147483647 
    min_p = -1
    for i in xrange(0, N):
        for j in xrange(i + 1, N):
            #print '%d %d' % (i, j)
            sum = S[j] - S[i] + A[i]
            avg = float(sum) / (j - i + 1)
            #print avg
            if avg < mm:
                mm = avg
                min_p = i
    return min_p

if __name__ == '__main__':
    print solution([4, 2, 2, 5, 1, 5, 8]) == 1

