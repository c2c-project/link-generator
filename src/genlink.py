# GENERATES LINKS TO UPLOAD TO API
import validators
from furl import furl

def genLinks(regUrl, contacts):
    retVal = []
    print(len(contacts))
    for contact in contacts:
        f = furl(regUrl)
        name = contact['embeddedData']['Voters_FirstName'] + ' ' + contact['embeddedData']['Voters_LastName'][0];
        modifiedUrl = f.add({ 'client': '18591', 'name': name, 'uniqueid': contact['id'], }).url
        if not validators.url(modifiedUrl):
            print('ERR: URL IS NOT VALID')
            return
        copy = contact
        if copy['embeddedData']:
            copy['embeddedData']['sessionUrl'] = modifiedUrl
        else:
            copy['embeddedData'] = dict()
            copy['embeddedData']['sessionUrl'] = modifiedUrl
        retVal.append(copy)
    return retVal