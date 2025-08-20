import os
import shutil
import sys
from genpage import *

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else default_basepath
    
    #dir_path_content = "content"
    #template_path = "template.html"
    #dest_dir_path = "docs"

    #print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    shutil.copytree(dir_path_static, dir_path_public)
    print("Finished copying everything")

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


main()