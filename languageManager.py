import consts as const

def getFoldersNamesByLanguage(language = 'pt'):
    if language == 'en':
        return const.folders
    else:
        return const.foldersPort
