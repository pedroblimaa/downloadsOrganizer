import src.utils.consts as c

def getFoldersByLanguage(language):
    for folder in c.foldersLanguages:
        if folder['language'] == language:
            return folder['names']