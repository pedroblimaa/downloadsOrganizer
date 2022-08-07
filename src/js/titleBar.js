const { ipcRenderer } = require("electron")

const closeBtn = document.getElementById('close-btn')
const minimizeBtn = document.getElementById('min-btn')
const maximizeBtn = document.getElementById('max-btn')

closeBtn.addEventListener('click', () => {
  ipcRenderer.send('close')
})

minimizeBtn.addEventListener('click', () => {
  ipcRenderer.send('minimize')
})

maximizeBtn.addEventListener('click', () => {
  ipcRenderer.send('maximize')
})
