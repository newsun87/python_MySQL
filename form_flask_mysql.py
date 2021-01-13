#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask,render_template,request
import pymysql 

# 儲存資料庫連線設定
DB_CONFIG = {
	"host": "127.0.0.1",
	"port": 3306,
	"user": "root",
	"passwd": "admin",
	"db": "myschool",
	"charset": "utf8"
}

app=Flask(__name__)
@app.route('/') 
def index(): 
  return render_template('mysql_index.html', result={}) #回傳網頁 
  
@app.route('/link', methods=['POST','GET']) 
def link():      
  if request.method =='POST': #判斷是否為POST請求     
   #判斷請求的表單按鈕是否為"查詢學生資料"  
   if request.values['redirect']=='查詢學生資料':
    results = query()    
    return render_template('mysql_index.html', result = results) #回傳查詢結果給網頁
   elif request.values['redirect']=='添加學生資料': #判斷請求的表單按鈕是否為"添加學生資料"
    return render_template('mysql_index.html', insert_result = {}) #回傳網頁
   elif request.values['redirect']=='刪除學生資料': #判斷請求的表單按鈕是否為"添刪除學生資料" 
    return render_template('mysql_index.html', delete_result = {}) #回傳網頁
    		
@app.route('/insert', methods=['POST','GET']) 
def insert():
   if request.method =='POST': #判斷是否為POST請求 
    db = mysql_connect()
    # 使用cursor()方法獲取操作遊標 
    cursor = db.cursor()   	             
    if request.values['send']=='新增': #判斷請求的表單資料是否為"send"
     sno = request.values['sno']
     name = request.values['name']
     address = request.values['address']
     birthday = request.values['birthday']	
     sql = "INSERT INTO students (sno, name, address, birthday) VALUES (%s, %s, %s, %s)"
     val = (sno, name, address, birthday)     
     cursor.execute(sql, val) # 執行SQL語句
     db.commit()
     db.close()# 關閉資料庫連線  	        
     return render_template('mysql_index.html', insert_result = "資料新增成功") #回傳網頁
     
@app.route('/delete', methods=['POST','GET']) 
def delete():
   if request.method =='POST': #判斷是否為POST請求 
    db = mysql_connect()
    # 使用cursor()方法獲取操作遊標 
    cursor = db.cursor()   	             
    if request.values['send']=='刪除': #判斷請求的表單資料是否為"send" 
     sno = request.values['sno']    
     sql = "DELETE FROM students WHERE sno= '%s'" % (sno)     
     cursor.execute(sql) # 執行SQL語句
     db.commit()
     db.close()# 關閉資料庫連線  	        
     return render_template('mysql_index.html', delete_result = "資料刪除成功") #回傳網頁
     
def mysql_connect():
	# 開啟資料庫連線
   db = pymysql.connect(
            host=DB_CONFIG["host"],
			port=DB_CONFIG["port"],
			user=DB_CONFIG["user"],
			passwd=DB_CONFIG["passwd"],
			db=DB_CONFIG["db"],
			charset=DB_CONFIG["charset"]
	    )
   return db # 回傳連線物件
   
def query(): 
   db = mysql_connect()
   # 使用cursor()方法獲取操作遊標 
   cursor = db.cursor()  
   if request.method =='POST': #判斷是否為POST請求 
    sql = "SELECT * FROM students" 
    cursor.execute(sql) # 執行SQL語句   
    results = cursor.fetchall() # 獲取所有記錄列表
    print(results)
    for row in results:
      sno = row[0]
      name= row[1]
      address = row[2]
      birthday = row[3]            
      print ("sno=%s, name=%s, address=%s, birthday=%s " % \
             (sno, name, address, birthday)) # 列印結果
    db.commit()
    db.close()# 關閉資料庫連線
    return results # 回傳查詢結果  

#db.close()# 關閉資料庫連線
if __name__ == "__main__": #表示此段為主程式
    app.run(debug=True, host='0.0.0.0', port=5000)

