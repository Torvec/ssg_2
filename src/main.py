from copy_static import copy_static_files


source_dir = "./static"
dest_dir = "./public"


def main():
   copy_static_files(source_dir, dest_dir)


if __name__ == "__main__":
    main()