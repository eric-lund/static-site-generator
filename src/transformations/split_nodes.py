from textnode import TextType, TextNode;
from transformations.extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        node_text = node.text
        extracted_image = extract_markdown_images(node_text)

        # add the original node if there are no images
        if not extracted_image:
            new_nodes.append(node)
            continue

        for image in extracted_image:
            alt = image[0]
            link = image[1]
            section = node_text.split(f"![{alt}]({link})", 1)

            # append the text when it exists
            if section[0]:           
                new_nodes.append(TextNode(section[0], TextType.TEXT))

            # append image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))

            # update the node_text if there is a second string
            node_text = section[1]
        
        # append if there's any remaining text after the last image
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        node_text = node.text
        extracted_link = extract_markdown_links(node_text)

        # add the original node if there are no images
        if not extracted_link:
            new_nodes.append(node)
            continue

        for link in extracted_link:
            alt = link[0]
            url = link[1]
            section = node_text.split(f"![{alt}]({url})", 1)

            # append the text when it exists
            if section[0]:           
                new_nodes.append(TextNode(section[0], TextType.TEXT))

            # append image node
            new_nodes.append(TextNode(alt, TextType.LINK, url))

            # update the node_text if there is a second string
            node_text = section[1]
        
        # append if there's any remaining text after the last image
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes