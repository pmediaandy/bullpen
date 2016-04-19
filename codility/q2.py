#!/usr/bin/env python

def show(S):
    #print S
    pass

def get_stamp(T):
    v = T.split(':')
    return int(v[0]) * 3600 + int(v[1]) * 60 + int(v[2])

def make_string(tt):
    v1 = tt / 3600
    v2 = (tt % 3600) / 60
    v3 = tt % 60
    return '%02d:%02d:%02d' % (v1, v2, v3)

def solution(S, T):
    show('%s - %s' % (S, T))
    ts = get_stamp(S)
    tt = get_stamp(T)
    show('%d - %d' % (ts, tt))
    cnt = 0
    for x in xrange(ts, tt + 1):
        sx = make_string(x)
        show('%s - %d' % (sx, x))
        sx = sx.replace(':', '')
        mm = {}
        for c in sx:
            mm[c] = 1
        if len(mm.keys()) <= 2:
            show('yes')
            cnt += 1
    return cnt

if __name__ == '__main__':
    print solution('15:15:00', '15:15:12') == 1
    print solution('22:22:21', '22:22:23') == 3
    print solution('00:00:00', '00:00:01') == 2
    print solution('00:00:00', '00:00:10') == 11

