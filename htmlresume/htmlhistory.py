from models import *
from string import Template
import textwrap
from . import HTMLBlock

class HTMLHistory(HTMLBlock):

    def __init__(self, history: list[WorkHistory]):
        super().__init__("history")
        self.history = history
        self.template = Template(
"""<div class="workhistory">
    <div class="title">$title</div>
    <div class="company">
        <span class="company-name">$company</span> : <span class="workperiod">$workperiod</span>
    </div>
    <div class="description">
$description
    </div>
</div>""")

    def __repr__(self) -> str:
        output = []
        for item in self.history:
            data = {}
            data['title'] = item.title
            data['company'] = item.company
            start = item.start_date.strftime('%m/%d%Y')
            if not item.end_date:
                end = "Current"
            else:
                end = item.end_date.strftime('%m/%d/%Y')
            data['workperiod'] = f"{start} - {end}"

            description = []
            if item.description.paragraphs:
                for paragraph in item.description.paragraphs:
                    description.append(f"<p>{paragraph}</p>")
            if item.description.bullets:
                description.append("<ul>")
                for bullet in item.description.bullets:
                    description.append(self.indent(f"<li>{bullet}</li>"))
                description.append("</ul>")
            data['description'] = self.indent("\n".join(description), 2)
            output.append(self.template.substitute(data))
        return self.indent("\n".join(output))
