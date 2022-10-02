import os

exePath = os.path.join(os.getcwd(), "dist", "win-unpacked")
scriptsFromPath = os.path.join(os.getcwd(), "script")
scriptsToPath = os.path.join(exePath, "script")

os.system("yarn dist")
os.system("cp -r '" + scriptsFromPath + "' '" + scriptsToPath + "'")
os.system("node build_installer.js")
