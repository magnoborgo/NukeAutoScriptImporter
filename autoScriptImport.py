# Boundary Visual Effects - Automatic script importer from a folder
# Version 1.0
# Compatibility: Nuke 6.3 and up (not tested on previous versions)
#
#
# If you like it and use it frequently, please consider a small donation to the author,
# via Paypal on the email mborgo[at]boundaryvfx.com

#===============================================================================
# This action will help you quickly import .nk scripts from a folder into your current project
#
# This script will load all .nk files into the current open project.
# Use it to import shapes from silhouette, trackers and etc from other softwares.
# The ideia is to place .nk files in a temporary folder and get rid of them after importing
#===============================================================================

#===============================================================================
# Version Log
# v1 (2012/10/01)

# Copyright (c) 2012, Magno Borgo
# All rights reserved.
#
# BSD-style license:
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Magno Borgo or its contributors may be used to
#        endorse or promote products derived from this software without
#        specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
#BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
#OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
#OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#===============================================================================
# Instructions to use
#===============================================================================
# Set up the default import folder path on init.py or menu.py with the code below:
#
# os.environ['AUTOSCRIPTIMPORTPATH'] = '/path/to/your/folder'
#
# run the script AutoImportScripts() to load all the files.
# IF you want the files on the folder to be DELETED after importing use AutoImportScripts(False)
#
# I recommend using it with a keyboard shortcut, which you can setup with something like this on manu.py
# ATTENTION: the False below will delete all the .nk files on the folder after importing them
'''
toolbar = nuke.menu("Nodes")
bvfxt = toolbar.addMenu("BoundaryVFX Tools")
bvfxt.addCommand('AutoScriptImport','AutoScriptImport(False)','F9', icon='bvfx_AutoImport.png')
'''
# Another  nice way to load files is to use the code below on the menu.py or ini.py, everytime you save the project
# it will load the scripts and delete the files.
#
'''
nuke.addOnScriptSave(AutoScriptImport, False)
'''
#===============================================================================



import os, nuke

def AutoScriptImport(keep=True):
    path = os.getenv('AUTOSCRIPTIMPORTPATH')
    #set the path manually below if you do not want to use env variables
    #path = "path/to/the/folder"
    if path == None:
        msg = "AutoScriptPath path not set!, use:\nos.environ['AUTOIMPORTPATH'] = '/path/to/your/folder' on menu.py"
        if nuke.GUI:
            nuke.message(msg)
        raise TypeError(msg)
    if not os.path.exists(path):
        msg =  'AutoScriptPath do not exists: ' + path
        if nuke.GUI:
            nuke.message(msg)
        raise TypeError(msg)
    dirList=os.listdir(path)
    for fname in dirList:
        ext = os.path.splitext(fname)
        if ext[1] == ".nk":
            nuke.scriptReadFile(path+fname)
            if not keep: #delete the files
                os.remove(os.path.join(path,fname))