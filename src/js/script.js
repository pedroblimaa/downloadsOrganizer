const { PythonShell } = require('python-shell')

document.getElementById('organize-btn').addEventListener('click', function () {
  getLanguage()
  runPythonScript('organize')
})

document.getElementById('undo-btn').addEventListener('click', function () {
  getLanguage()
  runPythonScript('undo')
})

function runPythonScript(scriptName) {
  PythonShell.run(`./script/${scriptName}.py`, null, function (err) {
    console.log('Running')
    handleScriptReturn(scriptName, err)
  })
}

function handleScriptReturn(scriptName, err) {
  if (err) {
    alert('Error: ' + err)
    throw err
  }
  alert(scriptName + ' susccessfully!')
}

function getLanguage() {
  // TODO - Get Value from the active buttons
}
