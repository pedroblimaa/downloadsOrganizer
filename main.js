const { app, BrowserWindow, ipcMain } = require('electron')

const createWindow = () => {
  const win = getBrowserWindow()
  win.loadFile('src/index.html')

  win.openDevTools()

  ipcMain.on('close', () => {
    win.close()
  })

  ipcMain.on('minimize', () => {
    win.minimize()
  }),

  ipcMain.on('maximize', () => {
    if (win.isMaximized()) {
      win.unmaximize()
    } else {
      win.maximize()
    }
  }),

  win.on('closed', () => {
    mainWindow = null
  })
}

const getBrowserWindow = () => {
  return new BrowserWindow({
    // width: 500,
    // height: 210,
    width: 1000,
    height: 800,
    frame: false,
    webPreferences: {
      contextIsolation: false,
      nodeIntegration: true,
      devTools: true,
      enableRemoteModule: true,
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
