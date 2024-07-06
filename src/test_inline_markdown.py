import unittest
from inline_markdown import *
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_empty_list(self):
        # Test case 1: Empty list of nodes
        old_nodes = []
        delimiter = ","
        text_type = "text"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, [])

    def test_split_nodes_delimiter_no_delimiter(self):
        # Test case 2: No delimiter in the nodes
        old_nodes = [TextNode("Hello World", text_type_text)]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, [TextNode("Hello World", text_type_text)])

    def test_split_nodes_delimiter_bold(self):
        # Test case 3: Single delimiter in the nodes
        old_nodes = [TextNode("Hello **World**", text_type_text)]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_bold)],
        )

    def test_split_nodes_delimiter_two_bolded_words(self):
        # Test case 4: Two bolded words in the nodes
        old_nodes = [TextNode("Hello **World** and **Universe**", text_type_text)]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("Universe", text_type_bold),
            ],
        )

    def test_split_nodes_delimiter_long_bolded_words(self):
        # Test case 5: Long bolded words in the nodes
        old_nodes = [TextNode("Hello **World and Universe**!", text_type_text)]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World and Universe", text_type_bold),
                TextNode("!", text_type_text),
            ],
        )

    def test_split_nodes_delimiter_italic(self):
        # Test case 6: Single italic word in the nodes
        old_nodes = [TextNode("Hello *World*", text_type_text)]
        delimiter = "*"
        text_type = "italic"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_italic)],
        )

    def test_split_nodes_delimiter_two_italic_words(self):
        # Test case 7: Two italic words in the nodes
        old_nodes = [TextNode("Hello *World* and *Universe*", text_type_text)]
        delimiter = "*"
        text_type = "italic"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_italic),
                TextNode(" and ", text_type_text),
                TextNode("Universe", text_type_italic),
            ],
        )

    def test_split_nodes_delimiter_long_italic_words(self):
        # Test case 8: Long italic words in the nodes
        old_nodes = [TextNode("Hello *World and Universe*!", text_type_text)]
        delimiter = "*"
        text_type = "italic"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World and Universe", text_type_italic),
                TextNode("!", text_type_text),
            ],
        )

    def test_split_nodes_delimiter_code(self):
        # Test case 9: Single code in the nodes
        old_nodes = [TextNode("Hello `World`", text_type_text)]
        delimiter = "`"
        text_type = "code"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_code)],
        )

    def test_split_nodes_delimiter_two_codes(self):
        # Test case 10: Two codes in the nodes
        old_nodes = [TextNode("Hello `World` and `Universe`", text_type_text)]
        delimiter = "`"
        text_type = "code"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_code),
                TextNode(" and ", text_type_text),
                TextNode("Universe", text_type_code),
            ],
        )

    def test_split_nodes_delimiter_long_codes(self):
        # Test case 11: Long codes in the nodes
        old_nodes = [TextNode("Hello `World and Universe`!", text_type_text)]
        delimiter = "`"
        text_type = "code"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World and Universe", text_type_code),
                TextNode("!", text_type_text),
            ],
        )

    def test_extract_markdown_images_no_images(self):
        # Test case 1: No images in the text
        text = "This is a sample text"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_images_one_image(self):
        # Test case 2: Single image in the text
        text = "This is an ![image](https://example.com/image.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("image", "https://example.com/image.jpg")])

    def test_extract_markdown_images_two_images(self):
        # Test case 3: Two images in the text
        text = "This is an ![image1](https://example.com/image1.jpg) and ![image2](https://example.com/image2.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [
                ("image1", "https://example.com/image1.jpg"),
                ("image2", "https://example.com/image2.jpg"),
            ],
        )

    def test_extract_markdown_links_no_links(self):
        # Test case 1: No links in the text
        text = "This is a sample text"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_one_link(self):
        # Test case 2: Single link in the text
        text = "This is a [link](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://example.com")])

    def test_extract_markdown_links_two_links(self):
        # Test case 3: Two links in the text
        text = "This is a [link1](https://example.com) and [link2](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link1", "https://example.com"), ("link2", "https://example.com")])

    def test_split_nodes_image_no_images(self):
        # Test case 1: No images in the nodes
        old_nodes = [
            TextNode("Hello", text_type_text),
            TextNode("World", text_type_text),
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [TextNode("Hello", text_type_text), TextNode("World", text_type_text)],
        )

    def test_split_nodes_image_one_image(self):
        # Test case 2: Single image in the nodes
        old_nodes = [
            TextNode(
                "This is an ![image](https://example.com/image.jpg) test",
                text_type_text,
            )
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is an ", text_type_text),
                TextNode("image", text_type_image, "https://example.com/image.jpg"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_image_two_images(self):
        # Test case 3: Two images in the nodes
        old_nodes = [
            TextNode(
                "This is an ![image1](https://example.com/image1.jpg) and ![image2](https://example.com/image2.jpg) test",
                text_type_text,
            )
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is an ", text_type_text),
                TextNode("image1", text_type_image, "https://example.com/image1.jpg"),
                TextNode(" and ", text_type_text),
                TextNode("image2", text_type_image, "https://example.com/image2.jpg"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_image_two_nodes_with_images(self):
        # Test case 4: Two nodes with images both with images
        old_nodes = [
            TextNode("This is an ![image1](https://example.com/image1.jpg)", text_type_text),
            TextNode(" and ![image2](https://example.com/image2.jpg)", text_type_text),
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is an ", text_type_text),
                TextNode("image1", text_type_image, "https://example.com/image1.jpg"),
                TextNode(" and ", text_type_text),
                TextNode("image2", text_type_image, "https://example.com/image2.jpg"),
            ],
        )

    def test_split_nodes_image_at_start(self):
        # Test case 5: Image at the start of the nodes
        old_nodes = [TextNode("![image](https://example.com/image.jpg) test", text_type_text)]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("image", text_type_image, "https://example.com/image.jpg"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_image_at_end(self):
        # Test case 6: Image at the end of the nodes
        old_nodes = [TextNode("test ![image](https://example.com/image.jpg)", text_type_text)]
        result = split_nodes_image(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("test ", text_type_text),
                TextNode("image", text_type_image, "https://example.com/image.jpg"),
            ],
        )

    def test_split_nodes_link_no_links(self):
        # Test case 1: No links in the nodes
        old_nodes = [
            TextNode("Hello", text_type_text),
            TextNode("World", text_type_text),
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [TextNode("Hello", text_type_text), TextNode("World", text_type_text)],
        )

    def test_split_nodes_link_one_link(self):
        # Test case 2: Single link in the nodes
        old_nodes = [TextNode("This is a [link](https://example.com) test", text_type_text)]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", text_type_text),
                TextNode("link", text_type_link, "https://example.com"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_link_two_links(self):
        # Test case 3: Two links in the nodes
        old_nodes = [
            TextNode(
                "This is a [link1](https://example.com) and [link2](https://example.com) test",
                text_type_text,
            )
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", text_type_text),
                TextNode("link1", text_type_link, "https://example.com"),
                TextNode(" and ", text_type_text),
                TextNode("link2", text_type_link, "https://example.com"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_link_two_nodes_with_links(self):
        # Test case 4: Two nodes with links both with links
        old_nodes = [
            TextNode("This is a [link1](https://example.com)", text_type_text),
            TextNode(" and [link2](https://example.com)", text_type_text),
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("This is a ", text_type_text),
                TextNode("link1", text_type_link, "https://example.com"),
                TextNode(" and ", text_type_text),
                TextNode("link2", text_type_link, "https://example.com"),
            ],
        )

    def test_split_nodes_link_at_start(self):
        # Test case 5: Link at the start of the nodes
        old_nodes = [TextNode("[link](https://example.com) test", text_type_text)]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("link", text_type_link, "https://example.com"),
                TextNode(" test", text_type_text),
            ],
        )

    def test_split_nodes_link_at_end(self):
        # Test case 6: Link at the end of the nodes
        old_nodes = [TextNode("test [link](https://example.com)", text_type_text)]
        result = split_nodes_link(old_nodes)
        self.assertEqual(
            result,
            [
                TextNode("test ", text_type_text),
                TextNode("link", text_type_link, "https://example.com"),
            ],
        )

    def test_text_to_textnodes(self):
        # Test case 1: No markdown in the text
        text = "Hello World"
        result = text_to_textnodes(text)
        self.assertEqual(result, [TextNode("Hello World", text_type_text)])

    def test_text_to_textnodes_bold(self):
        # Test case 2: Bold markdown in the text
        text = "Hello **World**"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_bold)],
        )

    def test_text_to_textnodes_italic(self):
        # Test case 3: Italic markdown in the text
        text = "Hello *World*"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_italic)],
        )

    def test_text_to_textnodes_code(self):
        # Test case 4: Code markdown in the text
        text = "Hello `World`"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [TextNode("Hello ", text_type_text), TextNode("World", text_type_code)],
        )

    def test_text_to_textnodes_link(self):
        # Test case 5: Link markdown in the text
        text = "Hello [World](https://example.com)"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_link, "https://example.com"),
            ],
        )

    def test_text_to_textnodes_image(self):
        # Test case 6: Image markdown in the text
        text = "Hello ![World](https://example.com/image.jpg)"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_image, "https://example.com/image.jpg"),
            ],
        )

    def test_text_to_textnodes_all_markdown(self):
        # Test case 7: All markdown in the text
        text = "Hello **World** *Universe* `Code` [Link](https://example.com) ![Image](https://example.com/image.jpg)"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("Hello ", text_type_text),
                TextNode("World", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("Universe", text_type_italic),
                TextNode(" ", text_type_text),
                TextNode("Code", text_type_code),
                TextNode(" ", text_type_text),
                TextNode("Link", text_type_link, "https://example.com"),
                TextNode(" ", text_type_text),
                TextNode("Image", text_type_image, "https://example.com/image.jpg"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
