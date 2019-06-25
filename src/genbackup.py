import qapi
import json
# generates backup before any put operation
def backup(backupTarget):
    with open('backup.txt', 'w') as f:
        json.dump(backupTarget, f)
