from . import tags

BODY = f"./{tags.BODY}"
NOTES = f"./{tags.BODY}[@name='notes']"
TITLE_INFO = f"./{tags.DESCRIPTION}/{tags.TITLE_INFO}"

DESCRIPTION = f"./{tags.DESCRIPTION}"
DOCUMENT_INFO = f"{DESCRIPTION}/{tags.DOCUMENT_INFO}"
PUBLISH_INFO = f"{DESCRIPTION}/{tags.PUBLISH_INFO}"
