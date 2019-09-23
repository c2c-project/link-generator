import json
import csv
# generates backup before any put operation
def backup(backupTarget):
    gentxt(backupTarget)
    gencsv(backupTarget)

def gentxt(backupTarget):
    with open('backup.txt', 'w') as f:
        json.dump(backupTarget, f)

def gencsv(backupTarget):
    # print(backupTarget)
    keys = list()
    initialHeaders = ['id','firstName', 'lastName', 'email', 'externalDataReference', 'language']
    qHeaders = ['RecipientID','FirstName', 'LastName', 'PrimaryEmail', 'ExternalDataReference', 'Language']
    with open('backup.csv', 'w') as f:
        csvwriter = csv.writer(f)

        # find all possible embedded data fields first, must looop through all b/c fields may not be consistent
        for contact in backupTarget:
            if contact['embeddedData']:
                for key in list(contact['embeddedData'].keys()):
                    if key not in initialHeaders and key not in keys:
                        keys = keys + [key]
        headers = initialHeaders + keys
        printedHeaders = qHeaders + keys
        # write header row
        csvwriter.writerow(printedHeaders)

        for contact in backupTarget:
            # must do this to maintain order integrity
            # print(contact)
            row = list()
            for key in headers:
                if key in contact and contact[key]:
                    row = row + [contact[key]]
                elif key in contact['embeddedData'] and contact['embeddedData'][key]:
                    row = row + [contact['embeddedData'][key]]
                else:
                    row = row + ['']
            # print(row)
            csvwriter.writerow(row)

def genLinkInfo(backupTarget):
        # print(backupTarget)
    keys = list()
    initialHeaders = ['id', 'First_Name', 'Last_Name', 'sessionUrl']
    qHeaders = ['RecipientID','First_Name', 'Last_Name', 'sessionUrl']
    with open('backup_links.csv', 'w') as f:
        csvwriter = csv.writer(f)

        # find all possible embedded data fields first, must looop through all b/c fields may not be consistent
        # for contact in backupTarget:
        #     if contact['embeddedData']:
        #         for key in list(contact['embeddedData'].keys()):
        #             if key not in initialHeaders and key not in keys:
        #                 keys = keys + [key]
        headers = initialHeaders + keys
        printedHeaders = qHeaders + keys
        # write header row
        csvwriter.writerow(printedHeaders)

        for contact in backupTarget:
            # must do this to maintain order integrity
            # print(contact)
            row = list()
            for key in headers:
                if key in contact and contact[key]:
                    row = row + [contact[key]]
                elif key in contact['embeddedData'] and contact['embeddedData'][key]:
                    row = row + [contact['embeddedData'][key]]
                else:
                    row = row + ['']
            # print(row)
            csvwriter.writerow(row)