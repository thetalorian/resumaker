from models import *
from . import HTMLBlock
from string import Template

class HTMLSkills(HTMLBlock):

    def __init__(self, skills: list[SkillSet]):
        self.skills = skills
        self.template : Template = Template(
"""<div class="skillset">
    <div class="skillcategory">$category</div>
    <div class="skills">
$skills
    </div>
</div>""")

    def __repr__(self) -> str:
        output = []
        for skill in self.skills:
            data = {
                "category": skill.category,
                "skills": self.indent(", ".join(skill.entries), 2)
            }
            output.append(self.template.substitute(data))
        return self.indent("\n".join(output))
