class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""

        all_attributes = ""
        for attribute in self.props:
            all_attributes += f' {attribute}="{self.props[attribute]}"'
        return all_attributes
    
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            #raise ValueError("The leaf node has no value, it must do")
            return ""
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("are you kidding me? an html parent node without tag?")
        if not self.children:
            raise ValueError("it is a parent node and thus must have child nodes")
        else:
            #html_string = "<" + self.tag + self.props_to_html + ">"
            #html_string = f"<{self.tag}{self.props_to_html()}>"
            
            children_html = ""
            for child in self.children:
                children_html += child.to_html()

            #html_string += "</" + self.tag + ">"
            #html_string += f"</{self.tag}>"
            #return html_string

            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, props: {self.props})"