import os
import sys

VERSION = "0.0.0"
IS_BINARY_FILE = False


if IS_BINARY_FILE:
	FACTORY_DIR = os.path.join(sys._MEIPASS, "data")
else:
	FACTORY_DIR = "data"

HOME_DIR = os.environ.get("HOME")
WORK_DIR = os.path.join(HOME_DIR, ".fresh-reader")

TEMPLATE_FILE = os.path.join(WORK_DIR, "template.html")
DEMO_FILE = os.path.join(WORK_DIR, "demo.html")
STYLE_FILE = os.path.join(WORK_DIR, "style.css")
SCRIPT_FILE = os.path.join(WORK_DIR, "script.js")
OUTPUT_FILE = os.path.join(WORK_DIR, "output.html")
