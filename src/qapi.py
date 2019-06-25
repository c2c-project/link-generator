# QUALTRICS API
import requests
import json
from urllib.parse import urlparse
import validators
import pprint
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
def getContacts(config, apiUrl, targetList):
    headers = {
        'x-api-token': config['apiToken']
    }
    url = apiUrl + targetList['id'] + '/contacts'
    print(url)
    response = requests.get(url, headers = headers)
    return response.json()['result']['elements']

# runs any put hooks before the actual put requests, such as generate a backup
def putHook(updatedList):
    genbackup.backup(updatedList)

# curl -X POST -H 'X-API-TOKEN: <API Token>' -H "Content-Type: application/json"  --data @contacts.json  'https://co1.qualtrics.com/API/v3/mailinglists/CG_6F1gRt186CZOVoh/contactimports'
# https://api.qualtrics.com/reference#create-contacts-import
def putList(config, apiUrl, targetList, updatedList):
    newUrl = apiUrl + targetList['id'] + '/contactimports'
    print(newUrl)
    putHook(updatedList)
    headers = {
        'x-api-token': config['apiToken'],
        'content-type': 'application/json'
    }
    formatted = {
        "contacts": updatedList
    }
    print(formatted)
    jsonString = json.dumps(formatted)
    response = requests.post(url = newUrl, data = jsonString, headers = headers)
    print(response.json())
    pass


if __name__ == "__main__":
    # print(CONFIG['apiUrl'])
    # print(validators.url('asdf'))
    # print()
    # getLists()
    # the above can be uncommented for testing/debugging purposes
    pass