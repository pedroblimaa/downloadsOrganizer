from fileinput import filename
import languageManager as lm
import consts as c
import os

foldersNames = lm.getFoldersNamesByLanguage('pt')


def createFolders(files, path):
    for folder in foldersNames:
        if not folder in files:
            os.mkdir(path + "\\" + folder)


def organize(files, path):

    for file in files:
        handleFileTransference(file, path)

        fileWasMoved = not (file in os.listdir(path))
        if (not fileWasMoved) and (isNotCategoryFolder(file)):
            moveToFolder(path, "other", file)


def prepareFolders(files, path):

    otherLanguageFolderNames = getOtherLanguageFolderNames()

    for folderLanguage in otherLanguageFolderNames:
        isOrganized = verifyIfDownloadsIsOrganized(folderLanguage, files)
        if isOrganized:
            revertOrganization(folderLanguage, path)
            deleteFolder(folderLanguage, path)

def deleteFolder(folderLanguage, path):
    os.rmdir(path + "\\" + folderLanguage)

def revertOrganization(folderLanguage, path):
    for folder in folderLanguage:
        removeFilesFromFolder(folder, path)


def removeFilesFromFolder(folder, path):
    folderPath = path + "\\" + folder
    for file in os.listdir(folderPath):
        removeFileFromFolder(folderPath, path, file)


def removeFileFromFolder(folderPath, path, newName, duplicatedFileNumber = 0):
    duplicatedFileNumber += 1

    try:
        print('Moving' + file)
        os.rename(folderPath + "\\" + newName, path + "\\" + newName)
        print(file + ' Moved!')
    except FileExistsError:
        handleFileRename(folderPath, path,  renameFile(newName, duplicatedFileNumber),
                         duplicatedFileNumber)


def verifyIfDownloadsIsOrganized(folderLanguage, files):
    for folder in folderLanguage:
        folderHasFile = verifyIfFolderHasFile(files, folder)
        if folderHasFile == False:
            return False
    return True


def verifyIfFolderHasFile(files, folder):
    for file in files:
        if file == folder:
            return True
    return False


def getOtherLanguageFolderNames():
    otherLanguageFolderNames = []

    for folderLanguage in c.foldersLanguages:
        appendOtherFolderNames(otherLanguageFolderNames, folderLanguage)

    return otherLanguageFolderNames


def appendOtherFolderNames(otherLanguageFolderNames, folderLanguage):
    if(folderLanguage != foldersNames):
        return otherLanguageFolderNames.append(folderLanguage)


def verifyIfIsAnotherFolder(file):
    for folderLanguage in c.foldersLanguages:
        if((file in folderLanguage) and (folderLanguage != foldersNames)):
            return True


def handleFileTransference(file, path):
    for folder in foldersNames:
        if file.endswith(c.foldersExtensions[folder]):
            moveToFolder(path, folder, file)


def moveToFolder(path, folder, file):
    duplicatedFileNumber = 0

    handleFileRename(path, folder, file, file, duplicatedFileNumber)


def handleFileRename(path, folder, file, newName, duplicatedFileNumber):
    duplicatedFileNumber += 1

    try:
        os.rename(path + "\\" + file, path + "\\" + folder + "\\" + newName)
    except FileExistsError:
        handleFileRename(path, folder, file, renameFile(file, duplicatedFileNumber),
                         duplicatedFileNumber)


def renameFile(fileName, duplicatedFileNumber):
    fileNameList = fileName.rsplit('.', 1)
    duplicatedFileString = "(" + str(duplicatedFileNumber) + ")."
    return fileNameList[0] + duplicatedFileString + fileNameList[-1]


def isFileSuitableToFolders(path, file, isFolderSuitable):
    return isFolder(path, file) or not isFolderSuitable


def fileExists(filePath):
    return os.path.exists(filePath) and os.path.isfile(filePath)


def isFolder(path, file):
    return os.path.isdir(path + "\\" + file)


def isNotCategoryFolder(file):
    return not(file in foldersNames)
