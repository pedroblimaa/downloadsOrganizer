# Downloads Oragnizer

Downloads Organizer is an application that helps you keep your downloads folder organized, saving you time and effort. If you have a messy downloads folder and don't want to organize it manually every time, this app is for you.

## Table of Contents

- [Introduction](#introduction)
- [Generating Installer](#generating-installer)
- [Usage](#usage)

## <a id="installation">Installation</a>

You will need Node.js to run the Electron project:
- https://nodejs.org/en/download/

To build the Windows installer, you also need Python and PyInstaller because the Python organizer is bundled as an executable during packaging:
- https://www.python.org/

```bash
py -m pip install pyinstaller
```

> Note: If you only want to use the app and do not wish to check the repository or contribute to development, you can simply extract the `Downloads Organizer Setup 0.1.0.rar` zip file and run the installer.

1. Clone the project repository:

```bash
git clone https://github.com/pedroblimaa/downloadsOrganizer.git
```

2. Navigate to the project folder:
```bash
cd downloadsOrganizer
```

3. Install the required dependencies:
```bash
pnpm install
```

## <a id="generating-installer">Generating Installer</a>

> Note: If you don't want to generate an installer, you can jump for the `Usage` section

If you want to generate the Windows installer, run the following command:
`pnpm build`

The generated installer includes the compiled organizer executable, so users who install the app do not need to install Python separately.

## <a id="usage">Usage</a>

After installation, you can start the app by running `pnpm start` or opening the generated executable application.

To organize your downloads folder, simply click the Organize button. To undo the organization, click the Undo button.

That's it! Enjoy your newly organized downloads folder.
