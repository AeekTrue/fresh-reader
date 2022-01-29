import os
from xml.etree import ElementTree as ET
from .tags import *
from .attribs import *

html_templates = {
	DESCRIPTION: ("div", {"id": "description", "class": "body"}),
	TITLE_INFO: ("div", {"id": "title-info", "class": "body"}),
	AUTHOR: ("h1", {"class": "author"}),
	FIRST_NAME: ("div", {"class": "first-name"}),
	MIDDLE_NAME: ("div", {"class": "middle-name"}),
	LAST_NAME: ("div", {"class": "last-name"}),
	ID: ("div", {"class": "fb2-id"}),
	COVER_PAGE: ("div", {"class": "cover-page"}),
	ANNOTATION: ("div", {"class": "annotation"}),
	BOOK_TITLE: ("h1", {"class": "book-title"}),
	GENRE: ("div", {"class": "genre"}),
	DATE: ("div", {"class": "date"}),
	DOCUMENT_INFO: ("div", {"id": "document-info", "class": "section"}),
	LANG: ("div", {"class": "lang"}),
	BODY: ("div", {"class": "body"}),
	SECTION: ("div", {"class": "section"}),
	TITLE: ("h1", {"class": "title"}),
	SUBTITLE: ("h3", {"class": "subtitle"}),
	PARAGRAPH: ("p",),
	EMPTY_LINE: ("br",),
	STRONG: ("b",),
	EMPHASIS: ("em",),
	SUB: ("sub",),
	SUP: ("sup",),
	EPIGRAPH: ("div", {"class": "epigraph"}),
	CITE: ("div", {"class": "cite"}),
	POEM: ("div", {"class": "poem"}),
	STANZA: ("p", {"class": "stanza"}),
	V: ("div", {"class": "v"}),
	TEXT_AUTHOR: ("div", {"class": "text-author"}),
	LINK: ("a",),
	IMAGE: ("img",),
	CUSTOM_UNKNOWN_TAG: ("div", {"unknown-tag": ""}),
}


class FictionBook:
	def __init__(self, path):
		self._tree = ET.parse(path)
		self.raw = self._tree.getroot()
		self.description = self.raw.find(f"./{DESCRIPTION}")
		self.title_info = self.description.find(f"./{TITLE_INFO}")
		self.bodies = self.raw.findall(f"./{BODY}")

	def gen_html(self):
		html = ET.Element("div", {"id": "fiction-book"})
		html.append(self.make_element(self.title_info))
		for e in self.bodies:
			if e is not None:
				html.append(self.make_element(e))
		return html

	def make_element(self, element: ET.Element) -> ET.Element:
		if element is None:
			return ET.Element("div", {"class": "empty"})

		if element.tag in html_templates.keys():
			html = ET.Element(*html_templates.get(element.tag))
		else:
			print(f"Unknown tag: {element.tag}")
			html = ET.Element(*html_templates.get(CUSTOM_UNKNOWN_TAG))
			html.set("class", f"{element.tag} unknown-tag")

		if element.get("id") is not None:
			html.attrib["id"] = element.get("id")

		if element.tag == LINK:
			link = element.get(HREF)
			html.set("href", link)
			if link[0] == '#':
				html.set("class", "local-link")
		elif element.tag == IMAGE:
			binary_id = element.get(HREF)[1:]
			content_type = element.get("content-type")
			binary = self.raw.find(f"./{BINARY}[@id='{binary_id}']").text
			html.set("src", f"data:{content_type};base64, {binary}")
			html.set("alt", f"<PICTURE {binary_id}>")

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
