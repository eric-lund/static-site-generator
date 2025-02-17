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
        # todo test this output; it doesn't seem right
        if not self.props:
            return ''
        
        html_string = ''
        for key, value in self.props.items():
            html_string += ' ' + key + '="' + value +'"'

        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"