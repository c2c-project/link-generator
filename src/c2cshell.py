# IMPLEMENTS ALL MODULES & IS A CLI

# python lib imports
import cmd,sys
# module imports
import qapi
from parseconfig import config
import genlink

CONFIG = config()
API_URL = CONFIG['apiUrl'] + 'mailinglists/'
REG_URL = CONFIG['regUrl']

class C2CShell(cmd.Cmd):
    intro = 'Welcome to C2CShell. Type help or ? to list commands.'
    prompt = '(C2CShell) > '

    def __init__(self):
        super(C2CShell, self).__init__()
        self.targetList = None
        self.contactLists = None
    
    def do_upload(self, *args):
        'Upload generated links; must do after you select a contact list'
        if self.targetList == None:
            print('You must select a target list first! Type `list` then `select <list # you want>`')
        else:
            contacts = qapi.getContacts(CONFIG, API_URL, self.targetList)
            withLinks = genlink.genLinks(REG_URL, contacts)
            qapi.putList(withLinks)
    
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
        print('{3:<10} {0:<40} {1:<40} {2:<40}'.format('name', 'category', 'folder', '#'))
        # cList = contactList dict
        for index,cList in enumerate(self.contactLists):
            print('{1:<10} {0[name]:<40} {0[category]:<40} {0[folder]:<40}'.format(cList, index))
        print('HINT: type `select <# of list you want to select>` to select it for further manipulation with other commands')

    def do_exit(self, *args):
        'Exit C2CShell'
        return True



if __name__ == "__main__":
    C2CShell().cmdloop()