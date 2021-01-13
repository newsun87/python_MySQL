#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
 
# 開啟資料庫連maxdb連線
db = pymysql.connect("localhost","root","1234", "maxdb") 
cursor = db.cursor() #建立cursor物件 
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:   
   cursor.execute(sql) # 執行SQL語句
   db.commit() # 提交到資料庫執行
except:   
   db.rollback() # 發生錯誤時回滾
db.close() # 關閉資料庫連線

