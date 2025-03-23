from textnode import TextNode, TextType

def main():
    text_node = TextNode("Some Text Here", TextType.TEXT)
    url_node = TextNode("A link to my site", TextType.LINK, "https://edward-vonschondorf.dev/" )
    print(text_node)
    print(url_node)

if __name__ == "__main__":
    main()