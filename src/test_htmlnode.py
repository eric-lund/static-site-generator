import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()