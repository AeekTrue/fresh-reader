import os
from xml.etree import ElementTree as ET
from .tags import *
from .attribs import *


class FictionBook:
	def __init__(self, path):
		self._tree = ET.parse(path)
		self.raw = self._tree.getroot()
		self.description = Description(self.raw.find(f"./{DESCRIPTION}"))

	def gen_html(self):
		html = ET.Element("div", {"id": "fiction-book"})

		body = self.raw.find(f"./{BODY}")
		notes = self.raw.find(f"./{BODY}[@name='notes']")
		comments = self.raw.find(f"./{BODY}[@name='comments']")
		for e in (body, notes, comments):
			if e is not None:
				html.append(self.make_element(e))

		return html

	def make_element(self, element: ET.Element) -> ET.Element:
		html: ET.Element

		html_templates = {
			BODY: ET.Element("div", {"class": "body"}),
			SECTION: ET.Element("div", {"class": "section"}),
			TITLE: ET.Element("h1", {"class": "title"}),
			SUBTITLE: ET.Element("h3", {"class": "subtitle"}),
			PARAGRAPH: ET.Element("p"),
			EMPTY_LINE: ET.Element("br"),
			STRONG: ET.Element("b"),
			EMPHASIS: ET.Element("em"),
			SUB: ET.Element("sub"),
			SUP: ET.Element("sup"),
			EPIGRAPH: ET.Element("div", {"class": "epigraph"}),
			CITE: ET.Element("div", {"class": "cite"}),
			POEM: ET.Element("div", {"class": "poem"}),
			STANZA: ET.Element("p", {"class": "stanza"}),
			V: ET.Element("div", {"class": "v"}),
			TEXT_AUTHOR: ET.Element("div", {"class": "text-author"}),
			LINK: ET.Element("a"),
			IMAGE: ET.Element("img"),
		}
		html = html_templates.get(element.tag)
		if html is None:
			print(f"Unknown tag: {element.tag}")
			html = ET.Element("div", {"class": f"unknown-tag {element.tag}"})

		html.attrib.update(element.attrib)

		if element.tag == LINK:
			link = element.get(HREF)
			html.set("href", link)
			html.set("onclick", f" y = saveScrollPos()")
		elif element.tag == IMAGE:
			binary_id = element.get(HREF)[1:]
			binary = self.raw.find(f"./{BINARY}[@id='{binary_id}']").text
			html.set("src", f"data:image/jpeg;base64, {binary}")
			html.set("alt", "<PICTURE>")

		html.text = element.text
		html.tail = element.tail
		for child in element:
			html.append(self.make_element(child))
		return html


class Tag:
	def __init__(self, fb2_element: ET.Element):
		self.raw = fb2_element


class Author(Tag):
	def __init__(self, fb2_element: ET.Element):
		super(Author, self).__init__(fb2_element)
		ft_name_elem = fb2_element.find(f"./{FIRST_NAME}")
		lt_name_elem = fb2_element.find(f"./{LAST_NAME}")
		if ft_name_elem is not None:
			self.first_name = ft_name_elem.text
		else:
			self.first_name = ""

		if lt_name_elem is not None:
			self.last_name = lt_name_elem.text
		else:
			self.last_name = ""

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Description(Tag):
	def __init__(self, fb2_element: ET.Element):
		super(Description, self).__init__(fb2_element)
		self._raw = fb2_element
		self.title_info = ""
		self.book_title = fb2_element.find(f"./{TITLE_INFO}/{BOOK_TITLE}").text
		self.author = Author(fb2_element.find(f"./{TITLE_INFO}/{AUTHOR}"))