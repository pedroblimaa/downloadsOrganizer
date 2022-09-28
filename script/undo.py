import src.undoManager as um
import src.verify as verify
import src.consts as c
import src.languageManager as lm
import os
from os.path import expanduser


def main():

    home = expanduser("~")
    path = home + "\\Downloads"

    folders = getCurrentFoldersNames(path)

    if folders == None:
        raise Exception("No current organization found to undo")

    um.undo(path, folders)


def getCurrentFoldersNames(path):
    foldersLanguage = verify.verifyOrganizationLanguage(os.listdir(path))

    return lm.getFoldersByLanguage(foldersLanguage)



if __name__ == "__main__":
    main()
