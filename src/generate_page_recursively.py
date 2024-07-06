from block_markdown import markdown_to_html_node, markdown_to_blocks
import os


def generate_page_recursively(from_path, template_path, dst_path):
    for item in os.listdir(from_path):
        itemSrcPath = os.path.join(from_path, item)
        itemDstPath = os.path.join(dst_path, item)
        if not os.path.isfile(itemSrcPath):
            generate_page_recursively(itemSrcPath, template_path, itemDstPath)
        else:                
            print(f"Generating page from {itemSrcPath} to {itemDstPath} using {template_path}")
            markdown_file = open(itemSrcPath)
            markdown = markdown_file.read()
            markdown_file.close()

            template_file = open(template_path)
            html_template = template_file.read()
            template_file.close()

            html_content = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            final_html = html_template.replace("{{ Title }}", title)
            final_html = final_html.replace("{{ Content }}", html_content)

            dst_dir = os.path.dirname(itemDstPath)
            if dst_dir != "":
                os.makedirs(dst_dir, exist_ok=True)
            
            dst_file = open(itemDstPath[:-3]+".html", "w")
            dst_file.write(final_html)
            dst_file.close()


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Title not found")
