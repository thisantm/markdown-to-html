import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), f' href="https://www.google.com" target="_blank"')

        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), node2.props_to_html(), f"self.assertEqual(node, node2) failed: {node} != {node2}"
        )

    def test_html_node__repr__(self):
        node = HTMLNode("test0", "test1", "test2", "test3")
        self.assertEqual(node.__repr__(), "HTMLNode(tag = test0, value = test1, children = test2, props = test3)")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.", "Should be: This is a paragraph of text.")

    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(), "<p>This is a paragraph of text.</p>", "Should be <p>This is a paragraph of text.</p>"
        )

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
            'Should be <a href="https://www.google.com">Click me!</a>',
        )

    def test_to_html_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children_and_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )

    def test_to_html_with_nested_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<p><b>Bold text</b><i>italic text</i></p><i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_nested_children_and_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("i", "italic text"),
                    ],
                    {"href": "https://www.google.com"},
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<p href="https://www.google.com"><b>Bold text</b>Normal text<p href="https://www.google.com"><b>Bold text</b><i>italic text</i></p><i>italic text</i>Normal text</p>',
        )


if __name__ == "__main__":
    unittest.main()
