documents = (".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")
media = (".mp4", ".avi", ".mp3", ".mkv", ".flv", ".wmv", ".mov", ".mpg", ".mpeg", ".jpeg", ".jpg", ".png", ".gif", ".ico")
compressed = (".zip", ".rar", ".7z")
installer = (".exe", ".msi")
other = ()
languages = ("pt-br", "en-us")

foldersName = {
    "documents": documents,
    "media": media,
    "compressed": compressed,
    "installer": installer,
    "other": other,
}

foldersLanguages = (
    {
        "language": "original",
        "names": ("documents", "media", "compressed", "installer", "other")
    },
    {
        "language": 'pt-br',
        "names": ("Documentos", "Midia", "Zips", "Instaladores", "Outros")
    },
    {
        "language": 'en-us',
        "names": ("Documents", "Media", "Zips", "Installers", "Other")
    },
)