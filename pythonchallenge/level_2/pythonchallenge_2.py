#!/usr/bin/env python

import urllib
import re
httpcontent = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

print httpcontent

content = httpcontent.split("--")

for i in content:
    #print i
    print len(i)

p=re.compile(r'[^a-zA-Z]+')
print p.sub(" ",content[3])
