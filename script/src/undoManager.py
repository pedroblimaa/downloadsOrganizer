import os
import src.consts as c

def undo(path, foldersNames):
    downloadItems = os.listdir(path)
    for item in downloadItems:
        if item in foldersNames:
            removeAllItemsFromFolder(path, item)
            os.rmdir(path + "\\" + item)

def removeAllItemsFromFolder(path, folder):
    folderPath = path + "\\" + folder
    folderItems = os.listdir(folderPath)
    for item in folderItems:
        os.rename(folderPath + "\\" + item, path + "\\" + item)