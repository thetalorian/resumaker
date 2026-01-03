from models import Resume
from . import HTMLHeader, HTMLHistory

class HTMLBody():
    def __init__(self, resume: Resume):
        self.data : Resume = resume
        self.header : HTMLHeader = HTMLHeader()
        self.history : HTMLHistory = HTMLHistory(resume.history)

    def __repr__(self) -> str:
        output = ""
        output += "<body>\n"
        output += str(self.header)
        output += str(self.history)
        output += "</body>\n"
        return output