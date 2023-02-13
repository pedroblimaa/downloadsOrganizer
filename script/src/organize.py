import os
from os.path import expanduser

import src.modules.languageManager as lm
import src.modules.organizeManager as om
import src.utils.verify as verify


def exec(args):

    if len(args) != 1:
        raise Exception("Invalid number of arguments, Usage: py downloads_organizer.py organize <language>... The language can be 'pt' or 'en")

    folderNames = getFoldersNames(args)

    home = expanduser("~")
    path = home + "\\Downloads"

    if isOrganizedWithDifferentLanguage(path, args[0]):
        raise Exception(
            "Already organized with a different language, please undo first")

    files = os.listdir(path)
    om.createFolders(files, path, folderNames)
    om.organize(files, path, folderNames)

def getFoldersNames(args):
    language = args[0]
    return lm.getFoldersByLanguage(language)


def isOrganizedWithDifferentLanguage(path, organizingLanguage):
    organizationLanguage = verify.verifyOrganizationLanguage(os.listdir(path))
    return organizationLanguage and organizationLanguage != organizingLanguage