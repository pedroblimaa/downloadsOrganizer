import os
from os.path import expanduser

import src.modules.languageManager as lm
import src.modules.undoManager as um
import src.utils.consts as c
import src.utils.verify as verify


def exec():

    home = expanduser("~")
    path = home + "\\Downloads"

    folders = getCurrentFoldersNames(path)

    if folders == None:
        raise Exception("No current organization found to undo")

    um.undo(path, folders)


def getCurrentFoldersNames(path):
    files = os.listdir(path)
    foldersLanguage = verify.verifyOrganizationLanguage(files)

    if foldersLanguage:
        return lm.getFoldersByLanguage(foldersLanguage)

    return getExistingOrganizationFolders(files)


def getExistingOrganizationFolders(files):
    existingFolders = []

    for language in c.foldersLanguages:
        for folderName in language['names']:
            if folderName in files and folderName not in existingFolders:
                existingFolders.append(folderName)

    if len(existingFolders) == 0:
        return None

    return existingFolders
