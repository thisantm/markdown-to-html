import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, f"self.assertEqual(node, node2) failed: {node} != {node2}")

        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold", "test.com")
        self.assertEqual(node, node2, f"self.assertEqual(node, node2) failed: {node} != {node2}")

        node = TextNode("This is a text node", "bold", "test.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, f"self.assertNotEqual(node, node2) failed: {node} == {node2}")

        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, f"self.assertNotEqual(node, node2) failed: {node} == {node2}")


if __name__ == "__main__":
    unittest.main()
