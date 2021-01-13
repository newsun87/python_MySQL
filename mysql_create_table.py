#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pymysql
 
# 開啟資料庫連db_test連線
db = pymysql.connect("localhost","root","1234", "maxdb") 
cursor = db.cursor() #建立cursor物件 
#cursor.execute("create database maxdb") #建立maxdb資料庫
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()
