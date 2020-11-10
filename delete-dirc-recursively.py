#!/usr/bin/python3

# You able to delete directory recursively, only when this are empty.
import os
def main():
	print(os.path.exists('/root/python/file-operation/wf4/one/two/three'))
	print(os.path.isdir('/root/python/file-operation/wf4/one/two/three'))
#	print(os.removedirs('/root/python/file-operation/wf4/one/two/three'))
# you got an error 'coz' the directory is not empty.
	os.removedirs('/root/python/file-operation/wf4/one/two/three')

if __name__ == '__main__':
	main()

# Output:
# tree wf4/
# wf4/
# └── one
#     ├── one.txt
#     └── two
#         └── three
# 3 directories, 1 file
# ./delete-dirc-recursively.py 
# True
# True
# tree wf4/
# wf4/
# └── one
#     └── one.txt
# 1 directory, 1 file

