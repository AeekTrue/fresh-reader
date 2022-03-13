import sys
import webbrowser
import jinja2

import config
import fb2_tools
import zipfile
from loguru import logger

logger.add(sys.stderr, format="[{time:HH:mm:ss.SSS}] <lvl>{level}</> - {message}", filter="name", level="INFO")

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(config.APP_DATA),
	autoescape=jinja2.select_autoescape([])
)


def open_zipped_fb2(file):
	zip_file = zipfile.ZipFile(file)
	for f in zip_file.filelist:
		if f.filename.endswith(".fb2"):
			logger.debug("found fb2 file:", f.filename)
			return zip_file.open(f.filename)


class Viewer:
	def __init__(self):
		self.viewer_page_file = config.OUTPUT_FILE
	
	def open_fiction_book(self, path):
		logger.debug(f"Opening file: {path}")
		if zipfile.is_zipfile(path):
			logger.debug("It's zipfile")
			fb2_file = open_zipped_fb2(path)
		else:
			fb2_file = open(path)
		
		book = fb2_tools.FictionBook(fb2_file)
		fb2_file.close()
		
		html = self.render_view_page(book)
		self.save_view_page(html)
		webbrowser.open(self.viewer_page_file)
	
	def render_view_page(self, book: fb2_tools.FictionBook) -> str:
		template = env.get_template(config.VIEWER_TEMPLATE_FILE)
		reader_info = f"HTML file generated by {config.NAME} v{config.VERSION}"
		html = template.render(
			book=book,
			title=book.title,
			title_info=book.html(fb2_tools.xpath.TITLE_INFO),
			fiction_book=book.html(fb2_tools.xpath.BODY),
			notes=book.html(fb2_tools.xpath.NOTES),
			document_info=book.html(fb2_tools.xpath.DOCUMENT_INFO),
			publish_info=book.html(fb2_tools.xpath.PUBLISH_INFO),
			reader_info=reader_info
		)
		return html
	
	def save_view_page(self, text: str):
		with open(config.OUTPUT_FILE, "wb") as f:
			f.write(text.encode("utf-8"))


viewer = Viewer()
