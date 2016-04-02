This python script action will help you quickly import .nk scripts from a folder into your current project
===============

This script will load all .nk files into the current open project.
Use it to import shapes from Silhouette Roto and Paint, Trackers exported from matchmoving softwares and etc

The ideia is to place .nk files in a temporary folder and get rid of them after importing (deleting them automatically)


Its very specially usefull if you set it to a shortcut in Nuke's menu.py:

#### Instructions to use ####

Set up the default import folder path on init.py or menu.py with the code below:
os.environ['AUTOSCRIPTIMPORTPATH'] = '/path/to/your/folder'

It can be hardcoded on the script if you dont want to use ENV vairables (check inside script code )


run the script AutoImportScripts() to load all the files.
IF you want the files on the folder to be DELETED after importing use AutoImportScripts(False)

I recommend using it with a keyboard shortcut, which you can setup with something like this on menu.py

toolbar = nuke.menu("Nodes")
bvfxt = toolbar.addMenu("BoundaryVFX Tools")
bvfxt.addCommand('AutoScriptImport','AutoScriptImport(False)','F9')


ATTENTION: the False below will delete all the .nk files on the folder after importing them
