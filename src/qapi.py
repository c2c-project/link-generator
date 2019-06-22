# QUALTRICS API
import requests
import json
from parseconfig import config
from urllib.parse import urlparse
import validators
import pprint

TARGET_LIST_ID = None
CONFIG = config()

# https://api.qualtrics.com/reference#list-mailing-lists
# url to list all mailing lists so user can select them
API_URL = CONFIG['rootUrl'] + 'mailinglists'

# https://api.qualtrics.com/reference#list-contacts
# curl -H 'X-API-TOKEN: yourtokenhere' 'https://yourdatacenterid.qualtrics.com/API/v3/mailinglists'
def getLists():
    headers = {
        'x-api-token': CONFIG['apiToken']
    }
    response = requests.get(API_URL, headers=headers)
    return response.json()['result']['elements']
    

# runs any put hooks before the actual put requests, such as generate a backup
def putHook():
    pass

def putList():
    pass


if __name__ == "__main__":
    print(CONFIG['rootUrl'])
    print(validators.url('asdf'))
    print()
    getLists()