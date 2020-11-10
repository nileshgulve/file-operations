#!/usr/bin/python3

import os,sys

def main():
	loc  = sys.argv[1]
	# os.F_OK - value return to pass, to test the existance of path
	ret = os.access(loc,os.F_OK)
	print("F_OK - return value %s" %ret)

	# os.R_OK - value return to pass, to test the Readability of path
	ret = os.access(loc,os.R_OK)
 	print("R_OK - return value %s" %ret)

	# os.W_OK - value return to pass, to test the Writability of path
        ret = os.access(loc,os.W_OK)
        print("W_OK - return value %s" %ret)

	# os.X_OK - value return to pass, to determine if path can be executed
        ret = os.access(loc,os.X_OK)
        print("X_OK - return value %s" %ret)

