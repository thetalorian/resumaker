from string import Template
import textwrap

class HTMLBlock():
    def __init__(self, cssClass: str) -> None:
        self.children: list[HTMLBlock] = []
        self.cssClass : str = cssClass
        self.template : Template = Template(
"""<div class="$cssClass">
$content
</div>""")


    def indent(self, input: str, level: int = 1) -> str:
        indent : str = " " * 4 * level
        return textwrap.indent(input, indent)


    def addChild(self, block) -> None:
        self.children.append(block)


    def childContent(self) -> str:
        output = []
        for item in self.children:
            output.append(str(item))
        return "\n".join(output)


    def __repr__(self) -> str:
        data = {}
        data['cssClass'] = self.cssClass
        data['content'] = self.childContent()
        output = self.template.substitute(data)
        return self.indent(output)
