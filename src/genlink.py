# GENERATES LINKS TO UPLOAD TO API
import validators
from furl import furl

def genLinks(baseUrl, contacts):
    for contact in contacts:
        f = furl(baseUrl)
        firstName, lastName, email = contact
        # id is a reserved word in python for objects...
        contactId = contact.id
        modifiedUrl = f.add({ 'fname': firstName, 'lName': lastName, 'email': email, 'qId': contactId })
        print(modifiedUrl)

        