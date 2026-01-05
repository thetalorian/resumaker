from string import Template
from models import Resume
from . import HTMLIntro, HTMLHistory, HTMLSkills, HTMLEducation, HTMLBlock, HTMLSection

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

        # Left Column for Name and introduction
        headerLeft = HTMLBlock("header-main")
        headerLeft.addChild(HTMLIntro(self.data.personal))
        header.addChild(headerLeft)

        # Right Column for Contact information
        headerRight = HTMLBlock("header-side")
        #contactInfo = HTMLContact(resume.contact)
        #headerRight.addContent(contactInfo)
        header.addChild(headerRight)

        self.addChild(header)

        # Main Body
        content = HTMLBlock("container")

        # Left column for work history
        contentLeft = HTMLBlock("column-main")
        history = HTMLSection("Professional Experience")
        history.addChild(HTMLHistory(self.data.history))
        contentLeft.addChild(history)
        content.addChild(contentLeft)

        # Right column for Skills and Education
        contentRight = HTMLBlock("column-side")
        skills = HTMLSection("Skills")
        skills.addChild(HTMLSkills(self.data.skills))
        contentRight.addChild(skills)
        education = HTMLSection("Education")
        education.addChild(HTMLEducation(self.data.education))
        contentRight.addChild(education)
        content.addChild(contentRight)
        self.addChild(content)


    def __repr__(self) -> str:
        data = {"content": self.childContent()}
        output = self.template.substitute(data)
        return self.indent(output)