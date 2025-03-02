import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode("div", "text", {"href": "https://www.google.com", "target": "_blank"}, None)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html_with_empty_props(self):
        node = HTMLNode("div", "text", None, {})
        self.assertEqual(node.props_to_html(), '')
        self.__repr__()
        
    def test_props_to_html_with_none_props(self):
        node = HTMLNode("div", "text")
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_i(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaf_to_html_link(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    

if __name__ == "__main__":
    unittest.main()