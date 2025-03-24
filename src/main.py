import os

import shutil

from copy_static import copy_files_r

from generate_content import generate_page


source_dir = "./static"
dest_dir = "./public"
content_dir = "./content"
template_path = "./template.html"


def main():
   print("Deleting public directory...")
   if os.path.exists(dest_dir):
      shutil.rmtree(dest_dir)

   print("Copying static files to public directory...")
   copy_files_r(source_dir, dest_dir)


   print("Generating page...")
   generate_page(
      os.path.join(content_dir, "index.md"),
      template_path,
      os.path.join(dest_dir, "index.html"),
   )


if __name__ == "__main__":
    main()