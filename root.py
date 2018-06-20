
process = Popen(["curl","www.google.com"], stdin = PIPE)
output = process.stdout.readline()
