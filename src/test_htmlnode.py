import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_empty(self):
        node=HTMLNode()
        self.assertEqual(node.tag,None)
        self.assertEqual(node.value,None)
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)

    def test_children(self):
        child=HTMLNode()
        parent=HTMLNode(None,None,[],None)
        parent.children.append(child)
        self.assertEqual(child,parent.children[0])

    def test_props(self):
        node=HTMLNode()
        node.props={"href":"localhost", "target":"_blank"}
        self.assertEqual(node.props_to_html(), ' href="localhost" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props_to_html(self):
        node = LeafNode("a","Click me!",{"href":"lordhonk.de"})
        self.assertEqual(node.to_html(), '<a href="lordhonk.de">Click me!</a>')

    def test_parent_one_child(self):
        node = LeafNode("p", "Hello World!")
        node2= ParentNode("div",[node],None)
        self.assertEqual(node2.to_html(),'<div><p>Hello World!</p></div>')

    def test_nesting_parents(self):
        node = LeafNode("p", "Hello World!")
        node2= ParentNode("span",[node],None)
        node3= ParentNode("div",[node2],None)
        self.assertEqual(node3.to_html(), '<div><span><p>Hello World!</p></span></div>')

    def test_multiple_children(self):
        node = LeafNode("li","Butter")
        node2= LeafNode("li","Eggs")
        node3= LeafNode("li","Flour")
        node4= ParentNode("ul",[node,node2,node3])
        self.assertEqual(node4.to_html(),'<ul><li>Butter</li><li>Eggs</li><li>Flour</li></ul>')

if __name__ == "__main__":
    unittest.main()
