import consts as c
import os


def createFolders(files, path):
    for folder in c.folders:
        if not folder in files:
            os.mkdir(path + "\\" + folder)


def moveFiles(files, path):
    print("Moving files...")
    for file in files:
        for folder in c.folders:
            if file.endswith(c.foldersName[folder]):
                filePath = path + "\\" + folder + "\\" + file
                if os.path.exists(filePath):
                    os.remove(filePath)
                os.rename(
                    path + "\\" + file,
                    path + "\\" + folder + "\\" + file,
                )
        if os.path.isdir(path + "\\" + file) and (not file in c.folders):
            print("Folder: " + file)
            os.rename(
                path + "\\" + file,
                path + "\\other\\" + file,
            )
