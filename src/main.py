from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from copy_static import *
from generate_page import *
from generate_page_recursively import *
import os
import shutil


def main():
    if not os.path.exists("./static"):
        raise Exception("Static folder not found")

    if not os.path.exists("./public"):
        print("Creating public folder")
        os.mkdir("./public")

    if os.listdir("./public"):
        print("Cleaning public folder")
        shutil.rmtree("./public")
        os.mkdir("./public")

    print("Copying static folder to public folder")
    copyFolder("./static", "./public")

    from_path = "./content"
    template_path = "./template.html"
    dst_path = "./public"
    generate_page_recursively(from_path, template_path, dst_path)


main()
