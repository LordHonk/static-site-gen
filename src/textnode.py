from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode


class TextType(Enum):
    PLAIN="plain"
    BOLD="**bold**"
    ITALIC="_italic_"
    CODE="`code`"
    LINK="[anchor text](url)"
    IMAGE="![alt_text](url)"


class TextNode():
    
    def __init__(self,text:str,text_type:TextType,url:str=None):
        self.text=text
        self.text_type=text_type
        self.url=url

    def __eq__(self,other):
        return self.text==other.text and self.text_type==other.text_type and self.url==other.url

    def __repr__(self)->str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"

    def text_node_to_html_node(text_node:"TextNode")->LeafNode:
        match(text_node.text_type):
            case TextType.PLAIN:
                return LeafNode(None,text_node.text,None)
            case TextType.BOLD:
                return LeafNode("b",text_node.text,None)
            case TextType.ITALIC:
                return LeafNode("i",text_node.text,None)
            case TextType.CODE:
                return LeafNode("code",text_node.text,None)
            case TextType.LINK:
                return LeafNode("a",text_node.text,{"href":text_node.url})
            case TextType.IMAGE:
                return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
            case _:
                raise Exception("unhandled TextType encountered")
