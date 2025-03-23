class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("child classes will implement this method")
    
    def props_to_html(self):
        if self.props:
            attributes = []
            for prop, value in self.props.items():
                attributes.append(f'{prop}="{value}"')
            return " ".join(attributes) 
        return None

    def __repr__(self):
        props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes require a value")
        if not self.tag:
            return f"{self.value}"
        props = ""
        if self.props:
            props = " " + self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node requires a tag")
        if not self.children:
            raise ValueError("Parent node requires children")
        props = ""
        if self.props:
            props = " " + self.props_to_html()
        child_nodes = []
        for child in self.children:
            child_nodes.append(child.to_html())
        return f"<{self.tag}{props}>{"".join(child_nodes)}</{self.tag}>"