import sys

from config import *
from viewer import viewer


def setup():
	if not os.path.exists(USER_DATA_DIR):
		os.mkdir(USER_DATA_DIR)


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
