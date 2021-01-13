#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])#接收瀏覽器的網頁路由請求
def index():
	if request.method =='POST': #判斷是否為POST請求
		if request.values['send']=='送出': #判斷請求的表單資料是否為"send"
			result = request.form #取得表單資料物件
			print(result) 
			return render_template('form1.html', result = result) #回傳網頁及參數資料
	return render_template('form1.html', result={}) #回傳網頁
if __name__ == "__main__": #表示此段為主程式
    app.run(debug=True, host='0.0.0.0', port=5000)
