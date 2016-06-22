#coding:utf-8
from MySQLdb import *

def conn():
	cn=Connection('127.0.0.1','root','omaiga','test')
#Connection()函数的参数依次为
#     host(string, host to connect);
#     user(string, user to connect as);
#     passwd(string, password to use);
#     db(string, database to use)
#也可以这样选择数据库
#cn.select_db('test')
	cur=cn.cursor()
	cur.execute('select * from t1')
#设置游标的位置，不设置默认为0
#cur.scroll(0)
	row=cur.fetchone()
#查询游标位置的一条记录，返回值为元组
	print row[0] #输出第一个字段内容
	print row[1]
 
if __name__=='__main__':
	conn()