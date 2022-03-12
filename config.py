import os
import platform
import sys

NAME = "fresh-reader"
VERSION = "0.4.0"
HOME_DIR = os.path.expanduser("~")
USER_DATA_DIR = os.path.join(HOME_DIR, ".fresh-reader")
OUTPUT_FILE = os.path.join(USER_DATA_DIR, "fiction-book.html")

if getattr(sys, 'frozen', False):
	APP_PATH = os.path.dirname(sys.executable)
	if platform.system() == 'Linux':
		APP_DATA = os.path.join("/usr", "share", NAME, "data")
	else:
		APP_DATA = os.path.join(APP_PATH, "data")
else:
	APP_PATH = os.path.dirname(__file__)
	APP_DATA = os.path.join(APP_PATH, "data")

DEMO_FILE = os.path.join(APP_DATA, "demo.fb2")

# path relative to APP_DATA
VIEWER_TEMPLATE_FILE = "viewer.html"
