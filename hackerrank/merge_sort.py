#!/usr/bin/env python

import numpy as np

def merge_sort(a, v):
    l = 0
    r = len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] > v:
            r = m-1
        elif a[m] < v:
            l = m+1
        else:
            l=m
            break
    if l >= len(a):
        a.append(v)
    else:
        a.insert(l,v)

a = np.random.rand(1,100)
b = []
for x in a[0]:
    merge_sort(b, x)

s = True
c = sorted(b)
for i in range(len(b)):
    if b[i] != c[i]:
        s = False
print(s)

