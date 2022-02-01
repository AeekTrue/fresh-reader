import shutil

from config import *
from viewer import viewer


def setup():
	if not os.path.exists(WORK_DIR) and IS_BINARY_FILE:
		shutil.copytree(FACTORY_DIR, WORK_DIR)


def main():
	if len(sys.argv) < 2:
		path = DEMO_FILE
	else:
		path = sys.argv[-1]

	viewer.open_fiction_book(path)


if __name__ == '__main__':
	setup()
	main()
