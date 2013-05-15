#!/usr/bin/env python
import sys
import json
import urllib

def extractWithoutTA(fields, data):
	column = sys.argv[2]
	for k in data[column].keys():
		print "%s,%s,%s" % (','.join(fields), k.encode('utf-8'), data[column][k])

def extractWithTA(fields, data):
	print "%s,%s" % (','.join(fields), data['TA'])

def main():
	f = open(sys.argv[1], 'r')
	while True:
		line = f.readline().strip()
		if line == '':
			break
		fields = line.split(',')
		data = json.loads(urllib.unquote(fields[-1]))
		if 'age' in data.keys():
			extractWithoutTA(fields[0:-2], data)
		else:
			extractWithTA(fields[0:-2], data)

if __name__ == '__main__':
	main()

