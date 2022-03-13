from xml.etree import ElementTree as ET
from .tags import *
from .attribs import *
from . import xpath

html_templates = {
	DESCRIPTION: ("div", {"id": "description", "class": "body"}),
	TITLE_INFO: ("div", {"id": "title-info", "class": "section"}),
	AUTHOR: ("h1", {"class": "author"}),
	FIRST_NAME: ("div", {"class": "first-name"}),
	MIDDLE_NAME: ("div", {"class": "middle-name"}),
	LAST_NAME: ("div", {"class": "last-name"}),
	NICKNAME: ("div", {"class": "nickname"}),
	ID: ("div", {"class": "fb2-id"}),
	COVER_PAGE: ("div", {"class": "cover-page"}),
	ANNOTATION: ("div", {"class": "annotation"}),
	BOOK_TITLE: ("h1", {"class": "book-title"}),
	GENRE: ("div", {"class": "genre"}),
	DATE: ("div", {"class": "date"}),
	DOCUMENT_INFO: ("div", {"id": "document-info"}),
	VERSION: ("div", {"class": "version"}),
	HISTORY: ("div", {"class": "history"}),
	PUBLISH_INFO: ("div", {"id": "publish_info", }),
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


def gen_id():
	id = 0
	while True:
		yield id
		id += 1


section_id_generator = gen_id()


class FictionBook:
	def __init__(self, file):
		tree = ET.parse(file)
		self.raw = tree.getroot()
		self.description = self.raw.find(xpath.DESCRIPTION)
		self.title_info = self.raw.find(xpath.TITLE_INFO)
		self.title = self.title_info.find(f"./{BOOK_TITLE}").text
		self.bodies = self.raw.findall(f"./{BODY}")
		self.contents = []
	
	def html(self, path: str):
		"""
		Generate HTML from given fb2 element.
		:param path: a string having element's XPath
		:return: HTML string
		"""
		element = self.raw.find(path)
		html = self.make_element(element)
		return ET.tostring(html, method="html").decode("utf-8")
	
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
		elif element.tag == SECTION:
			if element[0].tag == TITLE:
				if html.attrib.get("id") is None:
					section_id = f"section_{next(section_id_generator)}"
					html.attrib["id"] = section_id
					name = ET.tostring(element[0], method="html").decode("utf-8")
					self.contents.append((name, section_id))
		html.text = element.text
		html.tail = element.tail
		for child in element:
			html.append(self.make_element(child))
		return html

