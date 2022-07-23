import os
import src.consts as c

def undo(path):
    downloadItems = os.listdir(path)
    for item in downloadItems:
        if item in c.folders:
            removeAllItemsFromFolder(path, item)
            os.rmdir(path + "\\" + item)

def removeAllItemsFromFolder(path, folder):
    folderPath = path + "\\" + folder
    folderItems = os.listdir(folderPath)
    for item in folderItems:
        os.rename(folderPath + "\\" + item, path + "\\" + item)