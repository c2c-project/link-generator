# QUALTRICS API
import requests
import json
from urllib.parse import urlparse
import validators
import genbackup

# https://api.qualtrics.com/reference#list-mailing-lists
# curl -H 'X-API-TOKEN: yourtokenhere' 'https://yourdatacenterid.qualtrics.com/API/v3/mailinglists'
def getLists(config, apiUrl):
    headers = {
        'x-api-token': config['apiToken']
    }
    response = requests.get(apiUrl, headers = headers)
    return response.json()['result']['elements']

# https://api.qualtrics.com/reference#list-contacts
# curl -H 'X-API-TOKEN: yourtokenhere' 'https://yourdatacenterid.qualtrics.com/API/v3/mailinglists/ML_1234567890AbCdE/contacts'
def getContacts(config, apiUrl, targetList, urlOverride = None):
    headers = {
        'x-api-token': config['apiToken']
    }
    url = apiUrl + targetList['id'] + '/contacts'
    if (urlOverride):
        url = urlOverride
    response = requests.get(url, headers = headers).json()['result']
    # print(response)
    nextPage = response['nextPage']
    results = response['elements']
    if (nextPage):
        results = results + getContacts(config,apiUrl,targetList, urlOverride=nextPage)
    # print(results)
    return results

# runs any put hooks before the actual put requests, such as generate a backup
def putHook(updatedList):
    genbackup.backup(updatedList)

def isIterable(val):
    return isinstance(val, dict) or isinstance(val, list)

def parseDict(contact):
    retVal = dict()
    for key in contact:
        if contact[key] and not key == 'emailHistory':
            value = contact[key]
            if(isIterable(value)):
                value = mapfunc(value)
            retVal[key] = value
    return retVal


# caution: using it as if it were mutable
def parseList(contact):
    retVal = list()
    for n in contact:
        if n:
            value = n
            if(isIterable(value)):
                value = mapfunc(value)
            retVal = retVal + [value]
    return retVal

def mapfunc(contact):
    if isinstance(contact, dict):
        return parseDict(contact)
    elif isinstance(contact, list):
        return parseList(contact)
    else:
        print('Error: not list or dict, somhow. :(')

# curl -X POST -H 'X-API-TOKEN: <API Token>' -H "Content-Type: application/json"  --data @contacts.json  'https://co1.qualtrics.com/API/v3/mailinglists/CG_6F1gRt186CZOVoh/contactimports'
# https://api.qualtrics.com/reference#create-contacts-import
# IMPORTANT: must eliminate all falsy field values before reuploading to qualtrics via api, otherwise it will err
def putList(config, apiUrl, targetList, updatedList):
    newUrl = apiUrl + targetList['id'] + '/contactimports'
    putHook(updatedList)
    headers = {
        'x-api-token': config['apiToken'],
        'content-type': 'application/json'
    }
    mappedContacts = map(mapfunc, updatedList)
    formatted = {
        "contacts": list(mappedContacts)
    }
    jsonString = json.dumps(formatted, indent = 4)
    response = requests.post(url = newUrl, data = jsonString, headers = headers)
    return response.json()

# https://api.qualtrics.com/reference#section-generate-distribution-links
# used to generate distribution link to a survey
def genSurveyLinks():
    pass

# https://api.qualtrics.com/reference#section-generate-distribution-links
# used to retrieve the generated links
def getSurveyLinks():
    pass

if __name__ == "__main__":
    # print(CONFIG['apiUrl'])
    # print(validators.url('asdf'))
    # print()
    # getLists()
    # the above can be uncommented for testing/debugging purposes
    pass