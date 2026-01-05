from models import *
from string import Template
from . import HTMLBlock

class HTMLIntro(HTMLBlock):

    def __init__(self, personal: Personal):
        self.personal = personal
        self.template = Template(
"""<div class="personal">
    <div class="name">$name</div>
    <hr>
    <div class="introduction">
$introduction
    </div>
</div>""")

    def __repr__(self) -> str:
        data = {
            "name": self.personal.name,
            "introduction": self.indent(self.personal.introduction, 2)
        }
        output = self.template.substitute(data)
        return self.indent(output)
