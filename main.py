import shutil
import sys
import os
from config import *
from path import FACTORY_DIR, WORK_DIR, DEMO_FILE
from viewer import viewer


def setup():
	if not os.path.exists(WORK_DIR) and IS_BINARY_FILE:
		shutil.copytree(FACTORY_DIR, WORK_DIR)


def main():
	if len(sys.argv) < 2:
		viewer.open_fiction_book(DEMO_FILE)
	elif sys.argv[1] in ('-v', '--version'):
		print(VERSION)
	else:
		path = sys.argv[-1]
		viewer.open_fiction_book(path)


if __name__ == '__main__':
	setup()
	main()
