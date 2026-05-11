const { execFile } = require('child_process')
const fs = require('fs')
const path = require('path')

let notificationTimeout

document.getElementById('organize-btn').addEventListener('click', function () {
  const language = getLanguage()
  runOrganizer(['organize', language])
})

document.getElementById('undo-btn').addEventListener('click', function () {
  runOrganizer(['undo'])
})

function runOrganizer(args) {
  const packagedOrganizerPath = getPackagedOrganizerPath()

  if (fs.existsSync(packagedOrganizerPath)) {
    runCommand(packagedOrganizerPath, args)
    return
  }

  runPythonScript(args)
}

function getPackagedOrganizerPath() {
  return path.join(process.resourcesPath, 'downloads_organizer.exe')
}

function runPythonScript(args) {
  const scriptPath = path.resolve('script', 'downloads_organizer.py')
  const commands = ['py', 'python', 'python3']

  runPythonCommand(commands, scriptPath, args)
}

function runPythonCommand(commands, scriptPath, args) {
  const command = commands.shift()

  if (!command) {
    showNotification('Python is required to run this app in development. Install Python or run the packaged app.', 'error')
    return
  }

  runCommand(command, [scriptPath, ...args], function (err) {
    if (err && err.code === 'ENOENT') {
      runPythonCommand(commands, scriptPath, args)
      return
    }

    handleScriptReturn(err)
  })
}

function runCommand(command, args, callback) {
  execFile(command, args, function (err) {
    console.log('Running organizer')

    if (callback) {
      callback(err)
      return
    }

    handleScriptReturn(err)
  })
}

function handleScriptReturn(err) {
  if (err) {
    showNotification(getErrorMessage(err), 'error')
    throw err
  }

  showNotification('Downloads organized successfully!', 'success')
}

function showNotification(message, type) {
  const notification = document.getElementById('notification')
  const notificationMessage = document.getElementById('notification-message')

  clearTimeout(notificationTimeout)

  notificationMessage.textContent = message
  notification.className = `notification notification-${type} visible`

  notificationTimeout = setTimeout(function () {
    notification.classList.remove('visible')
  }, type === 'error' ? 7000 : 3500)
}

function getErrorMessage(err) {
  return err.stderr || err.message
}

function getLanguage() {
  const activeBtn = document.querySelector('.active')

  return activeBtn.id
}
