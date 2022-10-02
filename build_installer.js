const { MSICreator } = require('electron-wix-msi');
const path = require('path');

const APP_DIR = path.resolve(__dirname, './dist/win-unpacked');
const OUT_DIR = path.resolve(__dirname, './dist/installer');

console.log(path.resolve(__dirname, './src/assets'));

const msiCreator = new MSICreator({
    appDirectory: APP_DIR,
    outputDirectory: OUT_DIR,
    description: 'An Organizer for your files in Downloads folder',
    exe: 'Downloads Organizer',
    name: 'Downloads Organizer',
    appIconPath: path.resolve(__dirname, './src/assets/icon.ico'),
    manufacturer: 'Pedro Bonfilio Lima',
    version: '1.0.0',
    ui: {
        chooseDirectory: true,
    },
});

msiCreator.create().then(function () {
    msiCreator.compile();
});