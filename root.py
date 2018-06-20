from subprocess import Popen, PIPE, call

process = Popen(["curl","www.google.com"], stdout = process)
output = process.stdout.readline()
print(output)


