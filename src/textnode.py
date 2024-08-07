from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
def text_node_to_html_node(text_node):
    txt_type = text_node.text_type
    if txt_type == "text":
        return LeafNode(None, text_node.text, None)
    if txt_type == "bold":
        return LeafNode("b", text_node.text, None)
    if txt_type == "italic":
        return LeafNode("i", text_node.text, None)
    if txt_type == "code":
        return LeafNode("code", text_node.text, None)
    if txt_type == "link":
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    if txt_type == "image":
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    else:
        raise Exception("Invalid text type")
    
#def split_nodes_delimiter(old_nodes, delimiter, text_type):
