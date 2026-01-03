from models import *
from string import Template
import textwrap
from . import HTMLBlock

class HTMLHistory(HTMLBlock):

    def __init__(self, history: list[WorkHistory]):
        super().__init__("history")
        self.history = history
        self.template = Template(
"""
<div class="workhistory">
    <div class="title">$title</div>
    <div class="company">
        <span class="company-name">$company</span> : <span class="workperiod">$workperiod</span>
    </div>
    <div class="description">
$description
    </div>
    <div class="bullets">
$bullets
    </div>
</div>
""")

    def __repr__(self) -> str:
        output = ""
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

            data['description'] = ""
            for paragraph in item.description:
                data['description'] += f"        <p>{paragraph}</p>\n"
            data['bullets'] = ""
            if item.bullets:
                data['bullets'] += "        <ul>\n"
                for bullet in item.bullets:
                    data['bullets'] += f"            <li>{bullet}</li>\n"
                data['bullets'] += "        </ul>"
            output += self.template.substitute(data)
        return self.indent(output)
