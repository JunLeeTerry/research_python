#!/usr/bin/env python

import urllib
import os
import re
page = urllib.urlopen("http://www.pyth\
onchallenge.com/pc/def/equality.html").read()

#print page
p = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
s =  p.findall (page)
p2 = re.compile('[A-Z][a-z][A-Z]')
a = []
for i in s:
   a += p2.findall(i)
stringa = ''.join(a)
print stringa

p3 = re.compile('[A-Z]+')
answer = p3.sub("",stringa)
print("answer:" + answer)

'''
p2 = re.compile('[a-z]')
answerlist = ""
for i in s:
    for item in p2.findall(i):
        answerlist += item
print answerlist
'''
        


