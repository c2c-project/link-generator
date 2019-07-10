# GENERATES LINKS TO UPLOAD TO API
import validators
from furl import furl

def genLinks(regUrl, contacts):
    retVal = []
    names = []
    print(len(contacts))
    for contact in contacts:
        f = furl(regUrl)
        # extract name
        name = contact['embeddedData']['Voters_FirstName'] + ' ' + contact['embeddedData']['Voters_LastName'][0];
        
        # for duplicate names, append a number to them
        if name in names:
            name = name + str(names.count(name))
        names = names + [name]

        # url generation
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
        retVal = retVal + [copy]
    return retVal