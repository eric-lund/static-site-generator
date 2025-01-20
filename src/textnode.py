from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False # make sure `other` is an instance of TextNode first
        return(
            self.text == other.text and
            self.url == other.url and
            self.text_type == other.text_type

        )
    
    def __repr__(self):
        # keep the method readonly and not modify the TextNode object
        # make sure that self.url is not None for consistent formatting
        url = self.url if self.url is not None else ''
        return f"TextNode({self.text}, {self.text_type.value}, {url})"
        
