import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode("div", "text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_props_to_html_with_empty_props(self):
        node = HTMLNode("div", "text", None, {})
        self.assertEqual(node.props_to_html(), '')
        self.__repr__()
        
    def test_props_to_html_with_none_props(self):
        node = HTMLNode("div", "text")
        self.assertEqual(node.props_to_html(), '')

    

if __name__ == "__main__":
    unittest.main()