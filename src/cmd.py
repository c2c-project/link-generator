# IMPLEMENTS ALL MODULES & IS A CLI

# python lib imports
import cmd
# module imports
import qapi


def mainInterface():
    pass

def selectPrompt():
    elements = qapi.getLists()
    print('{3:<10} {0:<40} {1:<40} {2:<40}'.format('name', 'category', 'folder', '#'))
    # cList = contactList dict
    for index,cList in enumerate(elements):
        print('{1:<10} {0[name]:<40} {0[category]:<40} {0[folder]:<40}'.format(cList, index))


if __name__ == "__main__":
    selectPrompt()

    pass