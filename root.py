from subprocess import Popen, PIPE, call

process = Popen(["curl","www.google.com"], stdin = PIPE)
output = process.stdout.readline()

from subprocess import Popen, PIPE, call

process = Popen(["curl","www.google.com"], stdin = PIPE)
output = process.stdout.readline()
