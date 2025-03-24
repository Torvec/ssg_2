from copy_static import copy_files_r

from generate_content import generate_pages_r


source_dir = "./static"
dest_dir = "./public"
content_dir = "./content"
template_path = "./template.html"


def main():    
    copy_files_r(source_dir, dest_dir)
    generate_pages_r(content_dir, template_path, dest_dir)


if __name__ == "__main__":
    main()