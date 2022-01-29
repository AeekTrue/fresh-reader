from xml.etree import ElementTree as ET
from fb2_tools import FictionBook


def gen_html_page(book: FictionBook):
	content = book.gen_html()
	text = ET.tostring(content, method="html").decode("utf-8")
	return text


def render_file(path):
	book = FictionBook(path)
	fiction_book = gen_html_page(book)
	return "{% extends 'reader.html' %}{% block fiction_book %}" + fiction_book + "{% endblock %}"