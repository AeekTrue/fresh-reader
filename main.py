import tools
from fb2_tools import FictionBook
from config import *

import sys
import os
import shutil
import webbrowser
from app import app


def setup():
	if not os.path.exists(WORK_DIR) and IS_BINARY_FILE:
		shutil.copytree(FACTORY_DIR, WORK_DIR)


def main():
	if len(sys.argv) < 2:
		webbrowser.open(f"http://127.0.0.1:5000/")
	else:
		path = sys.argv[-1]
		path = os.path.abspath(path)
		webbrowser.open(f"http://127.0.0.1:5000/read?path={path}")
	app.run()


if __name__ == '__main__':
	setup()
	main()
