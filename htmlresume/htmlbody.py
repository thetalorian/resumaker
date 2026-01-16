from string import Template
from models import Resume
from . import HTMLIntro, HTMLContact, HTMLHistory, HTMLSkills, HTMLEducation, HTMLBlock, HTMLSection

class HTMLBody(HTMLBlock):
    def __init__(self, resume: Resume):
        super().__init__("body")
        self.data : Resume = resume
        self.configureLayout()
        self.template = Template(
"""<body>
$content
</body>""")

    def configureLayout(self):
        # Configure Layout

        # Info Header
        header = HTMLBlock("container")

        # Main Column for Name and introduction
        main_column = HTMLBlock("header-main")
        main_column.addChild(HTMLIntro(self.data.personal))
        header.addChild(main_column)

        # Side Column for Contact information
        side_column = HTMLBlock("header-side")
        side_column.addChild(HTMLContact(self.data.contact))
        header.addChild(side_column)

        self.addChild(header)


        # Main Body
        content = HTMLBlock("container")

        # Side column for Skills and Education
        side_column = HTMLBlock("column-side")
        skills = HTMLSection("Skills")
        skills.addChild(HTMLSkills(self.data.skills))
        side_column.addChild(skills)

        education = HTMLSection("Education")
        education.addChild(HTMLEducation(self.data.education))
        side_column.addChild(education)
        content.addChild(side_column)

        # Main column for work history
        main_column = HTMLBlock("column-main")
        history = HTMLSection("Professional Experience")
        history.addChild(HTMLHistory(self.data.history))
        main_column.addChild(history)
        content.addChild(main_column)

        self.addChild(content)


    def __repr__(self) -> str:
        data = {"content": self.childContent()}
        output = self.template.substitute(data)
        return self.indent(output)