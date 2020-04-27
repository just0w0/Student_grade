#coding=utf-8

import pymysql
from tkinter import *
from tkinter.messagebox import *  

def addstdinfo(sid,sname): #添加学生信息
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "insert into studentinfo(sid,sname,password) values(%s,%s,%s);"
    password = 123456
    try:
        cursor.execute(sql,[sid,sname,password])
        conn.commit()      
    except Exception as e:     # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()
def deletestdinfo(sid): #删除学生信息
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "delete from studentinfo where sid = %s;"
    try:
        cursor.execute(sql,[sid])
        conn.commit()
    except Exception as e:
        conn.rollback()
    cursor.close()
    conn.close()
def addstdginfo(sid,chinese,english,math): #增加学生成绩信息
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "insert into stdgrade(sid,chinese,english,math,sumall) values(%s,%s,%s,%s,%s);"
    sumall = float(chinese) + float(english) + float(math)
    try:
        cursor.execute(sql,[sid,chinese,english,math,sumall])
        conn.commit()      
    except Exception as e:     # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()
def alterstdg(sid,name,chinese,english,math): #修改学生成绩
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "update stdgrade set chinese = %s,english = %s,math = %s,sumall = %s where sid = %s;"
    sumall = float(chinese) + float(english) + float(math)
    try:
        cursor.execute(sql,[chinese,english,math,sumall,sid])
        conn.commit()      
    except Exception as e:     # 有异常，回滚事务
        conn.rollback()
    sql = "update studentinfo set sname =%s where sid =%s;"
    try:
        cursor.execute(sql,[name,sid])
        conn.commit()      
    except Exception as e:     # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()
def selectstdg():#总查询
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese","english","math","sum")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            english = row[3]
            math = row[4]
            sumall = row[5]
            print(id,name,chinese,english,math,sumall)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def selectperson():  #个人查询
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid where a.sid = %s;"
    sid = input("请输入要查询学生学号:")
    try:
        cursor.execute(sql,[sid])
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese","english","math","sum")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            english = row[3]
            math = row[4]
            sumall = row[5]
            print(id,name,chinese,english,math,sumall)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def selectbyasc(): #总成绩升序查询
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by sumall asc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese","english","math","sum")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            english = row[3]
            math = row[4]
            sumall = row[5]
            print(id,name,chinese,english,math,sumall)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def selectbydesc(): #总成绩降序查询
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by sumall desc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese","english","math","sum")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            english = row[3]
            math = row[4]
            sumall = row[5]
            print(id,name,chinese,english,math,sumall)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def mathbydesc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,math FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by math desc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","math")
        for row in results:
            id = row[0]
            name = row[1]
            math = row[2]
            print(id,name,math)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def mathbyasc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,math FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by math asc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","math")
        for row in results:
            id = row[0]
            name = row[1]
            math = row[2]
            print(id,name,math)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()    
def chinesebyasc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by chinese asc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            print(id,name,chinese)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def chinesebydesc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,chinese FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by chinese desc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","chinese")
        for row in results:
            id = row[0]
            name = row[1]
            chinese = row[2]
            print(id,name,chinese)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def englishbydesc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,english FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by english desc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","english")
        for row in results:
            id = row[0]
            name = row[1]
            english = row[2]
            print(id,name,english)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()
def englishbyasc():
    conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT a.sid,sname,english FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by english asc"
    try:
        cursor.execute(sql)
        results = cursor.fetchall() #获取查询记录
        print("id","name","english")
        for row in results:
            id = row[0]
            name = row[1]
            english = row[2]
            print(id,name,english)
    except Exception as e:     
        raise e
    cursor.close()
    conn.close()

