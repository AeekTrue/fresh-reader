import shutil
import sys

import config
from config import *
from viewer import viewer


def setup():
	if not os.path.exists(WORK_DIR) and IS_BINARY_FILE:
		shutil.copytree(FACTORY_DIR, WORK_DIR)


def main():
	path = DEMO_FILE
	if len(sys.argv) < 2:
		pass
	elif sys.argv[1] in ('-v', '--version'):
		print(config.VERSION)
	else:
		path = sys.argv[-1]

	viewer.open_fiction_book(path)


if __name__ == '__main__':
	setup()
	main()
