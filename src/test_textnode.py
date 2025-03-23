import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is text node 1", TextType.CODE)
        node2 = TextNode("This is text node 2", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node2 = TextNode("This is text node 2", TextType.LINK)
        self.assertIsNone(node2.url)

    def test_url_is_not_none(self):
        node2 = TextNode("This is text node 2", TextType.LINK, "www.google.com")
        self.assertIsNotNone(node2.url)

if __name__ == "__main__":
    unittest.main()