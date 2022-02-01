import webbrowser
import jinja2
import config
import fb2_tools

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(config.WORK_DIR),
	autoescape=jinja2.select_autoescape([])
)


class Viewer:
	def __init__(self):
		self.viewer_page_file = config.VIEWER_PAGE_FILE

	def open_fiction_book(self, path):
		book = fb2_tools.FictionBook(path)
		html = self.render_view_page(book)
		self.save_view_page(html)
		webbrowser.open(self.viewer_page_file)

	def render_view_page(self, book: fb2_tools.FictionBook) -> str:
		template = env.get_template(config.VIEWER_TEMPLATE_FILE)
		html = template.render(title="lol", fiction_book="<h1>kek</h1>")
		return html

	def save_view_page(self, text: str):
		with open(config.VIEWER_PAGE_FILE, "w") as f:
			f.write(text)


viewer = Viewer()
