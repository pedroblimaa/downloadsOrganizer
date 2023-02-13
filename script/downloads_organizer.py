import sys
import src.organize as organize
import src.undo as undo


def main():
    args = getArgs()

    if len(args) < 1 or len(args) > 2:
        raise Exception(
            "Invalid number of arguments. Usage: py downloads_organizer.py <desired_action=mandatory> <language=only for oganize>. Args received: " + str(args))

    if args[0] == "organize":
        organize.exec(args[1:])
    elif args[0] == "undo":
        undo.exec()
    else:
        raise Exception(
            "Invalid action. Usage: py downloads_organizer.py <desired_action=mandatory> <language=only for oganize>... The desired action can be 'organize' or 'undo'")


def getArgs():
    return sys.argv[1:]


if __name__ == "__main__":
    main()
