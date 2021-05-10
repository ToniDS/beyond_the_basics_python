import subprocess
import locale

procObj = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
print(outputStr)