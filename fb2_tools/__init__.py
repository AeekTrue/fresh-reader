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
	ID: ("div", {"class": "fb2-id"}),
	COVER_PAGE: ("div", {"class": "cover-page"}),
	ANNOTATION: ("div", {"class": "annotation"}),
	BOOK_TITLE: ("h1", {"class": "book-title"}),
	GENRE: ("div", {"class": "genre"}),
	DATE: ("div", {"class": "date"}),
	DOCUMENT_INFO: ("div", {"id": "document-info"}),
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
	BINARY: ("img",),
}


class FB2Element:
	def __init__(self, xml_element: ET.Element):
		if xml_element is not None:
			self.xml = xml_element
		else:
			self.xml = ET.Element("div", {"class": "not-found"})
			self.xml.text = ""
		self.attributes = dict()
		self.text = self.xml.text

	def make_html_attributes(self):
		if self.xml.get("id") is not None:
			self.attributes["id"] = self.xml.get("id")

	def make_html_element(self) -> ET.Element:
		if self.xml.tag in html_templates.keys():
			html = ET.Element(*html_templates.get(self.xml.tag))
		else:
			print(f"Unknown tag: {self.xml.tag}")
			html = ET.Element(*html_templates.get(CUSTOM_UNKNOWN_TAG))
			html.set("class", f"{self.xml.tag} unknown-tag")

		self.make_html_attributes()
		html.attrib.update(self.attributes)
		html.text = self.xml.text
		html.tail = self.xml.tail
		for child in self.xml:
			if child.tag == LINK:
				fb2_child = Link(child)
			elif child.tag == IMAGE:
				fb2_child = Image(child)
			elif child.tag == BINARY:
				fb2_child = Binary(child)
			else:
				fb2_child = FB2Element(child)
			html.append(fb2_child.make_html_element())

		return html

	def get_html_string(self) -> str:
		html = self.make_html_element()
		text = ET.tostring(html, method="html").decode("utf-8")
		return text

	def __str__(self):
		return self.get_html_string()


class FictionBook(FB2Element):
	def __init__(self, path):
		root = ET.parse(path).getroot()
		super(FictionBook, self).__init__(root)
		self.description = Description(self.xml.find(xpath.DESCRIPTION))
		self.body = FB2Element(self.xml.find(xpath.BODY))
		self.notes = FB2Element(self.xml.find(xpath.NOTES))
		self.binaries = [Binary(b) for b in self.xml.findall(xpath.BINARY)]

class Description(FB2Element):
	def __init__(self, xml_element: ET.Element):
		super(Description, self).__init__(xml_element)
		self.title_info = TitleInfo(self.xml.find(f"./{TITLE_INFO}"))
		self.document_info = DocumentInfo(self.xml.find(f"./{DOCUMENT_INFO}"))
		self.publish_info = PublishInfo(self.xml.find(f"./{PUBLISH_INFO}"))


class Link(FB2Element):
	def make_html_attributes(self):
		super(Link, self).make_html_attributes()
		link = self.xml.get(HREF)
		self.attributes["href"] = link
		if link[0] == '#':
			self.attributes["class"] = "local-link"


class Image(FB2Element):
	def make_html_attributes(self):
		super(Image, self).make_html_attributes()
		src = self.xml.get(HREF)
		self.attributes["src"] = src


class Binary(FB2Element):
	def make_html_attributes(self):
		super(Binary, self).make_html_attributes()
		content_type = self.xml.get("content-type")
		binary = self.xml.text
		self.attributes["src"] = f"data:{content_type};base64, {binary}"
		self.attributes["alt"] = f"<PICTURE>"


class CoverPage(FB2Element):
	pass


class Annotation(FB2Element):
	pass


class Date(FB2Element):
	pass


class TitleInfo(FB2Element):
	def __init__(self, xml_element: ET.Element):
		super(TitleInfo, self).__init__(xml_element)
		self.genres = [g.text for g in self.xml.findall(f"./{GENRE}")]
		self.authors = [Author(a) for a in self.xml.findall(f"./{AUTHOR}")]
		self.book_title = self.xml.find(f"./{BOOK_TITLE}").text
		self.annotation = Annotation(self.xml.find(f"./{ANNOTATION}"))
		self.keywords = ''
		self.date = Date(self.xml.find(f"./{DATE}"))
		self.cover_page = CoverPage(self.xml.find(f"./{COVER_PAGE}"))
		self.lang = FB2Element(self.xml.find(f"./{LANG}")).text
		self.src_lang = ''
		self.translators = []
		self.sequences = []


class DocumentInfo(FB2Element):
	def __init__(self, xml_element: ET.Element):
		super(DocumentInfo, self).__init__(xml_element)
		self.authors = [Author(a) for a in self.xml.findall(f"./{AUTHOR}")]


class PublishInfo(FB2Element):
	pass


class Author(FB2Element):
	def __init__(self, xml_element: ET.Element):
		super(Author, self).__init__(xml_element)
		self.first_name = FB2Element(self.xml.find(f"./{FIRST_NAME}")).text
		self.middle_name = FB2Element(self.xml.find(f"./{MIDDLE_NAME}")).text
		self.last_name = FB2Element(self.xml.find(f"./{LAST_NAME}")).text
		self.nickname = FB2Element(self.xml.find(f"./{NICKNAME}")).text
		self.home_pages = []
		self.emails = []
		self.id = ''

	def __str__(self):
		return f"{self.first_name} {self.middle_name} {self.last_name} {self.nickname}"
