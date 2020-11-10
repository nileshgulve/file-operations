#!/usr/bin/python3

import shutil,os

def main():
	filepath = '/root/python/file-operation/wf3/file.txt'

	print(os.path.exists(filepath))
	print(os.path.isfile(filepath))
	os.remove(filepath)
	print(os.path.exists(filepath))
if __name__ == '__main__':
	main()
# Output:
# tree wf3/
# wf3/
# └── file.txt
# 0 directories, 1 file
# ./delete-file.py 
# True
# True
# False
# tree wf3/
# wf3/
# 0 directories, 0 files

