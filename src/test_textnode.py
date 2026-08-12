import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none(self):
        node=TextNode("",TextType.PLAIN)
        self.assertEqual(node.text,"")
        self.assertEqual(node.text_type,TextType.PLAIN)
        self.assertEqual(node.url,None)

    def test_different(self):
        node=TextNode("Text ABC", TextType.PLAIN)
        node2=TextNode("Text XYZ", TextType.PLAIN)
        self.assertNotEqual(node,node2)

    def test_wrong_texttype(self):
        node=TextNode("test", None, "url")
        self.assertNotEqual(node.text_type,TextType.ITALIC)

    def test_text(self):
        node=TextNode("Hello World!",TextType.PLAIN)
        html_node=TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag,None)
        self.assertEqual(html_node.value,"Hello World!")

    def test_bold(self):
        node=TextNode("Hello World!",TextType.BOLD)
        html_node=TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(),'<b>Hello World!</b>')

    def test_img(self):
        node=TextNode("a picture of me",TextType.IMAGE,"lordhonk.de/img1.jpg")
        html_node=TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(),'<img src="lordhonk.de/img1.jpg" alt="a picture of me"></img>')


if __name__ == "__main__":
    unittest.main()
