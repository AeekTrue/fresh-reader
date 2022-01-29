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

TEMPLATE_FILE = os.path.join(WORK_DIR, "template.html")
DEMO_FILE = os.path.join(WORK_DIR, "demo.html")
READER_STYLE_FILE = os.path.join(WORK_DIR, "reader.css")
FB_STYLE_FILE = os.path.join(WORK_DIR, "fiction-book.css")
SCRIPT_FILE = os.path.join(WORK_DIR, "script.js")
OUTPUT_FILE = os.path.join(WORK_DIR, "fiction-book.html")
