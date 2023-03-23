# Downloads Oragnizer

Downloads Organizer is an application that helps you keep your downloads folder organized, saving you time and effort. If you have a messy downloads folder and don't want to organize it manually every time, this app is for you.

## Table of Contents

- [Introduction](#introduction)
- [Generating Installer](#generating-installer)
- [Usage](#usage)

## <a id="installation">Installation</a>

You will only need node.js and python in order to run the project:
- https://nodejs.org/en/download/
- https://www.python.org/

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
npm install
```

## <a id="generating-installer">Generating Installer</a>

#### If you don't want to generate an installer, you can jump for the `Usage` section

If you want to generate the win app run the foollowing command:
`npm run dist` or `yarn dist` for yarn

If you want to generate the installer run the following command:
`npm run build`

## <a id="usage">Usage</a>

After installation, you can start the app by running `npm run start` or `yarn start` or opening the generated executable application.

To organize your downloads folder, simply click the Organize button. To undo the organization, click the Undo button.

That's it! Enjoy your newly organized downloads folder.
