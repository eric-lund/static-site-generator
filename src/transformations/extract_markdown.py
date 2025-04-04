import re

def extract_markdown_images(text):
    # regex the alt texts image urls
    alt_text = re.findall(r"\!\[(.*?)\]", text)
    image = re.findall(r"\((.*?)\)", text)

    # create a list of tuples
    new_list = []
    for i in range(len(image)):
        result = (alt_text[i], image[i])
        new_list.append(result)

    return new_list
     
def extract_markdown_links(text):
    # regex the anchors and links
    anchor = re.findall(r"\[(.*?)\]", text)
    link = re.findall(r"\((.*?)\)", text)

    # create a list of tuples
    new_list = []
    for i in range(len(link)):
        result = (anchor[i], link[i])
        new_list.append(result)
    
    return new_list
