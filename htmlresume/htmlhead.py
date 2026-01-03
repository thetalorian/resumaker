class HTMLHead():
    def __init__(self):
        self.title: str = "Resume of Samuel Plum"
        self.meta : dict = {'charset': 'utf-8'}
        self.link: dict = {'href': 'resume.css', 'rel': 'stylesheet'}

    def __repr__(self) -> str:
        head = ""
        head += f"<head>\n"
        head += f"  <meta"
        for k,v in self.meta.items():
            head += f" {k}=\"{v}\""
        head += ">\n"
        head += f"  <link"
        for k,v in self.link.items():
            head += f" {k}=\"{v}\""
        head += f">\n"
        head += f"  <title>{self.title}</title>\n"
        head += f"</head>\n"
        return head