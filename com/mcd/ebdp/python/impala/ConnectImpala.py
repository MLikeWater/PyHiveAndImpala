#!/usr/bin/env bash
#coding=utf-8

from impala.dbapi import connect
conn = connect(host='localhost', port=21050, database='test', user='hello', password='world', auth_mechanism='PLAIN')
cursor = conn.cursor()

# 如果首次在Hive里面创建数据库或表或修改表结构，Impala侧需要同步元数据
cursor.execute('invalidate metadata customer')

# 如果Hive表的数据发生变化或增加分区，Impala侧使用refresh轻量级同步元数据
cursor.execute('refresh customer')

cursor.execute('SELECT * FROM customer LIMIT 100')
print cursor.description  # prints the result set's schema
results = cursor.fetchall()

for result in results:
    print(result)
