import consts as c
import os


def createFolders(files, path):
    for folder in c.folders:
        if not folder in files:
            os.mkdir(path + "\\" + folder)


def moveFiles(files, path):
    print("Moving files...")
    for file in files:
        hasFolder = False
        for folder in c.folders:
            if file.endswith(c.foldersName[folder]):
                moveFile(path, folder, file)
                hasFolder = True
        if (os.path.isdir(path + "\\" + file) or  not hasFolder) and (not file in c.folders):
            moveFile(path, "other", file)
    print("Done!")
    input("Press enter to exit...")


def moveFile(path, folder, file):
    filePath = path + "\\" + folder + "\\" + file
    if os.path.exists(filePath) and os.path.isfile(filePath):
        os.remove(filePath)
    os.rename(
        path + "\\" + file,
        path + "\\" + folder + "\\" + file,
    )
