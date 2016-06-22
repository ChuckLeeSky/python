#/usr/bin/python
import string,random,sys
print sys.path
file1=open('promoto.txt','wb')


for i in range(100):
	chars=string.letters+string.digits
	str1=[random.choice(chars) for i in range(10)]
	print str1
	file1.write(''.join(str1)+'\n')

file1.close()