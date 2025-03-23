import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, "This is just text")
        output = "HTMLNode(None, This is just text, None, None)"
        self.assertEqual(repr(node), output)

    def test_not_eq(self):
        node = HTMLNode("p", "This is paragraph text")
        output = "HTMLNode(None, This is just text, None, None)"
        self.assertNotEqual(repr(node), output)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "Link Text", None, props)
        output = "HTMLNode(a, Link Text, None, href=\"https://www.google.com\" target=\"_blank\")"
        self.assertEqual(repr(node), output)

    def test_not_implemented_error(self):
        node = HTMLNode(None, "Test")
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Child classes will implement this method.")

if __name__ == "__main__":
    unittest.main()