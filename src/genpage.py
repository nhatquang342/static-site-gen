import os
from pathlib import Path
from markdown_blocks import *

def generate_page(from_path, template_path, dest_path):
    print(f"... from {from_path} to {dest_path} using {template_path}")
    
    #with open(from_path, "r", encoding="utf-8") as f:
    #    markdown_content = f.read()

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    #with open(template_path, "r", encoding="utf-8") as f:
    #    template_content = f.read()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()
    
    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    
    title = extract_title(markdown_content)
    
    full_html = (
        template_content
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
    )

    #if not os.path.exists(dest_path):
    #    os.makedirs(dest_path)
    #with open(dest_path, "w", encoding="utf-8") as f:
    #    f.write(full_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for name in os.listdir(dir_path_content): #listdir → gets all items (files and folders) inside the current directory.
        src = os.path.join(dir_path_content, name) # → the full path of the item in the content directory.
        dst = os.path.join(dest_dir_path, name) # → the corresponding full path in the destination directory.
        #This way, src and dst always “mirror” each other’s structure.

        if os.path.isfile(src) and name.lower().endswith(".md"): # Only process Markdown files (skip binaries, .DS_Store, etc.)
            dst = Path(dst).with_suffix(".html")
            generate_page(src, template_path, dst)
        else:
            generate_pages_recursive(src, template_path, dst) # Recurse into subdirectories, mirroring structure in dest