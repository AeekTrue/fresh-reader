from . import tags

BODY = f"./{tags.BODY}"
NOTES = f"./{tags.BODY}[@name='notes']"
BINARY = f"./{tags.BINARY}"
DESCRIPTION = f"./{tags.DESCRIPTION}"
TITLE_INFO = f"./{tags.DESCRIPTION}/{tags.TITLE_INFO}"
DOCUMENT_INFO = f"{DESCRIPTION}/{tags.DOCUMENT_INFO}"
PUBLISH_INFO = f"{DESCRIPTION}/{tags.PUBLISH_INFO}"
