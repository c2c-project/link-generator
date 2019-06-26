# Instructions
-  Install Python 3
-  Install any other necessary libraries, non-standard ones are:
   -  [furl](https://github.com/gruns/furl)
   -  [validators](https://github.com/kvesteri/validators)
# Other Pre-Reqs
You must have a valid `config.json` in the root directory.  There is an `exampleconfig.json` in the root directory. 

__NOTE__: the trailing `/` in any url should be present.
# Run
- From the root directory, run `python src/c2cshell.py`, this may need to be `python3 src/c2cshell.py` depending on your install.
- Type `?` or `help` to list all commands.  Type `help <command>` for help with a particular command.

# Commands
- `list`: Show all contact lists from Qualtrics
- `show`: Show currently selected list
- `select <#>`: Select a list for manipulation
- `upload`: Upload generated links; must do after you select a contact list

# Example
The current ideal way to use this is as follows:
- Type `list`
- Type `select <# of option you wish to choose>` Ex. `select 0`
- Type `upload`

Links and a backup file named `backup.txt` are automatically made before the upload is invoked.

# TODO
- Make a backup.csv for easily reuploading the old list.
