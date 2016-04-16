#!/usr/bin/env python

def show(str):
    #print str
    pass

def solution(S):
    show(S)
    N = len(S)
    if N  == 0:
        return 1
    if N == 1:
        return 0
    q = []
    for c in S:
        if c is '(':
            q.append(')')
        elif c is '[':
            q.append(']')
        elif c is '{':
            q.append('}')
        elif c is ')' or c is ']' or c is '}':
            if len(q) == 0: 
                return 0
            v = q.pop()
            if v != c:
                return 0
    if len(q) != 0:
        return 0
    return 1 


if __name__ == '__main__':
    print solution('') == 1
    print solution('{') == 0
    print solution('{{') == 0
    print solution('{{{') == 0
    print solution(']]))') == 0
    print solution('()([)]]))') == 0
    print solution('{[()()]}') == 1
    print solution('([)()]') == 0

