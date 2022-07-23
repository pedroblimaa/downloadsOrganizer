import src.organizeManager as om
from os.path import expanduser
import os


def main():

    home = expanduser("~")
    path = home + "\\Downloads"

    fileNames = os.listdir(path)
    om.createFolders(fileNames, path)
    om.organize(fileNames, path)


if __name__ == "__main__":
    main()
