import filesManager as fm
from os.path import expanduser
import os



def main():
    home = expanduser("~")
    path = home + "\\Downloads"

    files = os.listdir(path)
    fm.createFolders(files, path)
    fm.moveFiles(files, path)


if __name__ == "__main__":
    main()
