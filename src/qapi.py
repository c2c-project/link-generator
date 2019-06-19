# QUALTRICS API
import requests
import json
from parseconfig import config
from urllib.parse import urlparse

TARGET_LIST_ID = None
CONFIG = config()
API_URL = CONFIG['rootUrl'] + 'mailinglists'

def getLists():

    pass

def modifyList():
    pass

def setTarget():
    pass

def getTarget():
    pass

if __name__ == "__main__":
    print(CONFIG['rootUrl'])