from string import Template
from models import *
from . import HTMLHead, HTMLBody


class HTMLResume():
    """Resume Class

    Generates a resume as an html page.
    """

    def __init__(self, resume: Resume):
        self.language = "en"
        self.head : HTMLHead = HTMLHead()
        self.body : HTMLBody = HTMLBody(resume)
        self.template : Template = Template(
"""<!DOCTYPE html>
<html lang="$language">
$head
$body
</html>""")


    def __repr__(self) -> str:
        data = {}
        data['language'] = self.language
        data['head'] = str(self.head)
        data['body'] = str(self.body)
        output = self.template.substitute(data)
        return output
