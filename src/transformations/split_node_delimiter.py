from textnode import TextType, TextNode;

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # Append the text if the TextType is not TEXT
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue    # continue on to the next node in old_nodes

        #grab the text for the current node
        text = node.text        
     
        # if the delimiter isn't in the text, then add the original node and move to the next one
        if delimiter not in text:
            new_nodes.append(node)
            continue
        
        if len(text.split(delimiter)) % 2 == 0:
            raise ValueError(f"Closing delimiter '{delimiter}' not found")

        # find the first delimiter
        start_index = text.find(delimiter)
        # find the closing delimter index
        end_index = text.find(delimiter, start_index + len(delimiter))
        
        # slice everything from the beginning of the string until the delimiter start_index
        # and append the TextNode
        new_nodes.append(TextNode(text[:start_index], TextType.TEXT))       
        
        # slice between the first delimiter + plus the length of the delimiter (e.g. **)
        # to the index of the second delimiter
        between_delimiters = text[start_index + len(delimiter):end_index]
        new_nodes.append(TextNode(between_delimiters, text_type))

        # slice the rest of text after the last delimiter
        end_text = text[end_index + len(delimiter):]
        
        # Add the text after the last delimiter
        if end_text:
            new_nodes.append(TextNode(end_text, TextType.TEXT))
        
    return new_nodes
   


