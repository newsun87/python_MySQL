#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
 
# 開啟資料庫連db_test連線
db = pymysql.connect("localhost","root","1234","db_test" )
 
# 使用 cursor() 方法建立一個遊標物件 cursor
cursor = db.cursor()
 
# 使用 execute()  方法執行 SQL 查詢 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法獲取單條資料.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 關閉資料庫連線
db.close()
