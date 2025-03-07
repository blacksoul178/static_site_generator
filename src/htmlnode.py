


class HTMLNode():
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag  #String
        self.value = value  
        self.props = props
        self.children = children


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        if self.props == None:
            return ""
        for key,value in self.props.items():
             string += f" {key}=\"{value}\""
        return string
    
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("value is required")
        super().__init__(tag,value, props, None)



    def to_html(self):
        props_string = ""
        #if self.props is not None:
            #for key,value in self.props.items():
               # props_string += f" {key}=\"{value}\""
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag,children, props = None ):
        super().__init__(tag, None, props, children )

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        if self.value:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
        