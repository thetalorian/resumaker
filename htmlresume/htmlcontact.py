from models import *
from string import Template
from . import HTMLBlock

class HTMLContact(HTMLBlock):

    def __init__(self, contact: Contact):
        self.contact = contact
        self.template = Template(
"""<div class="contact">
    <div class="address">
        <div class="address1">$street</div>
        <div class="address2">$city, $state $zip</div>
    </div>
    <div class="phone">$phone</div>
    <div class="email">$email</div>
    <div class="link">$link</div>
</div>""")

    def __repr__(self) -> str:
        data = {
            "phone": self.contact.phone,
            "email": self.contact.email,
            "street": self.contact.address.street,
            "city": self.contact.address.city,
            "state": self.contact.address.state,
            "zip": self.contact.address.zip,
            "link": self.contact.link
        }
        output = self.template.substitute(data)
        return self.indent(output)
