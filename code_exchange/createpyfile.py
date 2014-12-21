#!/usr/bin/env python

'''
	author:terry
	first the command will ask you to enter the file type.
	if you enter 'm',the script just only writes the Shebang.
	if you enter 'n',the script writes main method.Whether 
	you write '.py' or not,the script will help you write
	it. 

'''
import os 
import re

def main():
	pi_type = raw_input("please enter your file type('m'ain or 'n'ormal)")
	if (pi_type == 'n' or pi_type == 'm'):
		name = raw_input("please enter your file name:")
		p = re.compile('.py$')
		if p.search(name):
			pifile = file(name,"a+")
		else:
			pifile = file(name+".py","a+")
		pifile.write('#!/usr/bin/env python\n')
		if(pi_type == 'n'):
			pifile.write('def main():\n\
    pass\n\n\
if (__name__=="__main__"):\n\
    main()\n')
	else:
		print "type error"
		main()

if(__name__ == "__main__"):
	main()
