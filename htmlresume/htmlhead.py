from string import Template
from . import HTMLBlock

class HTMLHead(HTMLBlock):
    def __init__(self):
        self.title: str = "Resume of Samuel Plum"
        self.meta : dict = {'charset': 'utf-8'}
        self.link: dict = {'href': 'resume.css', 'rel': 'stylesheet'}
        self.template = Template(
"""<head>
    <meta $meta>
    <link $link>
    <title>$title</title>
</head>""")

    def __repr__(self) -> str:
        data = {}
        data['meta'] = " ".join([f"{k}=\"{v}\"" for k,v in self.meta.items()])
        data['link'] = " ".join([f"{k}=\"{v}\"" for k,v in self.link.items()])
        data['title'] = self.title
        output = self.template.substitute(data)
        return self.indent(output)