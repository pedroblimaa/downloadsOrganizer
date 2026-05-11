import os
import shutil


def undo(path, foldersNames):
    failedItems = []
    downloadItems = os.listdir(path)

    for item in downloadItems:
        if item in foldersNames:
            folderFailures = removeAllItemsFromFolder(path, item)
            failedItems.extend(folderFailures)
            removeFolderIfEmpty(path, item)

    if failedItems:
        raise Exception(
            "Could not move these items because Windows denied access: "
            + ", ".join(failedItems)
            + ". Close any apps using them and try Undo again."
        )


def removeAllItemsFromFolder(path, folder):
    folderPath = os.path.join(path, folder)
    folderItems = os.listdir(folderPath)
    failedItems = []

    for item in folderItems:
        sourcePath = os.path.join(folderPath, item)
        targetPath = getAvailableTargetPath(path, item)

        try:
            shutil.move(sourcePath, targetPath)
        except PermissionError:
            failedItems.append(os.path.join(folder, item))

    return failedItems


def removeFolderIfEmpty(path, folder):
    folderPath = os.path.join(path, folder)

    if len(os.listdir(folderPath)) == 0:
        os.rmdir(folderPath)


def getAvailableTargetPath(path, item):
    targetPath = os.path.join(path, item)

    if not os.path.exists(targetPath):
        return targetPath

    baseName, extension = os.path.splitext(item)
    duplicatedFileNumber = 1

    while True:
        newName = baseName + "(" + str(duplicatedFileNumber) + ")" + extension
        targetPath = os.path.join(path, newName)

        if not os.path.exists(targetPath):
            return targetPath

        duplicatedFileNumber += 1
