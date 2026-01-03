from string import Template
from . import HTMLBlock

class HTMLSection(HTMLBlock):

    def __init__(self, title: str):
        super().__init__("section")
        self.title : str = title
        self.template = Template(
"""<div class="section">$title</div>
<hr>
<div class="section-content">
$content
</div>""")

    def __repr__(self) -> str:
        data = {
            "title": self.title,
            "content": self.childContent()
        }
        output = self.template.substitute(data)
        return self.indent(output)
