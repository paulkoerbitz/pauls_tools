#!/usr/bin/env python
import csv, argparse

parser = argparse.ArgumentParser(description='Show entries from first csv file which are not in second file selected by a column')
parser.add_argument('col1', type=int, help='Column of first file')
parser.add_argument('col2', type=int, help='Column of second file')
parser.add_argument('file1', type=str, help='first file')
parser.add_argument('file2', type=str, help='second file')
parser.add_argument('mode', choices=['missingIn1','missingIn2','foundIn1','foundIn2'],
                    default='missingIn1')

args = parser.parse_args()

i1 = args.col1-1
i2 = args.col2-1
data1 = sorted([l for l in csv.reader(open(args.file1, 'r'))], key=lambda x: x[i1])
data2 = sorted([l for l in csv.reader(open(args.file2, 'r'))], key=lambda x: x[i2])

cursor2=0
only1, only2, both = [], [], []

for cursor1,l in enumerate(data1):
    while l[i1] > data2[cursor2][i2]:
        only2.append(cursor2)
        cursor2 = cursor2 + 1
    if l[i1] == data2[cursor2][i2]:
        both.append((cursor1,cursor2))
    else:
        only1.append(cursor1)

if args.mode == "missingIn2":
    print("\n".join((",".join(data1[i]) for i in only1)))
elif args.mode == "missingIn1":
    print("\n".join((",".join(data2[i]) for i in only2)))
elif args.mode == "foundIn1":
    print("\n".join((",".join(data1[i]) for (i,_) in both)))
elif args.mode == "foundIn2":
    print("\n".join((",".join(data2[j]) for (_,j) in both)))
