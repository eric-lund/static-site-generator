import unittest

from htmlnode import HTMLNode,LeafNode, ParentNode

class TextHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with no props
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        # Create a node with a single prop in a dictionary
        node = HTMLNode(props={"href": "https://www.google.com"})
        # Expected string should have a leading space
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"') 
        

    def test_props_to_html_multiple(self):
        # Create a node with multiple props in a dictionary
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        # Expected string should have a leading space
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"') 

    def test_to_html_with_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some raw text.")
        self.assertEqual(node.to_html(), "Just some raw text.")

    def test_to_html_missing_value(self):
        # Should raise ValueError
        try:
            node = LeafNode("p", None)
            node.to_html()
            assert False, "ValueError not raised"
        except ValueError:
            pass

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_nonstring_tags(self):
        child_node = LeafNode([], "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><[]>child</[]></div>")

    def test_to_html_complex_object_tag(self):
        node = ParentNode(["list", "as", "tag"], [])
        self.assertEqual(node.to_html(), "<['list', 'as', 'tag']></['list', 'as', 'tag']>")
        
    def test_to_html_numeric_tag(self):
        node = ParentNode(123, [])
        self.assertEqual(node.to_html(), "<123></123>")
    
    def test_to_html_none_tag(self):
        try:
            node = ParentNode(None, [])
            node.to_html()
            assert False, "ValueError not raised"
        except ValueError:
            pass

    def test_to_html_invalid_child_type(self):
        # Should raise TypeError
        try:
            parent = ParentNode("div", [
            LeafNode("b", "Bold text"),
            "I shouldn't be here!",  # Invalid child
            LeafNode("i", "Italic text")
            ])
            parent.to_html()
            assert False, "TypeError not raised"
        except TypeError:
            pass

if __name__ == "__main__":
    unittest.main()