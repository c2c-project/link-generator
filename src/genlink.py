# GENERATES LINKS TO UPLOAD TO API
import validators
from furl import furl

def genLinks(regUrl, contacts):
    retVal = []
    for contact in contacts:
        f = furl(regUrl)
        modifiedUrl = f.add({ 'fname': contact['firstName'], 'lName': contact['lastName'], 'email': contact['email'], 'qId': contact['id'] }).url
        if not validators.url(modifiedUrl):
            print('ERR: URL IS NOT VALID')
            return
        copy = contact
        copy['sessionUrl'] = modifiedUrl
        retVal.append(copy)
    return retVal