import os
import sys
from config import IS_BINARY_FILE

if IS_BINARY_FILE:
	HOME_DIR = os.path.expanduser("~")
	FACTORY_DIR = os.path.join(sys._MEIPASS, "data")
	WORK_DIR = os.path.join(HOME_DIR, ".fresh-reader")

else:
	FACTORY_DIR = "data"
	WORK_DIR = "data"

VIEWER_PAGE_FILE = os.path.join(WORK_DIR, "fiction-book.html")
DEMO_FILE = os.path.join(WORK_DIR, "demo.fb2")

# path relative to WORK_DIR
VIEWER_TEMPLATE_FILE = "viewer.html"
