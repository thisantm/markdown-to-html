import unittest
from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




    This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line


* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_code(self):
        md = """
```
print("Lord")
print("of")
print("the")
print("Rings")
```
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ['```\nprint("Lord")\nprint("of")\nprint("the")\nprint("Rings")\n```'],
        )

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_code(self):
        block = "```\nThis is code\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_to_block_type_single_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_multi_quote(self):
        block = "> This is a quote\n> with 2 parts"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is a list\n* with items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list\n2. with items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph_to_html(self):
        block = "This is a paragraph"
        self.assertEqual(paragraph_to_html(block).to_html(), "<p>This is a paragraph</p>")

    def test_paragraph_to_html_with_children(self):
        self.maxDiff = None
        block = "This is a paragraph with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            paragraph_to_html(block).to_html(),
            '<p>This is a paragraph with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></p>',
        )

    def test_heading_to_html_level_1(self):
        block = "# This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h1>This is a heading</h1>")

    def test_heading_to_html_level_2(self):
        block = "## This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h2>This is a heading</h2>")

    def test_heading_to_html_level_3(self):
        block = "### This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h3>This is a heading</h3>")

    def test_heading_to_html_level_4(self):
        block = "#### This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h4>This is a heading</h4>")

    def test_heading_to_html_level_5(self):
        block = "##### This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h5>This is a heading</h5>")

    def test_heading_to_html_level_6(self):
        block = "###### This is a heading"
        self.assertEqual(heading_to_html(block).to_html(), "<h6>This is a heading</h6>")

    def test_heading_to_html_with_children(self):
        block = "# This is a heading with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            heading_to_html(block).to_html(),
            '<h1>This is a heading with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></h1>',
        )

    def test_code_to_html(self):
        block = "```\nThis is code\n```"
        self.assertEqual(code_to_html(block).to_html(), "<pre><code>This is code</code></pre>")

    def test_code_to_html_with_children(self):
        block = "```\nThis is code with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)\n```"
        self.assertEqual(
            code_to_html(block).to_html(),
            '<pre><code>This is code with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></code></pre>',
        )

    def test_quote_to_html(self):
        block = "> This is a quote"
        self.assertEqual(quote_to_html(block).to_html(), "<blockquote>This is a quote</blockquote>")

    def test_quote_to_html_multi_quote(self):
        block = "> This is a quote\n> with 2 parts"
        self.assertEqual(quote_to_html(block).to_html(), "<blockquote>This is a quote with 2 parts</blockquote>")

    def test_quote_to_html_with_children(self):
        block = "> This is a quote with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            quote_to_html(block).to_html(),
            '<blockquote>This is a quote with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></blockquote>',
        )

    def test_quote_to_html_multi_quote_with_children(self):
        block = "> This is a quote with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)\n> This is another part of the quote with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            quote_to_html(block).to_html(),
            '<blockquote>This is a quote with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img> This is another part of the quote with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></blockquote>',
        )

    def test_ul_to_html(self):
        block = "* This is a list\n* with items"
        self.assertEqual(
            ul_to_html(block).to_html(),
            "<ul><li>This is a list</li><li>with items</li></ul>",
        )

    def test_ul_to_html_with_children(self):
        block = "* This is a list with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)\n* This is another item with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            ul_to_html(block).to_html(),
            '<ul><li>This is a list with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></li><li>This is another item with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></li></ul>',
        )

    def test_ol_to_html(self):
        block = "1. This is a list\n2. with items"
        self.assertEqual(
            ol_to_html(block).to_html(),
            "<ol><li>This is a list</li><li>with items</li></ol>",
        )

    def test_ol_to_html_with_children(self):
        block = "1. This is a list with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)\n2. This is another item with **bolded** text and `code` here and [a link](https://example.com) and ![an image](https://example.com/image.jpg)"
        self.assertEqual(
            ol_to_html(block).to_html(),
            '<ol><li>This is a list with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></li><li>This is another item with <b>bolded</b> text and <code>code</code> here and <a href="https://example.com">a link</a> and <img src="https://example.com/image.jpg" alt="an image"></img></li></ol>',
        )

    def test_markdown_to_html_node(self):
        md = """
# This is a heading

This is a paragraph

```
print("Lord")
print("of")
print("the")
print("Rings")
```

> This is a quote

* This is a list
* with items

1. This is an ordered list
2. with items
"""
        html_node = markdown_to_html_node(md)
        self.assertEqual(
            html_node.to_html(),
            '<div><h1>This is a heading</h1><p>This is a paragraph</p><pre><code>print("Lord")\nprint("of")\nprint("the")\nprint("Rings")</code></pre><blockquote>This is a quote</blockquote><ul><li>This is a list</li><li>with items</li></ul><ol><li>This is an ordered list</li><li>with items</li></ol></div>',
        )


if __name__ == "__main__":
    unittest.main()
