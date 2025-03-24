import os

from block_markdown import markdown_to_htmlnode


def generate_pages_r(dir_path_content, template_path, dest_dir_path):
    source_content = os.listdir(dir_path_content)
    for item in source_content:
        content_path = os.path.join(dir_path_content, item)
        if os.path.isdir(content_path):
            new_dest_path = os.path.join(dest_dir_path, item)
            if not os.path.exists(new_dest_path):
                os.mkdir(new_dest_path)
            generate_pages_r(content_path, template_path, new_dest_path)
        elif item.endswith(".md"):
            html_name = item.replace(".md", ".html")
            final_path = os.path.join(dest_dir_path, html_name)
            generate_page(content_path, template_path, final_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_htmlnode(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
