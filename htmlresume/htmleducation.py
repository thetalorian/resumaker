from models import *
from . import HTMLBlock
from string import Template

class HTMLEducation(HTMLBlock):

    def __init__(self, education: Education):
        self.data = education
        self.universityTemplate : Template = Template(
"""<div class="university">
    <div class="name">$name</div>
    <div class="degree">$degree</div>
    <div class="dates">$dates</div>
</div>""")
        self.certificateTemplate : Template = Template("<div class=\"certificate\">$certificate</div>"
)

    def __repr__(self) -> str:
        output = []
        if self.data.universities:
            for university in self.data.universities:
                data = {
                    "name": university.name,
                    "degree": university.major,
                    "dates": f"{str(university.start)} - {str(university.end)}"
                }
                output.append(self.universityTemplate.substitute(data))
        if self.data.certifications:
            for cert in self.data.certifications:
                data = {"certificate": cert}
                output.append(self.certificateTemplate.substitute(data))
        return self.indent("\n".join(output))
