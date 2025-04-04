import unittest
from transformations.text_to_html import text_node_to_html_node
from transformations.split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TextTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.CODE, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        correct = 'TextNode(This is a text node, code, https://www.google.com)'
        node = TextNode("This is a text node", TextType.CODE, "https://www.google.com")
        self.assertEqual(repr(node), correct)

    def test_repr2(self):
        incorrect = 'TextNode(This is a text node, link, https://www.google.com)'
        node = TextNode("This is a text node", TextType.CODE, "https://www.google.com")
        self.assertNotEqual(repr(node), incorrect)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("www.google.com", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "www.google.com")

    def test_image(self):
        node = TextNode({'src': "www.google.com", 'alt': "This is text"}, TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {'src': 'www.google.com', 'alt': 'This is text'})

    def test_split_text_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT),])
    
    def test_split_text_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("bold", TextType.BOLD),TextNode(" word", TextType.TEXT),])

    def test_split_text_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT),TextNode("italic", TextType.BOLD),TextNode(" word", TextType.TEXT),])

    def test_split_no_text_type(self):
        node = TextNode("This is text with a `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a `code block` word", TextType.BOLD)])
    
    def test_split_missing_delimiter(self):
        # Should raise ValueError
        try:
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)
            assert False, "ValueError not raised"
        except ValueError:
            pass

    def test_split_two_delimited_words(self):
        node = TextNode("This is text with a `code block` word and a **bold** word", TextType.TEXT)
        split1 = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = TextNode(split1[2].text, TextType.TEXT)
        split2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        self.assertEqual(split1, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word and a **bold** word", TextType.TEXT)])
        self.assertEqual(split2, [TextNode(" word and a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])