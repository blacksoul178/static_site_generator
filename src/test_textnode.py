import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a test node", TextType.ITALIC)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_eq_w_URL(self):
        node = TextNode("This is a test node", TextType.ITALIC, url="https://www.ford.ca")
        node2 = TextNode("This is a test node", TextType.ITALIC, url="https://www.ford.ca")
        self.assertEqual(node, node2)

    def test_mismatch_type(self):
        node = TextNode("This is a test node", TextType.CODE)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_mismatch_text(self):
        node = TextNode("This is node a test", TextType.ITALIC)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_Mismatch_url(self):
        node = TextNode("This is a test node", TextType.ITALIC)
        node2 = TextNode("This is a test node", TextType.ITALIC, url="https://www.ford.ca")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()