import subprocess

try:
    #subprocess.call(('Notepad.exe'))
    #subprocess.call(("C:/windoWs/notepad.exe"))
    subprocess.call(('notepad.exe', "repaso.txt"))
except subprocess.CalledProcessError as e:
    print (e.output)
