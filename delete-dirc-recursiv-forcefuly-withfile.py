#!/usr/bin/python3

import shutil
def main():
	shutil.rmtree('wf5/t1/t2')
	# rmtree cmd delete either empty or non empty directory 
if __name__ == '__main__':
	main()

# Output:
# tree wf5/
# wf5/
# └── t1
#     └── t2
#         └── t3
#             └── t4
#                ├── file1.txt
#                └── file2.txt
# 4 directories, 2 files
# ./delete-dirc-recursiv-forcefuly-withfile.py 
# tree wf5/
# wf5/
# └── t1
# 1 directory, 0 files

