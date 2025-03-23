import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
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
        output = 'HTMLNode(a, Link Text, None, href="https://www.google.com" target="_blank")'
        self.assertEqual(repr(node), output)

    def test_not_implemented_error(self):
        node = HTMLNode(None, "Test")
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "child classes will implement this method")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a", "Link Text", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Link Text</a>')

    def test_leaf_to_html_value_error(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

if __name__ == "__main__":
    unittest.main()