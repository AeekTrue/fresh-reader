from fb2_tools import FictionBook
from config import *

import xml.etree.ElementTree as ET
import sys
import os
import shutil
import webbrowser


def setup():
	if not os.path.exists(WORK_DIR) and IS_BINARY_FILE:
		shutil.copytree(FACTORY_DIR, WORK_DIR)


def gen_html_page(book: FictionBook):
	html_tree = ET.parse(TEMPLATE_FILE)
	html = html_tree.getroot()
	with open(SCRIPT_FILE) as f:
		html.find("./body/script[@id='js']").text = f.read()

	with open(FB_STYLE_FILE) as f:
		html.find("./head/style[@id='fiction-book-style']").text = f.read()

	with open(READER_STYLE_FILE) as f:
		html.find("./head/style[@id='reader-style']").text = f.read()

	content = book.gen_html()
	html.find("./body").insert(0, content)
	return ET.tostring(html, method="html").decode("utf-8")


def main():
	if len(sys.argv) < 2:
		path = DEMO_FILE
	else:
		path = sys.argv[-1]

	with open(OUTPUT_FILE, "w") as file:
		book = FictionBook(path)
		html_page = gen_html_page(book)
		file.write(html_page)

	webbrowser.open(OUTPUT_FILE)


if __name__ == '__main__':
	setup()
	main()
