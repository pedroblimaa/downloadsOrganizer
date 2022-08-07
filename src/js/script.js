const { PythonShell } = require('python-shell')

document.getElementById('organize-btn').addEventListener('click', function () {
  PythonShell.run('./script/organize.py', null, function (err) {
    console.log('Running')
    if (err) {
      alert('Error: ' + err)
      throw err
    }
    alert('Organized susccessfully!')
  })
})

document.getElementById('undo-btn').addEventListener('click', function () {
  PythonShell.run('./script/undo.py', null, function (err) {
    if (err) {
      alert('Error: ' + err)
      throw err
    }
    alert('Undo susccessfully!')
  })
})
