#!/usr/bin/env python

import random

def bin_ins_sort(a, v):
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

N = 100
a = []
for i in range(N):
    a.append(random.randint(0, 10000))
b = []
for x in a:
    bin_ins_sort(b, x)

s = True
c = sorted(a)
for i in range(len(a)):
    if b[i] != c[i]:
        s = False
print(s)

