from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown Syntax")
            for i in range(len(parts)):
                if i % 2 == 0:
                    if parts[i] != "":
                        new_nodes.append(TextNode(parts[i], text_type_text))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        image_tup_list = extract_markdown_images(node.text)
        if len(image_tup_list) == 0:
            new_nodes.append(node)
            continue

        split_text = node.text
        for image_tup in image_tup_list:
            parts = split_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            split_text = parts[1]

        if parts[-1] != "":
            new_nodes.append(TextNode(parts[-1], text_type_text))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        link_tup_list = extract_markdown_links(node.text)
        if len(link_tup_list) == 0:
            new_nodes.append(node)
            continue

        split_text = node.text
        for link_tup in link_tup_list:
            parts = split_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            split_text = parts[1]

        if parts[-1] != "":
            new_nodes.append(TextNode(parts[-1], text_type_text))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
