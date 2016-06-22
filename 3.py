import redis
import string,random,sys

file1=open('promoto.txt','wb')
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

cache = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

for i in range(100):
	chars=string.letters+string.digits
	str1=[random.choice(chars) for i in range(10)]
	file1.write(''.join(str1)+'\n')

file1.close()

with open('promoto.txt','r') as f:
	keyList=[]
	for lineNum,eachCode in enumerate(f.readline()):
		keyList.append(lineNum)
		cache.set(str(lineNum), eachCode)
	for i in keyList:
		print i
#read
for i in keyList:
	print cache.get(str(i))
