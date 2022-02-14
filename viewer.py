import webbrowser
import jinja2

import config
import fb2_tools
from xml.etree import ElementTree as ET

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(config.APP_DATA),
	autoescape=jinja2.select_autoescape([])
)


def element2str(element: ET.Element):
	return ET.tostring(element, method="html").decode("utf-8")


class Viewer:
	def __init__(self):
		self.viewer_page_file = config.OUTPUT_FILE
	
	def open_fiction_book(self, path):
		book = fb2_tools.FictionBook(path)
		html = self.render_view_page(book)
		self.save_view_page(html)
		webbrowser.open(self.viewer_page_file)
	
	def render_view_page(self, book: fb2_tools.FictionBook) -> str:
		template = env.get_template(config.VIEWER_TEMPLATE_FILE)
		html = template.render(
			book=book,
			title=book.title,
			title_info=book.html(fb2_tools.xpath.TITLE_INFO),
			fiction_book=book.html(fb2_tools.xpath.BODY),
			notes=book.html(fb2_tools.xpath.NOTES),
			document_info=book.html(fb2_tools.xpath.DOCUMENT_INFO),
			publish_info=book.html(fb2_tools.xpath.PUBLISH_INFO)
		)
		return html
	
	def save_view_page(self, text: str):
		with open(config.OUTPUT_FILE, "w") as f:
			f.write(text)


viewer = Viewer()
