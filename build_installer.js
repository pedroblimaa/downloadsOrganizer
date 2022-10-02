const { MSICreator } = require('electron-wix-msi')
const path = require('path')

//Create a bundled installer to install python before the app
const msiCreator = new MSICreator({
  appDirectory: path.resolve(__dirname, './dist/downloads-organizer-win32-x64'),
  outputDirectory: path.resolve(__dirname, './dist/installer'),
  description: 'An Organizer for your files in Downloads folder',
  exe: 'downloads-organizer',
  name: 'Downloads Organizer',
  appIconPath: path.resolve(__dirname, './src/assets/icon.ico'),
  manufacturer: 'Pedro Bonfilio Lima',
  version: '1.0.0',
  appIconPath: path.resolve(__dirname, './src/assets/icon.ico'),
  ui: {
    chooseDirectory: true,
  },
})

msiCreator.create().then(function () {
  msiCreator.compile()
})
