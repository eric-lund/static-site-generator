import unittest

from htmlnode import HTMLNode,LeafNode

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

if __name__ == "__main__":
    unittest.main()