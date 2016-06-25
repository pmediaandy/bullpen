#!/usr/bin/env python

import argparse
import xlwt
import csv
import os

def is_number(text):
    d = [ '-', '+', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
    for c in text:
        if c not in d:
            return False
    return True

def write_xls(outname, sheets):
    book = xlwt.Workbook(encoding="utf-8")
    for sh_name in sorted(sheets):
        st = book.add_sheet(sh_name)
        for i in range(len(sheets[sh_name])):
            row = sheets[sh_name][i]
            for j in range(len(row)):
                cell = row[j]
                if is_number(cell):
                    st.write(i, j, float(cell))
                else:
                    st.write(i, j, cell)
    book.save(outname)

def read_csv(fname, has_header = True):
    all = []
    with open(fname, 'r') as fin:
        cnt = 0
        reader = csv.reader(fin, delimiter=',', quotechar='"')
        for row in reader:
            cnt += 1
            if has_header and cnt == 1:
                all.append(row)
                continue
            all.append(row)
    return all

def exec_generate(args):
    if(len(args.csv) < 1):
        print('not input csv specified')
        return
    if(args.xls is None):
        print('not output xls specified')
        return
    out_xls = {}
    for c in args.csv:
        if ':' in c:
            sh_name = c.split(':')[0]
            csv_name = c.split(':')[1]
        else:
            sh_name = os.path.splitext(os.path.basename(c))[0]
            csv_name = c
        out_xls[sh_name] = read_csv(csv_name)

    write_xls(args.xls, out_xls)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Generate xls file with multiple tabs from input csv files')
    parser.add_argument('--csv', '-c', dest = 'csv', nargs = '+', action = 'store', default = [], help = 'The input csv files to read, CSV := [SHEET_NAME:]FILE_NAME')
    parser.add_argument('--xls', '-x', dest = 'xls', nargs = '?', action = 'store', default = None, help = 'The destination xls file to write')

    args = parser.parse_args()

    exec_generate(args)
