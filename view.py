#coding=utf-8
from tkinter import *  
from tkinter.messagebox import *
from conn import *
import tkinter.ttk as ttk
from tkinter import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
class InputFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1


    def write(self,name,sid,chinese,english,math):
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql = "select * from studentinfo;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall() #获取查询记录
            for row in results:
                if int(row[0]) == int(sid):
                    messagebox.showinfo(title='结果', message ="已存在该用户信息！")
                    cursor.close()
                    conn.close()
                    return
        except Exception as e:     
            raise e
        addstdinfo(sid,name)
        addstdginfo(sid,chinese,english,math)
        messagebox.showinfo(title='提示', message ="写入成功")
        return
    
    def click(self):
        name = self.E1.get()
        sid = self.E2.get()
        chinese = self.E3.get()
        english = self.E4.get()
        math = self.E5.get()
        if self.Isspace(name) or self.Isspace(sid) or self.Isspace(chinese) or self.Isspace(english) or self.Isspace(math) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.write(name,sid,chinese,english,math)
            
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '姓名: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '学号: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '语文: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '英语: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       

        Label(self, text = '数学: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)        
        Button(self, text='录入',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
  
class DeleteFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.createPage()
        
    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def delete(self,sid):
        temp=0
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql = "select sid from studentinfo;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall() #获取查询记录
            for row in results:
                if int(row[0]) == int(sid):
                    temp=1
                    cursor.close()
                    conn.close()
        except Exception as e:     
            raise e
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        if temp==1:
            deletestdinfo(sid)
            messagebox.showinfo(title='提示', message ="删除成功")
        
    def click(self):
        sid = self.E1.get()
        if self.Isspace(sid):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.delete(sid)
            
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '学号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)


        Button(self, text='删除',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
  
class ModifyFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

        
    def modify(self,name,sid,chinese,english,math):
        temp=0
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql = "select sid from studentinfo;"
        try:
            cursor.execute(sql)
            results = cursor.fetchall() #获取查询记录
            for row in results:
                if int(row[0]) == int(sid):
                    temp=1
                    cursor.close()
                    conn.close()
        except Exception as e:     
            raise e
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        if temp==1:
            alterstdg(sid,name,chinese,english,math)
            messagebox.showinfo(title='提示', message ="修改成功")
        
    def click(self):
        name = self.E1.get()
        sid = self.E2.get()
        chinese = self.E3.get()
        english = self.E4.get()
        math = self.E5.get()
        if self.Isspace(name) or self.Isspace(sid) or self.Isspace(chinese) or self.Isspace(english) or self.Isspace(math) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.modify(name,sid,chinese,english,math)
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '姓名: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '学号: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '语文: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '英语: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       

        Label(self, text = '数学: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)     
        Button(self, text='修改',command=self.click).grid(row=6, column=1, stick=E, pady=10)  

class QueryFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def query(self,sid):
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid where a.sid = %s"
        try:
            cursor.execute(sql,[sid])
            results = cursor.fetchall() #获取查询记录
            for row in results:
                if int(row[0]) == int(sid):
                    messagebox.showinfo(title='结果', message ="姓名："+str(row[1]) +"\n学号:"+str(row[0]) +"\n语文:"+ str(row[2]) +"\n英语:"+str(row[3]) +"\n数学:"+str(row[4])+"\n总分:"+str(row[5]))
                    cursor.close()
                    conn.close()
                    return
        except Exception as e:     
            raise e
        messagebox.showinfo(title='提示', message ="没有该信息")
        return        
        
        
    def click(self):
        sid = self.E1.get()
        if self.Isspace(sid):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.query(sid)
               
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '学号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)


        Button(self, text='查找',command=self.click).grid(row=6, column=1, stick=E, pady=10)
class QueryallFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.createPage()  


        
    def click(self):
        Button(self, text='语文',command=self.chbyasc).grid(row=2, column=1, stick=E, pady=10)
        Button(self, text='英语',command=self.enbyasc).grid(row=2, column=2, stick=E, pady=10)
        Button(self, text='数学',command=self.mabyasc).grid(row=2, column=3, stick=E, pady=10)


    def click2(self):
        Button(self, text='语文',command=self.chbydesc).grid(row=2, column=1, stick=E, pady=10)
        Button(self, text='英语',command=self.enbydesc).grid(row=2, column=2, stick=E, pady=10)
        Button(self, text='数学',command=self.mabydesc).grid(row=2, column=3, stick=E, pady=10)

    
    def chbyasc(self):
        columns = ("no","sno", "sname","yw")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yw", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yw", text="语文")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,chinese FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by chinese asc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
    def mabyasc(self):
        columns = ("no","sno", "sname","sx")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("sx", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("sx", text="数学")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,math FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by math asc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
    def mabydesc(self):
        columns = ("no","sno", "sname","sx")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("sx", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("sx", text="数学")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,math FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by math desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
    def enbyasc(self):
        columns = ("no","sno", "sname","yy")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yy", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yy", text="英语")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,english FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by english asc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results:
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
    def enbydesc(self):
        columns = ("no","sno", "sname","yy")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yy", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yy", text="英语")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,english FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by english desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results:
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
    def chbydesc(self):
        columns = ("no","sno", "sname","yw")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center')
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yw", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yw", text="语文")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=3,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,chinese FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by chinese desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2]))
            i=i+1
        conn.commit()
        conn.close()
        
               
    def createPage(self):
        Button(self, text='升序',command=self.click).grid(row=1, column=1, stick=E, pady=10)
        Button(self, text='降序',command=self.click2).grid(row=1, column=2, stick=E, pady=10)
class QuerysumallFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.createPage()  
        
    def allbyasc(self):
        columns = ("no","sno", "sname","yw","en","ma","all")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center') 
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yw", width=193, anchor='center')
        treeview.column("en", width=193, anchor='center')
        treeview.column("ma", width=193, anchor='center')
        treeview.column("all", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yw", text="语文")
        treeview.heading("en", text="英语")
        treeview.heading("ma", text="数学")
        treeview.heading("all", text="总成绩")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=6,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by sumall asc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2],line[3],line[4],line[5]))
            i=i+1
        conn.commit()
        conn.close()

    def allbydesc(self):
        columns = ("no","sno", "sname","yw","en","ma","all")
        treeview = ttk.Treeview(self, height=21, show="headings", columns=columns)  # 表格
        treeview.column("no", width=193, anchor='center') 
        treeview.column("sno", width=193, anchor='center') 
        treeview.column("sname", width=193, anchor='center')
        treeview.column("yw", width=193, anchor='center')
        treeview.column("en", width=193, anchor='center')
        treeview.column("ma", width=193, anchor='center')
        treeview.column("all", width=193, anchor='center')
        treeview.heading("no", text="排名") 
        treeview.heading("sno", text="学号") 
        treeview.heading("sname", text="姓名")
        treeview.heading("yw", text="语文")
        treeview.heading("en", text="英语")
        treeview.heading("ma", text="数学")
        treeview.heading("all", text="总成绩")
        vbar = ttk.Scrollbar(self,orient=VERTICAL,command=treeview.yview)
        treeview.configure(yscrollcommand=vbar.set)
        treeview.grid(row=8, column=2, stick=E, pady=10)
        vbar.grid(row=8,column=6,sticky=NS)
        conn = pymysql.connect(host="localhost",user="root",password="",port=3306,database="test1",charset="utf8")
        cursor = conn.cursor()
        sql="SELECT a.sid,sname,chinese,english,math,sumall FROM studentinfo a left join stdgrade b ON a.sid = b.sid order by sumall desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        i=1
        for line in results: 
            treeview.insert('','end',values=(i,line[0],line[1],line[2],line[3],line[4],line[5]))
            i=i+1
        conn.commit()
        conn.close()


               
    def createPage(self):
        Button(self, text='升序',command=self.allbyasc).grid(row=1, column=1, stick=E, pady=10)
        Button(self, text='降序',command=self.allbydesc).grid(row=1, column=2, stick=E, pady=10)
