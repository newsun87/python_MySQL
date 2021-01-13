#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pymysql 
# 開啟資料庫連db_test連線
db = pymysql.connect("localhost","root","1234", "maxdb") 
cursor = db.cursor() #建立cursor物件 
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)""" # SQL 插入語句
try:
  cursor.execute(sql) # 執行sql語句
  db.commit() # 提交到資料庫執行
except:
  db.rollback() # 如果發生錯誤則回滾 
db.close() # 關閉資料庫連線
