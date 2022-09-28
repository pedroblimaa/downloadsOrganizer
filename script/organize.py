import src.organizeManager as om
import src.languageManager as lm
import src.verify as verify
import os
import sys
from os.path import expanduser



def main():

    args = getArgs()

    if len(args) != 1:
        raise Exception("Invalid number of arguments")

    folderNames = getFoldersNames(args)

    home = expanduser("~")
    path = home + "\\Downloads"

    if isOrganized(path):
        raise Exception("Already organized, please undo first")

    files = os.listdir(path)
    om.createFolders(files, path, folderNames)
    om.organize(files, path, folderNames)

def getArgs():
    return sys.argv[1:]

def getFoldersNames(args):
    language = args[0]
    return lm.getFoldersByLanguage(language)

def isOrganized(path):
    return verify.verifyOrganizationLanguage(os.listdir(path))

if __name__ == "__main__":
    main()
