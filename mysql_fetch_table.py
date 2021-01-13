#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql 
# 開啟資料庫連線
db = pymysql.connect("localhost","root","1234","maxdb" ) 
# 使用cursor()方法獲取操作遊標 
cursor = db.cursor() 
# SQL 查詢語句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:  
   cursor.execute(sql) # 執行SQL語句   
   results = cursor.fetchall() # 獲取所有記錄列表
   print(results)
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]      
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )) # 列印結果
except:
   print ("Error: unable to fetch data")
 
db.close()# 關閉資料庫連線