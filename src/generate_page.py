from block_markdown import markdown_to_html_node, markdown_to_blocks
import os


def generate_page(from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    html_template = template_file.read()
    template_file.close()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    final_html = html_template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    dst_dir = os.path.dirname(dst_path)
    if dst_dir != "":
        os.makedirs(dst_dir, exist_ok=True)

    dst_file = open(dst_path, "w")
    dst_file.write(final_html)
    dst_file.close()


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Title not found")
