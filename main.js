const { app, BrowserWindow } = require('electron')
const path = require('path')

const createWindow = () => {
  const win = getBrowserWindow()
  win.loadFile('src/index.html')

  win.on('closed', () => {
    mainWindow = null
  })
}

const getBrowserWindow = () => {
  return new BrowserWindow({
    width: 1200,
    height: 440,
    frame: false,
    webPreferences: {
      contextIsolation: false,
      nodeIntegration: true,
      devTools: true,
      preload: path.join(__dirname, 'src/js/preload.js'),
    },
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (mainWindow === null) createWindow()
})
