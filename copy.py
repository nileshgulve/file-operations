#!/usr/bin/python3

import shutil,os

def main():
	srcpath = '/root/python/file-operation/wf1/dir1/file1'
	dstpath = '/root/python/file-operation/wf1/dir2/file2'

	os.path.exists(srcpath)
	os.path.exists(dstpath)
	os.path.dirname(dstpath)
	shutil.copy(srcpath,dstpath)
	os.path.exists(dstpath)
if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/python/file-operation# tree wf1/
# wf1/
# ├── dir1
# │   └── file1
# └── dir2
# 2 directories, 1 file
# ./copy.py 
# tree wf1/
# wf1/
# ├── dir1
# │   └── file1
# └── dir2
#     └── file2
# 2 directories, 2 files
