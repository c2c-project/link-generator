# QUALTRICS API
import requests
import json
from urllib.parse import urlparse
import validators
import pprint

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
def getContacts(config, apiUrl, targetListID):
    headers = {
        'x-api-token': config['apiToken']
    }
    url = apiUrl + targetListID + '/' + 'contacts'
    response = requests.get(url, headers = headers)
    return response.json()['result']['elements']

# runs any put hooks before the actual put requests, such as generate a backup
def putHook():
    pass

def putList():
    pass


if __name__ == "__main__":
    # print(CONFIG['apiUrl'])
    # print(validators.url('asdf'))
    # print()
    # getLists()
    pass