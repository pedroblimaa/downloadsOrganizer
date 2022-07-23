from fileinput import filename
import consts as c
import os


def createFolders(files, path):
    for folder in c.folders:
        if not folder in files:
            os.mkdir(path + "\\" + folder)


def organize(files, path):

    for file in files:
        handleFileTransference(file, path)

        fileWasMoved = not (file in os.listdir(path))
        if (not fileWasMoved) and (isNotCategoryFolder(file)):
            moveToFolder(path, "other", file)


def handleFileTransference(file, path):
    for folder in c.folders:
        if file.endswith(c.foldersName[folder]):
            moveToFolder(path, folder, file)


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


def isNotCategoryFolder(file):
    return not(file in c.folders)
