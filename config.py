import os
import sys

NAME = "fresh-reader"
VERSION = "0.3.0"
HOME_DIR = os.path.expanduser("~")
USER_DATA_DIR = os.path.join(HOME_DIR, ".fresh-reader")
OUTPUT_FILE = os.path.join(USER_DATA_DIR, "fiction-book.html")

if getattr(sys, 'frozen', False):
	APP_PATH = os.path.dirname(sys.executable)
else:
	APP_PATH = os.path.dirname(__file__)

WORK_DIR = os.path.join(APP_PATH, "data")
DEMO_FILE = os.path.join(WORK_DIR, "demo.fb2")

# path relative to WORK_DIR
VIEWER_TEMPLATE_FILE = "viewer.html"
