from textnode import *
from htmlnode import *
from inline_markdown import text_to_textnodes
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")
    final_markdown_list = []
    for i in range(len(markdown_list)):
        markdown_list[i] = markdown_list[i].strip()
        if markdown_list[i] != "":
            final_markdown_list.append(markdown_list[i])
    return final_markdown_list


def block_to_block_type(block):
    block_parts = block.split("\n")
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading

    if len(block_parts) > 1 and block_parts[0].startswith("```") and block_parts[-1].startswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in block_parts:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote

    if block.startswith("* "):
        for line in block_parts:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("- "):
        for line in block_parts:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("1. "):
        for i in range(1, len(block_parts)):
            if not block_parts[i].startswith(f"{i+1}. "):
                return block_type_paragraph
        return block_type_ordered_list

    return block_type_paragraph


def define_html_children(markdown):
    text_nodes = text_to_textnodes(markdown)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes


def paragraph_to_html(block):
    parts = block.split("\n")
    full_paragraph = " ".join(parts)
    children = define_html_children(full_paragraph)
    return ParentNode("p", children)


def heading_to_html(block):
    parts = block.split(" ")
    full_heading = " ".join(parts[1:])
    level = len(re.match(r"#+", block).group())
    children = define_html_children(full_heading)
    return ParentNode(f"h{level}", children)


def code_to_html(block):
    parts = block.split("\n")
    full_code = "\n".join(parts[1:-1])
    children = define_html_children(full_code)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])


def quote_to_html(block):
    parts = block.split("\n")
    quote_list = []
    for part in parts:
        quote_list.append(part.lstrip("> ").strip())
    full_quote = " ".join(quote_list)
    children = define_html_children(full_quote)
    return ParentNode("blockquote", children)


def ul_to_html(block):
    parts = block.split("\n")
    full_list = []
    for part in parts:
        child = define_html_children(part[2:])
        full_list.append(ParentNode("li", child))
    return ParentNode("ul", full_list)


def ol_to_html(block):
    parts = block.split("\n")
    full_list = []
    for part in parts:
        child = define_html_children(part[3:])
        full_list.append(ParentNode("li", child))
    return ParentNode("ol", full_list)


def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    children = []
    for block in blocks_list:
        html_node = markdown_block_to_html(block)
        children.append(html_node)
    return ParentNode("div", children)


def markdown_block_to_html(block):
    match block_to_block_type(block):
        case "paragraph":
            return paragraph_to_html(block)
        case "heading":
            return heading_to_html(block)
        case "code":
            return code_to_html(block)
        case "quote":
            return quote_to_html(block)
        case "unordered_list":
            return ul_to_html(block)
        case "ordered_list":
            return ol_to_html(block)
        case default:
            raise ValueError("Block not of a valid type")
