const { PythonShell } = require('python-shell')

document.getElementById('organize-btn').addEventListener('click', function () {
  const language = getLanguage()
  runPythonScriptWithArgs('downloads_organizer', ['organize', language])
})

document.getElementById('undo-btn').addEventListener('click', function () {
  runPythonScriptWithArgs('downloads_organizer', ['undo'])
})

function runPythonScriptWithArgs(scriptName, args) {
  PythonShell.run(`./script/${scriptName}.py`, { args: args }, function (err) {
    console.log('Running Script')
    handleScriptReturn(scriptName, err)
  })
}

function handleScriptReturn(scriptName, err) {
  if (err && err.message.includes('Python')) {
    alert('Python is required to run this app, please install it using Microsoft Store')
    throw err
  } else if (err) {
    alert(err)
    throw err
  }
  alert(scriptName + ' susccessfully!')
}

function getLanguage() {
  const activeBtn = document.querySelector('.active')

  return activeBtn.id
}
