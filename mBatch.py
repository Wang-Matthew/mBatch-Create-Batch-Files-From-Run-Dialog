#!python3
#mBatch.py

import os, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    file2Convert = sys.argv[1]
else:
    file2Convert = pyperclip.paste()

withoutPyExt = file2Convert[:-3]

currentPath = ('C:\\PathOfWhereverYouPutYourPythonFiles\\' + withoutPyExt + '.bat')

newBatchFile = open(currentPath, 'w')
newBatchFile.write('@py.exe C:\\PathOfWhereverYouPutYourPythonFiles\\' + file2Convert + ' %*')
newBatchFile.close()
