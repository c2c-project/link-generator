# Instructions
-  Install Python 3
-  Install any other necessary libraries, non-standard ones are:
   -  [furl](https://github.com/gruns/furl)
   -  [validators](https://github.com/kvesteri/validators)
# Other Pre-Reqs
You must have a valid `config.json` in the root directory.  There is an `exampleconfig.json` in the root directory. 

__NOTE__: the trailing `/` in any url should be present, if one is needed.
# Run
- From the root directory, run `python src/c2cshell.py`, this may need to be `python3 src/c2cshell.py` depending on your install.
- Type `?` or `help` to list all commands.  Type `help <command>` for help with a particular command.

# Commands
- `list`: Show all contact lists from Qualtrics
- `show`: Show currently selected list
- `select <#>`: Select a list for manipulation
- `upload`: Upload generated links; must do after you select a contact list
- `backup`: Generate a backup.txt and backup.csv with corresponding generated links, using the currently selected list.
 __NOTE__: backup.* is always overwritten with each `backup` invocation

# Example
The current ideal way to use this is as follows:
- Type `list`
- Type `select <# of option you wish to choose>` Ex. `select 0`
- Type `upload`

Links and a backup file named `backup.txt` & `backup.csv` are automatically made before the upload is invoked.
The new generated url is in a field named `sessionUrl`.

# TODO
- Nothing at this time.
