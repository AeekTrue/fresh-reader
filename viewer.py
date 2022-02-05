import webbrowser
import jinja2
import fb2_tools
from xml.etree import ElementTree as ET

import path

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(path.WORK_DIR),
	autoescape=jinja2.select_autoescape([])
)


def element2str(element: ET.Element):
	return ET.tostring(element, method="html").decode("utf-8")


class Viewer:
	def __init__(self):
		self.viewer_page_file = path.VIEWER_PAGE_FILE

	def open_fiction_book(self, path):
		book = fb2_tools.FictionBook(path)
		html = self.render_view_page(book)
		self.save_view_page(html)
		webbrowser.open(self.viewer_page_file)

	def render_view_page(self, book: fb2_tools.FictionBook) -> str:
		template = env.get_template(path.VIEWER_TEMPLATE_FILE)
		html = template.render(book=book)
		return html

	def save_view_page(self, text: str):
		with open(path.VIEWER_PAGE_FILE, "w") as f:
			f.write(text)


viewer = Viewer()
