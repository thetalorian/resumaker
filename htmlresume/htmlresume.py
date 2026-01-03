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


    def __repr__(self) -> str:
        output = "<!DOCTYPE html>\n"
        output += f"<html lang=\"{self.language}\">\n"
        output += str(self.head)
        output += str(self.body)
        output += f"</html>\n"
        return output
