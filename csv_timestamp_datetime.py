#!/usr/bin/python
import time
import struct
import csv
import sys

#@outputSchema("ip:chararray")
def long2ip (l):
    return '%d.%d.%d.%d' % (l>>24 & 255, l>>16 & 255, l>>8 & 255, l & 255) 

#@outputSchema("timestamp:chararray")
def l2t (lint):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(lint))


if __name__ == '__main__':
    newfile = open(sys.argv[2],"w")
    writer = csv.writer(newfile)
    oldfile = open(sys.argv[1],"r")
    reader = csv.reader(oldfile)
    for row in reader:
        writer.writerow([row[0], long2ip(long(row[2])), l2t(long(row[1])), row[3], row[4]])
    newfile.close()
    oldfile.close()
