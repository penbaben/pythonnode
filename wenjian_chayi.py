#!/usr/bin/python
#coding: utf-8

import difflib
import sys
import codecs
try:
	textfile1 = sys.argv[1]
	textfile2 = sys.argv[2]
except Exception as e:
	print("Error:" + str(e))
	print("Usage:  filename1 filename2")
	sys.exit()

def readfile(filename):
	try:
		fileHandle = open(filename, 'r')  #python3默认读取编码
		text = fileHandle.read().splitlines()
		fileHandle.close()
		return text
		
	except IOError as error:
		print('read file Error:' + str(error))
		sys.exit()
		
if textfile1 == '' or textfile2 == '':
	print("Usage:  filename1 filename2")
	sys.exit()
	
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
	