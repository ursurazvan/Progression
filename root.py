from subprocess import Popen, PIPE, call
import re

process = Popen(["curl","http://challenge01.root-me.org/programmation/ch1/"], stdout = PIPE)
output = 'asd'
while output!='':
	output = process.stdout.readline()
	output = output.decode("utf-8")
	print(output)	
	if 'n+1' in output:
		a=re.findall("[-\d]+", output)
		if a[-2]=='-':
			arguments = a[-3:]
		else:
			arguments = a[-2:]
			arguments.insert(1,'+')
	if 'U<sub>0</sub> =' in output:
		a=re.findall("[-\d]+", output)
		arguments.append(a[-1])
	if 'You must find U' in output:
		a=re.findall("[-\d]+", output)
		arguments.append(a[0])
		print(arguments)
process.stdout.close()


