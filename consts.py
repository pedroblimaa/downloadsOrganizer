documents = (".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")
media = (".mp4", ".avi", ".mp3", ".mkv", ".flv", ".wmv", ".mov", ".mpg", ".mpeg", ".jpeg", ".jpg", ".png", ".gif", ".ico")
compressed = (".zip", ".rar", ".7z")
installer = (".exe", ".msi")
other = ()
folders = ("Documents", "Media", "Compressed", "Installer", "Other")
foldersPort = ("Documentos", "Media", "Comprimidos", "Instaladores", "Outros")

foldersLanguages = [folders, foldersPort]

foldersExtensions = {
    "documents": documents,
    "media": media,
    "compressed": compressed,
    "installer": installer,
    "other": other,
}