#!/usr/bin/python

import sys
import getopt
import os
import re
import datetime
import time
import traceback

class PDNS_Record:
    query_pos = -1
    response_pos = -1 
    answer_pos = -1 
    ans_cnt = -1
    ips = []
    line = []
    param = {}

    def reset(self):
        self.query_pos = -1
        self.response_pos = -1 
        self.answer_pos = -1 
        self.ans_cnt = -1 
        self.ips = []
        self.line = []
        self.param = {}

    def __init__(self):
        self.reset()

    def match_response(self, line):
        self.ans_cnt = -1
        c1 = line.find('ANSWER: ')
        if c1 == -1: return
        c2 = line[c1 + 8:].find(',')
        self.ans_cnt = int(line[c1 + 8:c1 + 8 + c2])

    def parse_tstamp(self, line):
        line = line[line[1:].find('[') + 1:]
        timestr = line[1:20]
        tmpdt = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(tmpdt.timetuple()))

    def trim_code(self, msg):
        return re.split(' ', msg)[0]

    def output(self):
        self.param['t'] = self.parse_tstamp(self.line[0])
        self.param['di'] = ''
        self.param['ho'] = ''
        self.param['pa'] = ''
        self.param['c'] = ''
        self.param['sc'] = ''
        self.param['me'] = ''
        self.param['ra'] = ''
        self.param['dc'] = ''
        self.param['li'] = 'PDNS'

        if self.query_pos != -1:
            for p in self.line[1:self.query_pos]:
                c = p.find(':')
                if c >= 0: self.param[p[0:c]] = p[c + 2:]

        qtype = self.trim_code(self.param.pop('qtype', ''))

        if qtype == 'A':
            self.param['ho'] = self.param.pop('qname', '')[:-1]
            if self.response_pos != -1:
                self.match_response(self.line[self.response_pos + 2])
                if self.ans_cnt > 0:
                    for x in range(self.ans_cnt):
                        e = self.line[self.answer_pos + x + 1]
                        c = e.find('IN A ')
                        if c != -1: 
                            self.ips.append(e[c + 5:])
                        else:
                            c = e.find('IN CNAME ')
                            if c != -1:
                                self.param['pa'] = "/CNAME/" + e[c + 9:][:-1]
                    # size of IPs may still be zero because of CNAME
                    if len(self.ips) > 0:
                        self.param['di'] = self.ips.pop(0)
                        if len(self.ips) > 0: self.param['pa'] = "/IP/" + ','.join(self.ips)
        elif qtype == 'PTR': 
            m = re.search('^(\d+\.\d+\.\d+\.\d+)', self.param.pop('qname'))
            if m:
                self.param['di'] = m.group(1)
                self.match_response(self.line[self.response_pos + 2])
                if self.ans_cnt > 0:
                    for x in range(self.ans_cnt):
                        m = re.search('PTR\s(.*)$', self.line[self.answer_pos + x + 1])
                        if m: self.param['ho'] = m.group(1).strip()[:-1]
        elif qtype == 'AAAA':
            self.param['ho'] = self.param.pop('qname', '')[:-1]
        elif qtype == 'TXT':
            self.param['ho'] = self.param.pop('qname', '')[:-1]
        elif qtype == 'SRV':
            self.param['ho'] = self.param.pop('qname', '')[:-1]
        elif qtype == 'SOA':
            self.param['ho'] = self.param.pop('qname', '')[:-1]
        elif qtype == '':
            return

        self.param['i'] = self.param.pop('query_ip', '')
        self.param['d'] = self.param.pop('response_ip', '')
        self.param['s'] = self.trim_code(self.param.pop('rcode', ''))
        self.param['sch'] = self.trim_code(self.param.pop('proto', ''))
        self.param['g'] = self.param.pop('type', '')
        self.param['po'] = self.param.pop('response_port', '')
        self.param['cp'] = qtype
        self.param.pop('qclass', None)
        self.param.pop('id', None)
        self.param.pop('delay', None)
        self.param.pop('udp_checksum', None)
        self.param.pop('query_port', None)
        self.param.pop('timeout', None)

        for key in self.param.keys(): 
            print '%s=%s\t' % (key, self.param[key]), 
        print

sample = 1

def usage():  
    print "Usage: %s [-s] [--sample] arg" % sys.argv[0]

if __name__ == '__main__':
    try:  
        opts, args = getopt.getopt(sys.argv[1:], "s:", ["sample="])  
        for o, a in opts: 
            if o in ("-s", "--sample"):
                sample = int(a)
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    count = 0
    skip_query = False
    r = PDNS_Record()
    for line in sys.stdin:
        try:
            line = line.strip()
            if len(line) == 0:
                continue
            if (count == 0 or r.line[-1] == '---') and line[0] == '[':
                if count > 0:
                    if count % sample == 0: r.output()
                    r.reset()
                count = count + 1
                skip_query = False
            elif line[0:7] == 'query: ':
                r.query_pos = len(r.line)
                r.line.append(line)
                skip_query = True
            elif line[0:10] == 'response: ':
                if line[10:] == '<PARSE ERROR>': 
                    line = '---'
                else:
                    r.response_pos = len(r.line)
                skip_query = False
            elif line == ';; ANSWER SECTION:':
                r.answer_pos = len(r.line)
            if skip_query != True or line == '---':
                r.line.append(line)
        except:
            err = traceback.format_exc()
            print >> sys.stderr, err, "Line:", r.line[0]
            r.reset()
            r.line.append(line)
            count = count + 1
            skip_query = False

    if count % sample == 0: r.output()
