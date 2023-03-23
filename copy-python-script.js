"use strict"

const fs = require("fs-extra")
const path = require("path")

exports.default = () => {
  const outDir = "./dist/installers"
  const unpackedDir = path.join(outDir, "win-unpacked")

  fs.copySync("script", path.join(unpackedDir, "script"))

  console.log("\x1b[32m%s\x1b[0m", "    Copied script to win-unpacked")

  return Promise.resolve()
}
