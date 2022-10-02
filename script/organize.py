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

    if isOrganizedWithDifferentLanguage(path, args[0]):
        raise Exception("Already organized with a different language, please undo first")

    files = os.listdir(path)
    om.createFolders(files, path, folderNames)
    om.organize(files, path, folderNames)

def getArgs():
    return sys.argv[1:]

def getFoldersNames(args):
    language = args[0]
    return lm.getFoldersByLanguage(language)

def isOrganizedWithDifferentLanguage(path, organizingLanguage):
    organizationLanguage = verify.verifyOrganizationLanguage(os.listdir(path))
    return organizationLanguage and organizationLanguage != organizingLanguage

if __name__ == "__main__":
    main()
