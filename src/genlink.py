# GENERATES LINKS TO UPLOAD TO API
import validators
from furl import furl

def genLinks(regUrl, contacts):
    retVal = []
    names = []
    print(len(contacts))
    for contact in contacts:
        f = furl(regUrl)
        # extract first name + first letter of last name
        name = contact['embeddedData']['RecipientFirstName'] + ' ' + contact['embeddedData']['RecipientLastName'][0];
        # extract study id
        studyId = contact['embeddedData']['study_id']
        
        # for duplicate names, append a number to them
        if name in names:
            name = name + str(names.count(name))
        names = names + [name]

        # url generation
        modifiedUrl = f.add({ 'client': '18718', 'name': name, 'uniqueid': studyId, }).url
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