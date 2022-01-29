import os
import sys

VERSION = "0.0.0"
IS_BINARY_FILE = False


if IS_BINARY_FILE:
	HOME_DIR = os.environ.get("HOME")
	FACTORY_DIR = os.path.join(sys._MEIPASS, "data")
	WORK_DIR = os.path.join(HOME_DIR, ".fresh-reader")
else:
	FACTORY_DIR = "data"
	WORK_DIR = "data"

TEMPLATE_DIR = os.path.join(WORK_DIR, "templates")
STATIC_DIR = os.path.join(WORK_DIR, "static")

DEMO_FILE = os.path.join(WORK_DIR, "demo.fb2")
OUTPUT_FILE = os.path.join(TEMPLATE_DIR, "fiction_book.html")
