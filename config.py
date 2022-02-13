import os

NAME = "fresh-reader"
VERSION = "0.2.0"

HOME_DIR = os.path.expanduser("~")
USER_DATA_DIR = os.path.join(HOME_DIR, ".fresh-reader")

OUTPUT_FILE = os.path.join(USER_DATA_DIR, "fiction-book.html")
WORK_DIR = "data"
DEMO_FILE = os.path.join(WORK_DIR, "demo.fb2")

# path relative to WORK_DIR
VIEWER_TEMPLATE_FILE = "viewer.html"
