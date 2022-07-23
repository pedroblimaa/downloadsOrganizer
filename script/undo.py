import src.undoManager as um
from os.path import expanduser


def main():

    home = expanduser("~")
    path = home + "\\Downloads"

    um.undo(path)


if __name__ == "__main__":
    main()
