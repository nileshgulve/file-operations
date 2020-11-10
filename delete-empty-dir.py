#!/usr/bin/python3

import shutil,os

def main():
	emtpath = '/root/python/file-operation/wf2/empty_dir1'
	nonemtpath = '/root/python/file-operation/wf2/not_empty_dir2'

	print(os.path.exists(emtpath))
	print(os.path.exists(nonemtpath))
	print(os.path.isdir(emtpath))
	print(os.path.isdir(nonemtpath))
	os.rmdir(emtpath)
#	os.rmdir('nonemtpath')
# If you are deleting non empty directory then you get error - directory is not empty

if __name__ == '__main__':
	main()

# Output:
# root@deb1:~/python/file-operation# tree wf1/
# wf2/
# ├── empty_dir1
# └── not_empty_dir2
#     └── file1.txt
# ./delete-empty-dir.py 
# True
# True
# True
# True
# tree wf2/
# wf2/
# └── not_empty_dir2
#     └── file1.txt


