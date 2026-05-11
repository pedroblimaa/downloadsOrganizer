"use strict"

const fs = require("fs-extra")
const path = require("path")

exports.default = () => {
  const outDir = "./dist/installers"
  const unpackedDir = path.join(outDir, "win-unpacked")
  const executableName = "downloads_organizer.exe"
  const executablePath = path.join("build", "python", executableName)
  const resourcesDir = path.join(unpackedDir, "resources")

  if (!fs.existsSync(executablePath)) {
    throw new Error(
      `Python executable not found at ${executablePath}. Run pnpm build:python first.`
    )
  }

  fs.copySync(executablePath, path.join(resourcesDir, executableName))

  console.log("\x1b[32m%s\x1b[0m", "    Copied Python executable to resources")

  return Promise.resolve()
}
