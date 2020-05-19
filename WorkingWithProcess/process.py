import subprocess #enable us to use and easily work with child processes in Python
pc = subprocess.Popen(['ps','-U','0'], stdout=subprocess.PIPE).communicate()[0] #Allow us to execute ps command as a python child process.
#variable pc will be a byte array containing the output of the command we executed.
print(pc.decode('utf-8'))
