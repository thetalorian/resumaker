import textwrap

class HTMLBlock():
    def __init__(self, cssClass: str) -> None:
        self.children: list[HTMLBlock] = []
        self.cssClass : str = cssClass


    def indent(self, input: str) -> str:
        indent : str = " " * 4
        return textwrap.indent(input, indent)


    def addChild(self, block) -> None:
        self.children.append(block)


    def childContent(self) -> str:
        output = ""
        for item in self.children:
            output += str(item)
        return output


    def __repr__(self) -> str:
        output = f"<div class=\"{self.cssClass}\">\n"
        output += self.childContent()
        output += f"</div>\n"
        return self.indent(output)
