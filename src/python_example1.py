#!/usr/bin/env python
import sys
num = sys.argv[1]
total = 0

for i in range(1,int(num)+1):
	total = total + i

print("The sum from 1 to " + str(num) + " is " + str(total) )