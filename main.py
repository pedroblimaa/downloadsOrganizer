import filesManager as fm
from os.path import expanduser
import os

def main():
    print("Moving files...")

    home = expanduser("~")
    path = home + "\\Downloads"

    fileNames = os.listdir(path)
    fm.prepareFolders(fileNames, path)
    fm.createFolders(fileNames, path)
    fm.organize(fileNames, path)

    print("Done!")
    input("Press enter to exit...")

if __name__ == "__main__":
    main()