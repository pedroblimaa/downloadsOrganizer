let { PythonShell } = require('python-shell')

// listen to the btn with id 'organize-btn' click event
document.getElementById('organize-btn').addEventListener('click', function () {
  PythonShell.run('./script/organize.py', null, function (err) {
    console.log('Running')
    if (err) throw err
    alert('Organized susccessfully!')
  })
})

document.getElementById('undo-btn').addEventListener('click', function () {
  PythonShell.run('./script/undo.py', null, function (err) {
    if (err) throw err
    alert('Undo susccessfully!')
  })
})
