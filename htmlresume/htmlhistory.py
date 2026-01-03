from models import *

class HTMLHistory():

    def __init__(self, history: list[WorkHistory]):
        self.history = history

    def __repr__(self) -> str:
        output = ""
        output += "<div class=\"column-main\">\n"
        output += "<div class=\"section\">Professional Experience</div>\n"
        output += "<hr>\n"
        for item in self.history:
            output += f"<div class=\"workhistory\">\n"
            output += f"<div class=\"title\">{item.title}</div>\n"
            output += f"<div class=\"company\">\n"
            output += f"<span class=\"company-name\">{item.company}</span>"
            output += f"<span class=\"workperiod\">{item.start_date.strftime('%m/%d/%Y')} - "
            if not item.end_date:
                output += f"Current"
            else:
                output += f"{item.end_date.strftime('%m/%d/%Y')}"
            output += "</span>\n"
            output += f"</div>\n"
            output += "<div class=\"description\">\n"
            for paragraph in item.description:
                output += f"<p>{paragraph}</p>\n"
            output += "</div>\n"
            if item.bullets:
                output += "<ul>\n"
                for bullet in item.bullets:
                    output += f"<li>{bullet}</li>\n"
                output += "</ul>\n"
            output += f"</div>"
        output += "</div>\n"
        return output
