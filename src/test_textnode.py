import unittest

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

if __name__ == "__main__":
    unittest.main()
    