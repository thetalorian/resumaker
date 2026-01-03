from . import HTMLBlock

class HTMLSection(HTMLBlock):

    def __init__(self, title: str):
        super().__init__("section")
        self.title : str = title

    def __repr__(self) -> str:
        output = ""
        output += f"<div class=\"section\">{self.title}</div>\n"
        output += "<hr>\n"
        output += "<div class=\"section-content\">\n"
        output += self.childContent()
        output += "</div>\n"
        return self.indent(output)
