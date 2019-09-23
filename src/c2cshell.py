# IMPLEMENTS ALL MODULES & IS A CLI
import cmd,sys
import qapi
import parseconfig
import genlink
import genbackup

CONFIG = parseconfig.config()
API_URL = CONFIG['apiUrl'] + 'mailinglists/'
REG_URL = CONFIG['regUrl']

class C2CShell(cmd.Cmd):
    intro = 'Welcome to C2CShell. Type help or ? to list commands.'
    prompt = '(C2CShell) > '

    def __init__(self):
        super(C2CShell, self).__init__()
        self.targetList = None
        self.contactLists = qapi.getLists(CONFIG, API_URL)
        print('Loading Qualtrics Contact Lists...')

    def do_upload(self, *args):
        'Upload generated links; must do after you select a contact list'
        if self.targetList == None:
            print('You must select a target list first! Type `list` then `select <list # you want>`')
        else:
            contacts = qapi.getContacts(CONFIG, API_URL, self.targetList)
            withLinks = genlink.genLinks(REG_URL, contacts)            
            response = qapi.putList(CONFIG, API_URL, self.targetList , withLinks)
            print(response)
            print('If you see `200 - OK`, above then everything is good to go!')
    
    def do_select(self, *args):
        'Select a list for manipulation'
        index = int(args[0])
        self.targetList = self.contactLists[index]
        print('Selected list: ', self.targetList)
    
    def do_show(self, *args):
        'Show currently selected list'
        print(self.targetList)

    def do_list(self, *args):
        'Show all contact lists from Qualtrics'
        self.contactLists = qapi.getLists(CONFIG, API_URL)
        print('{3:<10} {0:<25} {1:<25} {2:<25}'.format('name', 'category', 'folder', '#'))
        # cList = contactList dict
        for index,cList in enumerate(self.contactLists):
            print('{1:<10} {0[name]:<25} {0[category]:<25} {0[folder]:<25}'.format(cList, index))
        print('HINT: type `select <# of list you want to select>` to select it for further manipulation with other commands')
    
    def do_backup(self, *args):
        'Generate a backup.txt and backup.csv with corresponding generated links, using the currently selected list.'
        if self.targetList == None:
            print('Must select a list to backup first! Type `help list`')
        else:
            contacts = qapi.getContacts(CONFIG, API_URL, self.targetList)
            withLinks = genlink.genLinks(REG_URL, contacts)
            genbackup.backup(withLinks)
            genbackup.genLinkInfo(withLinks)
            print('Look for a file named backup.csv in the root directory of the script!')

    def do_exit(self, *args):
        'Exit C2CShell'
        return True

if __name__ == "__main__":
    C2CShell().cmdloop()