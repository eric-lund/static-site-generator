from textnode import TextNode

def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"

    result = TextNode(text, text_type, url)
    print(result)

# ensures only runs if the file is executed directly and not imported
if __name__ == "__main__":
    main()