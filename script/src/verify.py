import consts as c
from os.path import expanduser
import os

def verifyOrganizationLanguage(fileNames):
    language = ''

    for folder in c.foldersLanguages:
        isRightFolder = verifyFolderLanguageMatch(folder, fileNames)
        if isRightFolder:
            language = folder['language']
            break

    print(language)


def verifyFolderLanguageMatch(folder, fileNames):
    for folderName in folder['names']:
        folderNameMatch = verifyFolderMatch(fileNames, folderName)
        if not folderNameMatch:
            return False

    return True

def verifyFolderMatch(fileNames, folderName):
    for systemFile in fileNames:
        if systemFile == folderName:
            return True

    return False


home = expanduser("~")
path = home + "\\Downloads"

fileNames = os.listdir(path)
verifyOrganizationLanguage(fileNames)