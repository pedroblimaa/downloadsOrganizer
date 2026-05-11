"use strict"

const { spawnSync } = require("child_process")
const fs = require("fs-extra")
const path = require("path")

const rootDir = path.resolve(__dirname, "..")
const pythonDistDir = path.join(rootDir, "build", "python")
const pyinstallerWorkDir = path.join(rootDir, "build", "pyinstaller")
const specDir = path.join(rootDir, "build")
const entrypoint = path.join(rootDir, "script", "downloads_organizer.py")

const pythonCommands = [
  { command: "py", args: ["-m"] },
  { command: "python", args: ["-m"] },
  { command: "python3", args: ["-m"] },
]

function main() {
  const python = findPythonWithPyInstaller()

  fs.removeSync(pythonDistDir)
  fs.ensureDirSync(pythonDistDir)

  const result = spawnSync(
    python.command,
    [
      ...python.args,
      "PyInstaller",
      "--onefile",
      "--clean",
      "--name",
      "downloads_organizer",
      "--distpath",
      pythonDistDir,
      "--workpath",
      pyinstallerWorkDir,
      "--specpath",
      specDir,
      entrypoint,
    ],
    {
      cwd: rootDir,
      stdio: "inherit",
      shell: false,
    }
  )

  if (result.status !== 0) {
    process.exit(result.status || 1)
  }
}

function findPythonWithPyInstaller() {
  for (const python of pythonCommands) {
    const result = spawnSync(
      python.command,
      [...python.args, "PyInstaller", "--version"],
      {
        cwd: rootDir,
        encoding: "utf8",
        shell: false,
      }
    )

    if (result.status === 0) {
      return python
    }
  }

  console.error(
    "PyInstaller was not found. Install Python and run: py -m pip install pyinstaller"
  )
  process.exit(1)
}

main()
