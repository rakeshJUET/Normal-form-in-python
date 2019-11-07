from Tkinter import *
import sqlite3
from Tkinter import *
from tkMessageBox import *

splashRoot=Tk()
splashRoot.configure(background='#222022')
Label(splashRoot,text='RAKESH KUMAR DWIVEDI',font='Arial 20 bold',bg='#222022',fg='#1ed2f4',width=40).grid(row=0,column=0,columnspan=2)
Label(splashRoot,text='Enrollment No',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=1,column=0)
Label(splashRoot,text='171B092',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=1,column=1)
Label(splashRoot,text='',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=2,column=0)

Label(splashRoot,text='Batch',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=3,column=0)
Label(splashRoot,text='B3',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=3,column=1)
Label(splashRoot,text='',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=4,column=0)

Label(splashRoot,text='Email Id',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=5,column=0)
Label(splashRoot,text='rakeshdwivedi15072000@gmail.com',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=5,column=1)
Label(splashRoot,text='',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=6,column=0)

Label(splashRoot,text='Phone No',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=7,column=0)
Label(splashRoot,text='8827935409',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=7,column=1)
Label(splashRoot,text='',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=8,column=0)
def mainWindow():
    root5=Tk()
    root5.configure(background='#222022')
    con=sqlite3.Connection('record_database')
    cur=con.cursor()
    cur.execute('create table if not exists emp092 (emp_id varchar(10),emp_name varchar(20),date_of_birth varchar(10),emp_mobileno number,address varchar(50), salary number)')
    #cur.execute("delete from emp092")
    def insert():
        if e1.get():
            if e2.get():
                if e3.get():
                    if e4.get():
                        if e5.get():
                            if e6.get():
                               cur.execute("insert into emp092 values (?,?,?,?,?,?)",[e1.get(),e2.get(),e3.get(),e4.get(),(e5.get()),int(e6.get())])
                               con.commit()
                            else:
                               showerror("STATUS",'ENTER SALARY')
                        else:
                           showerror("STATUS",'ENTER ADDRESS')
                    else:
                        showerror("STATUS",'ENTER MOBILE_NO')
                else:
                    showerror("STATUS",'ENTER DATE OF BIRTH')
            else:
                showerror("STATUS",'ENTER EMP_NAME')
        else:
            showerror("STATUS",'ENTER EMP_ID')
        showinfo("STATUS",'VALUES INSERTED :)')  
           
          
    def show():
        emp_id= e7.get()
        try:
            sqlText="select * from emp092 where emp_id='"+emp_id+"'"
            cur.execute(sqlText)
            a=cur.fetchall()
            print a
            Label(root5,text=a).grid(row=20,column=1)
        except:
            showerror("STATUS",'INVALID EMPLOY_ID')
        #Label(root,text=a).grid(row=7,column=1)
    def show_all():
        cur.execute("select * from emp092")
        a1=cur.fetchall()
        print a1
    def att():
        print e7.get()
        cur.execute('select * from emp092  where emp_id=?',(e11.get(),))
        a3=cur.fetchall()
        print a3
        #Label(root,text=a3).grid(row=12,column=0)
    root=Tk()
    def resetData():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
    Label(root5,text='EMPLOY RECORD',width=50,font='Arial 20 bold',bg='#222022',fg='#ffffff').grid(row=0,column=0,columnspan=2)
    Label(root5,text='',bg='#222022').grid(row=1,column=0)
    Label(root5,text='EMPLOY_ID',bg='#222022',fg='#ffffff').grid(row=2,column=0)
    e1=Entry(root5)
    e1.grid(row=2,column=1)
    
    Label(root5,text='',bg='#222022').grid(row=3,column=0)
    Label(root5,text='EMP_NAME',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=4,column=0)
    e2=Entry(root5)
    e2.grid(row=4,column=1)
    
    Label(root5,text='',bg='#222022').grid(row=5,column=0)
    Label(root5,text='DATE_OF_BIRTH',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=6,column=0)
    e3=Entry(root5)
    e3.grid(row=6,column=1)

    Label(root5,text='',bg='#222022').grid(row=7,column=0)
    Label(root5,text='EMP_MOBILENO',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=8,column=0)
    e4=Entry(root5)
    e4.grid(row=8,column=1)
    
    Label(root5,text='',bg='#222022').grid(row=9,column=0)
    Label(root5,text='ADDRESS',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=10,column=0)
    e5=Entry(root5)
    e5.grid(row=10,column=1)
    
    Label(root5,text='',bg='#222022').grid(row=11,column=0)
    Label(root5,text='SALARY',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=12,column=0)
    e6=Entry(root5)
    e6.grid(row=12,column=1)
    
    Label(root5,text='',bg='#222022').grid(row=13,column=0)
    Label(root5,text='EMPLOY_ID',font='Arial 10',bg='#222022',fg='#ffffff').grid(row=14,column=0)
    e7=Entry(root5)
    e7.grid(row=14,column=1)
    Label(root5,text='',bg='#222022').grid(row=15,column=0)
    
    Button(root5,text='RESET',font='Arial 10',width=15,command=resetData).grid(row=16,column=0)
    Button(root5,text='INSERT',font='Arial 10',width=15,command=insert).grid(row=16,column=1)
    Label(root5,text='',bg='#222022').grid(row=17,column=0)
    
    Button(root5,text='SHOW',font='Arial 10',width=15,command=show).grid(row=18,column=0)
    Button(root5,text='SHOW ALL',font='Arial 10',width=15,command=show_all).grid(row=18,column=1)
    Label(root5,text='',bg='#222022').grid(row=19,column=0)
    
    

    root5.mainloop()

    
def loginWindow(e):
	splashRoot.destroy()
	loginWindowRoot=Tk()
	loginWindowRoot.configure(background='#222022')
	loginWindowRoot.title('my webkiosk')
	Label(loginWindowRoot,text='LOGIN',font='Arial 15 bold',bg='#222022',fg='#ffffff',width=40).grid(row=0,column=0,columnspan=2)
	Label(loginWindowRoot,text='',width=15,bd=7,bg='#222022').grid(row=1,column=0)
	Label(loginWindowRoot,text='USERNAME',font='Arial 10',width=15,bd=5,bg='#222022',fg='#ffffff').grid(row=2,column=0)
	e1=Entry(loginWindowRoot,relief=FLAT,font='Arial 10',width=15)
	e1.grid(row=2,column=1,ipady=4)
	Label(loginWindowRoot,text='',width=15,bd=7,bg='#222022',fg='#ffffff').grid(row=3,column=0)
	b=Label(loginWindowRoot,text='PASSWORD',width=15,font='Arial 10',bg="#222022",bd=5,fg='#ffffff').grid(row=4,column=0)
	e2=Entry(loginWindowRoot,show='*',relief=FLAT,font='Arial 10',width=15,bg='white')
	e2.grid(row=4,column=1,ipady=4)
	def submitData():
	    if(e2.get()=='12345'):
	        mainWindow()
	    else:
	        showerror('response','Wrong Password')
	        showinfo('response','please try again!!!!')
	def resetData():
	    e1.delete(0,END)
	    e2.delete(0,END)
	Label(loginWindowRoot,text='',width=15,bd=7,bg='#222022',fg='#ffffff').grid(row=5,column=0)
	Button(loginWindowRoot,text='RESET',bg='red',width=10,command=resetData).grid(row=6,column=0,ipady=4)
	Button(loginWindowRoot,text='SUBMIT',bg='red',width=10,command=submitData).grid(row=6,column=1,ipady=4)
	Label(loginWindowRoot,text='',width=15,bd=7,bg='#222022',fg='#ffffff').grid(row=7,column=0)
	loginWindowRoot.mainloop()

splashRoot.bind('<Motion>',loginWindow)
splashRoot.mainloop()
               
