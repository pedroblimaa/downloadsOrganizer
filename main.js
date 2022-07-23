const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = getBrowserWindow()
  win.loadFile('index.html')

  win.webContents.openDevTools()

  win.on('closed', () => {
    mainWindow = null
  })
}

const getBrowserWindow = () => {
  return new BrowserWindow({
    width: 1200,
    height: 440,

    webPreferences: {
      // --- !! IMPORTANT !! ---
      // Disable 'contextIsolation' to allow 'nodeIntegration'
      // 'contextIsolation' defaults to "true" as from Electron v12
      contextIsolation: false,
      nodeIntegration: true,
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
