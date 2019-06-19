# PARSES CONFIG
import json
import os
import warnings
from pathlib import Path

CONFIG_PATH = os.path.realpath(os.path.dirname(__file__) + '/../config.json')
CONFIG = dict()

def parse():
    myFile = Path(CONFIG_PATH)
    if myFile.is_file():
        global CONFIG
        with open(CONFIG_PATH) as f:
            CONFIG = json.load(f)
    else:
        print('No config file found. Make sure `config.json` is in the root directory. Exiting...')
        print('Generic Hint: Check file name case.')
        exit()

def config():
    parse()
    return CONFIG

# used for testing when running by itself
if __name__ == '__main__':
    # test with valid data
    parse()
    print(CONFIG)

    # test invalid data
    CONFIG_PATH = 'invalid-path.txt'
    parse()
    print(CONFIG) # should never get here
