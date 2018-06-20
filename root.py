from subprocess import Popen, PIPE, call
import re
from time import sleep

process = Popen(["curl","-c","-","http://challenge01.root-me.org/programmation/ch1/"], stdout = PIPE)
output = 'asd'
while output!='':
	output = process.stdout.readline()
	output = output.decode("utf-8")	
	if 'n+1' in output:
		a=re.findall("[-\d]+", output)
		if a[-2]=='-':
			arguments = a[-3:]
			arguments[1]='-1'
		else:
			arguments = a[-2:]
			arguments.insert(1,'1')
	if 'U<sub>0</sub> =' in output:
		a=re.findall("[-\d]+", output)
		arguments.append(a[-1])
	if 'You must find U' in output:
		a=re.findall("[-\d]+", output)
		arguments.append(a[0])
	if 'PHPSESSID' in output:
		cook=output.split()
		cook=cook[-1]
		
process.stdout.close()

a = list(map(int, arguments))
print(a)
res = a[3]
for i in range (1,a[-1]+1):
	res = (res + a[0]) + (i*a[1]*a[2])
print(res)
site="http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="
site=site+str(res)
print(site)
cookie = "PHPSESSID="+cook
print(cookie)
a=call(["curl","-v","--cookie",cookie,site])
