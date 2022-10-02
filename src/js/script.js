const { PythonShell } = require('python-shell')

document.getElementById('organize-btn').addEventListener('click', function () {
  const language = getLanguage()
  runPythonScriptWithArgs('organize', [language])
})

document.getElementById('undo-btn').addEventListener('click', function () {
  runPythonScript('undo')
})

function runPythonScript(scriptName) {
  PythonShell.run(`./script/${scriptName}.py`, null, function (err) {
    console.log('Running Script')
    handleScriptReturn(scriptName, err)
  })
}

function runPythonScriptWithArgs(scriptName, args) {
  PythonShell.run(`./script/${scriptName}.py`, { args: args }, function (err) {
    console.log('Running Script')
    handleScriptReturn(scriptName, err)
  })
}

function handleScriptReturn(scriptName, err) {
  if (err) {
    alert(err)
    throw err
  }
  alert(scriptName + ' susccessfully!')
}

function getLanguage() {
  const activeBtn = document.querySelector('.active')

  return activeBtn.id
}
