import os
from os.path import expanduser

import src.modules.languageManager as lm
import src.modules.undoManager as um
import src.utils.verify as verify


def exec():

    home = expanduser("~")
    path = home + "\\Downloads"

    folders = getCurrentFoldersNames(path)

    if folders == None:
        raise Exception("No current organization found to undo")

    um.undo(path, folders)


def getCurrentFoldersNames(path):
    foldersLanguage = verify.verifyOrganizationLanguage(os.listdir(path))

    return lm.getFoldersByLanguage(foldersLanguage)