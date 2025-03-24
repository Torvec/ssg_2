import sys

import os

import shutil

from copy_static import copy_files_r

from generate_content import generate_pages_r


source_dir = "./static"
dest_dir = "./docs"
content_dir = "./content"
template_path = "./template.html"


basepath = '/'
if len(sys.argv) > 1:
    basepath = sys.argv[1]


def main():

   print("Deleting docs directory...")
   if os.path.exists(dest_dir):
      shutil.rmtree(dest_dir)

   print("Copying static files to docs directory...")
   copy_files_r(source_dir, dest_dir)

   print("Generating content...")
   generate_pages_r(content_dir, template_path, dest_dir, basepath)


if __name__ == "__main__":
    main()