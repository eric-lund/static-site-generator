class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        # tag: p, a, h1
        # value: string of the HTML tag
        # children: list of HTMLNode objects
        # props: dictionary of attributes of the HTML tag
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ''
        
        # add a leading space before the first key
        return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # We need to explicity pass Children=None, because LeafNode should never have children
        super().__init__(tag = tag, value = value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        
        if self.tag is None:
            return self.value
        
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"