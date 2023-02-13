from fileinput import filename
import src.utils.consts as c
import os


def createFolders(files, path, folderNames):
    for folderName in folderNames:
        if not folderName in files:
            os.mkdir(path + "\\" + folderName)


def organize(files, path, folderNames):

    for file in files:
        handleFileTransference(file, path, folderNames)

        fileWasMoved = not (file in os.listdir(path))
        if (not fileWasMoved) and (isNotCategoryFolder(file, folderNames)):
            moveToFolder(path, folderNames[-1], file)


def handleFileTransference(file, path, folderNames):
    for folderName in folderNames:
        if file.endswith(getExtensionsByFolders(folderNames, folderName)):
            moveToFolder(path, folderName, file)


def getExtensionsByFolders(folders, folder):
    index = folders.index(folder)
    extensionsList = [c.documents, c.media, c.compressed, c.installer, c.other]

    return extensionsList[index]


def moveToFolder(path, folder, file):
    duplicatedFileNumber = 0

    handleFileRename(path, folder, file, file, duplicatedFileNumber)


def handleFileRename(path, folder, file, newName, duplicatedFileNumber):
    duplicatedFileNumber += 1

    try:
        os.rename(
            path + "\\" + file,
            path + "\\" + folder + "\\" + newName,
        )
    except FileExistsError:
        handleFileRename(
            path,
            folder,
            file,
            renameFile(file, duplicatedFileNumber),
            duplicatedFileNumber
        )
    except PermissionError:
        print("Permission error: " + file)


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


def isNotCategoryFolder(file, folderNames):
    return not (file in folderNames)
