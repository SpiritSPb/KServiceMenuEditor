#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By ShiJingchang at 2015.11.12
# To ensure KDE Service Menu Editor can run without additional operations by end users. I just add some Python lines in this file to move UI files.
# KDE Service Menu Editor is writen by David Edmundson. Its project website is: http://blog.davidedmundson.co.uk/node/3 or http://kde-apps.org/content/show.php?content=85062&forumpage=0

import os

# Get the directory UI files should be located.
print 'You must ensure the command kde4-config can run in terminal!'
GlobalSearchPath = os.popen('kde4-config --path data').readlines()
UserHomeSearchPathRepo = ''.join(GlobalSearchPath)
UserHomeSearchPathRepo = UserHomeSearchPathRepo.split(':')
UserHomeSearchPath = UserHomeSearchPathRepo[0]
KServiceMenuEditorDirName = 'kservicemenueditor'
KServiceMenuEditorDirPath = UserHomeSearchPath + KServiceMenuEditorDirName

# Make the directory UI files should be located.
FlagRun = os.mkdir(KServiceMenuEditorDirPath)
if FlagRun is None:
    pass
else:
    print 'Make directory failed!'

MoveUIFilesCommand = 'mv *.ui ' + KServiceMenuEditorDirPath
FlagRun = os.system(MoveUIFilesCommand)
if FlagRun != 0:
    print ['Error: Move UI files failed!']
else:
    print 'UI files are placed in the right place. You can run this program now!'
