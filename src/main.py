from textnode import TextNode, TextType

from htmlnode import HTMLNode

def main():
    text_node = TextNode("Some Text Here", TextType.TEXT)
    url_node = TextNode("A link to my site", TextType.LINK, "https://edward-vonschondorf.dev/" )
    print(text_node)
    print(url_node)
    html_node = HTMLNode(None, "This is Text")
    html_node_2 = HTMLNode("p", "This is paragraph text")
    link_attributes = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    html_node_3 = HTMLNode("a", "This is a link", None, link_attributes)
    print(html_node)
    print(html_node_2)
    print(html_node_3)

if __name__ == "__main__":
    main()