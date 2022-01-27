ns = '{http://www.gribuser.ru/xml/fictionbook/2.0}'

TITLE = ns + 'title'
SUBTITLE = ns + 'subtitle'
PARAGRAPH = ns + 'p'
EMPTY_LINE = ns + 'empty-line'
STRONG = ns + 'strong'
EMPHASIS = ns + 'emphasis'
SUB = ns + 'sub'
SUP = ns + 'sup'

EPIGRAPH = ns + 'epigraph'
CITE = ns + 'cite'
POEM = ns + 'poem'
STANZA = ns + 'stanza'
V = ns + 'v'
TEXT_AUTHOR = ns + 'text-author'
LINK = ns + 'a'
IMAGE = ns + 'image'

BODY = ns + 'body'
BINARY = ns + 'binary'
SECTION = ns + 'section'

DESCRIPTION = ns + 'description'
TITLE_INFO = ns + 'title-info'
BOOK_TITLE = ns + 'book-title'

AUTHOR = ns + 'author'
FIRST_NAME = ns + 'first-name'
LAST_NAME = ns + 'last-name'
# class Tag:
# 	def __init__(self, section_name: str, name_space=ns):
# 		self.tag_name = section_name.replace("_", "-", -1).lower()
# 		self.value = f"{name_space}{self.tag_name}"
#
# 	def __str__(self):
# 		return self.value