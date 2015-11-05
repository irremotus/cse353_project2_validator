#!/bin/python3

# usage: ./validator.py <number of nodes>

import sys

if len(sys.argv) != 2:
	print("Usage: ./validator.py <number of nodes>")
	quit()

lists = []

for i in range(1, int(sys.argv[1]) + 1):
	lists.append([])

for i in range(1, int(sys.argv[1]) + 1):
	fname = "node" + str(i) + ".txt"
	f = open(fname, "r")
	for line in f.readlines():
		parts = line.split(":", 1)
		l = parts[1]
		if l[-1] == "\n":
			l = l[:-1]
		lists[int(parts[0])-1].append(str(i) + ":" + l)
	f.close()

errorCount = 0

for i in range(1, int(sys.argv[1]) + 1):
	fname = "node" + str(i) + "output.txt"
	f = open(fname, "r")
	for line in f.readlines():
		l = line
		if l[-1] == "\n":
			l = l[:-1]
		try:
			lists[i-1].remove(l)
		except ValueError:
			print("Line in list", i, ":", l, "is unexpected")
			errorCount = errorCount + 1
	if len(lists[i-1]) > 0:
		print("Missing lines in list", i)
		for line in lists[i-1]:
			print("\t", line)
			errorCount = errorCount + 1

if errorCount == 0:
	print("No errors! YAY!!!!!")
