import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, "This is just text")
        output = "HTMLNode(None, This is just text, None, None)"
        self.assertEqual(repr(node), output)

    def test_not_eq(self):
        node = HTMLNode("p", "This is paragraph text")
        output = "HTMLNode(None, This is just text, None, None)"
        self.assertNotEqual(repr(node), output)

    def test_repr(self):
        node = HTMLNode(
            "a",
            "Link Text",
            None,
            {"href":"https://www.google.com", "target":"_blank"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, Link Text, None, {'href': 'https://www.google.com', 'target': '_blank'})",
        )

    def test_not_implemented_error(self):
        node = HTMLNode(None, "Test")
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "child classes will implement this method")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
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
        self.assertEqual(str(context.exception), "All leaf nodes require a value")


class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        child_nodes = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", child_nodes)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html_with_props(self):
        child_props = {
            "class": "todo"
        }
        child_nodes = [
            LeafNode("li", "Do this", child_props),
            LeafNode("li", "Do that", child_props),
            LeafNode("li", "Do something else", child_props),
            LeafNode("li", "Do another thing", child_props),
        ]
        props = {
            "class": "toDoList",
        }
        node = ParentNode("ul", child_nodes, props)
        self.assertEqual(node.to_html(), '<ul class="toDoList"><li class="todo">Do this</li><li class="todo">Do that</li><li class="todo">Do something else</li><li class="todo">Do another thing</li></ul>')

    def test_parent_to_html_with_grandchildren(self):
        grandchild_props = {
            "class": "navlink",
            "href": "www.google.com"
        }
        grandchild_node = LeafNode("a", "Link Text", grandchild_props)
        child_props = {
            "class": "navitem"
        }
        child_node = ParentNode("li", [grandchild_node], child_props)
        parent_props = {
            "class": "navbar"
        }
        parent_node = ParentNode("ul", [child_node], parent_props)
        self.assertEqual(parent_node.to_html(), '<ul class="navbar"><li class="navitem"><a class="navlink" href="www.google.com">Link Text</a></li></ul>')

    def test_parent_to_html_no_tag_value_error(self):
        child_nodes = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode(None, child_nodes)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Parent node requires a tag")

    def test_parent_to_html_no_children_value_error(self):
        node = ParentNode("b", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Parent node requires children")


if __name__ == "__main__":
    unittest.main()