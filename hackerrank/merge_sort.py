#!/usr/bin/env python

import random

def merge(left, right):
    res = []
    while True:
        if len(left) == 0:
            res += right
            break
        elif len(right) == 0:
            res += left
            break
        elif left[0] > right[0]:
            res += [ right.pop(0) ]
        else:
            res += [ left.pop(0) ]
        if len(left) == 0 and len(right) == 0:
            break
    #print(res)
    return res
    
def merge_sort(a):
    N = len(a)
    if N == 1:
        return a
    else:
        m = N//2
        left = a[0:m]
        right = a[m:]
        #print('%s %s' % (left, right))
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

N = 100
a = []
for i in range(N):
    a.append(random.randint(0, 10000))
b = merge_sort(a)

s = True
c = sorted(a)
for i in range(len(a)):
    if b[i] != c[i]:
        s = False
print(s)

