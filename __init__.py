import filesManager as fm
import os


def main():
    path = "C:\\Users\\Pedro\\Downloads"
    files = os.listdir(path)
    fm.createFolders(files, path)
    fm.moveFiles(files, path)


if __name__ == "__main__":
    main()
