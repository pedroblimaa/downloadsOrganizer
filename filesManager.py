import consts as c
import os

def createFolders(files):
    for folder in c.folders:
        if not folder in files:
            os.mkdir("C:\\Users\\Pedro\\Downloads\\" + folder)

def moveFiles(files, path):
    print("Moving files...")
    for file in files:
        for folder in c.folders:
            if file.endswith(c.foldersName[folder]):
                os.rename(
                    path + "\\" + file,
                    "C:\\Users\\Pedro\\Downloads\\" + folder + "\\" + file,
                )
        if os.path.isdir(path + "\\" + file) and (not file in c.folders):
            print("Folder: " + file)
            os.rename(
                path + "\\" + file,
                "C:\\Users\\Pedro\\Downloads\\other\\" + file,
            )