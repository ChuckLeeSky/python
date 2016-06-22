# -*- coding:utf8 -*-
# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:lihaozheng
# Date:2016-06-22

"""
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""

import string,random
import MySQLdb


def generate_key():
    key_list=[]
    for i in range(200):
        chars=string.letters+string.digits
        s=[random.choice(chars) for i in range(10)]
        str1=''.join(s)
        key_list.append(str1)
    return key_list


def write_to_mysql(key_list):
    # Connect to database
    db = MySQLdb.connect("localhost", "root", "omaiga", "test")

    # Use function cursor() to open the cursor operation
    cursor = db.cursor()

    # If the table exists, delete it
    cursor.execute("drop table if exists ukey")

    # Create table
    sql = """create table ukey (
            key_value char(40) not null
            )"""
    cursor.execute(sql)

    # Insert data
    try:
        for i in range(200):
            cursor.execute('insert into ukey values("%s")' % (key_list[i]))
        # Commit to database
        db.commit()
    except:
        # Rollback when errors occur
        db.rollback()

    # Close database
    db.close()


if __name__ == '__main__':
    write_to_mysql(generate_key())