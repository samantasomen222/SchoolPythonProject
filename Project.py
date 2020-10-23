"""
Student Management system 
For angels' academy sr. sec. school
"""
from tkinter import *
from tkinter import ttk
import time
import datetime
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
import os
"""
making of table names
"""

StudentTable="Student"
AdminTable="Admins"
MarksTable="Marks"

"""
making directory
"""
path=os.environ["userprofile"]
try:
    os.mkdir(path+"\\Documents\\Student Database")
except FileExistsError:
    pass

con = sqlite3.connect(path+"\\Documents\\student Database\Studb.db")
cur = con.cursor()

"""
creating tables
"""
con.execute("create table if not exists Admins(adminId varchar(5) primary key,Password varchar(8))")
con.execute("create table if not exists Student(StudId varchar(5) primary key,Stud_name varchar(20),Stud_Email varchar(30),Stud_Contact varchar(10),Stud_class varchar(2))")
con.execute("create table if not exists Marks(StudId varchar(5) primary key,Marks_For varchar(10),Marks_of varchar(5),marks_ob varchar(5))")


"""
creating user intrface
"""
root=Tk()

root.title("Login")
root.iconbitmap('image\login.ico')
root.geometry('950x700+225+0')
root.resizable(False,False)

img1 = ImageTk.PhotoImage(file='image\log.jpg')

img2 = ImageTk.PhotoImage(file='image\logi.jpg')

img3 = ImageTk.PhotoImage(file='image\signin.png')


label=Label(root,image=img1).place(x=0,y=0,relwidth=1,relheight=1)

"""
login
"""
frm2=Frame(root,bg='white')
frm2.place(relx=0.4,rely=0,relwidth=0.2,relheight=0.3)
lb=Label(frm2,image=img3).place(x=0,y=0,relwidth=1,relheight=1)


"""
second working window
"""

def win2():
	root2=Tk()
	root2.geometry('950x600+200+45')
	root2.title('Student management System')
	root2.iconbitmap('image\student.ico')
	root2.resizable(False,False)

	img=ImageTk.PhotoImage(file='image\stud.jpg')

	now=datetime.datetime.now()
	timenow=''
	datetoday=''

	"""
	Clock
	"""

	def tick():
		timenow=''
		newtime=time.strftime('%H: %M: %S')
		if newtime != timenow:
			timenow= newtime
			clock.config(text=timenow)
		
		clock.after(200,tick)

	"""
	Date
	"""

	def date():
		datetoday=''
		newdate=now.strftime('%d-%m-%y')
		if datetoday != newdate:
			datetoday=newdate
			dateprt. config(text=datetoday)

		dateprt.after(200,date)


	"""
	Making of frames
	"""

	frm1=Frame(root2,bg='#8B1A1A')
	frm1.place(relx=0,rely=0,relwidth=1,relheight=0.2)

	frm2=Frame(root2,bg='#228B22')
	frm2.place(relx=0,rely=0.2,relwidth=0.15,relheight=0.8)

	frm3=Frame(root2,bg='#B5B5B5')
	frm3.place(relx=0.15,rely=0.2,relwidth=0.85,relheight=0.8)

	frm4=Frame(frm3,bg='#282828')
	frm4.place(relx=0,rely=0.85,relwidth=1,relheight=0.15)

	frm5=Frame(frm3,bg='#B5B5B5')
	frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

	"""
	Adding of clock and date
	"""

	clock=Label(frm4,text=timenow,font=('arial',10,'bold'),bg='#282828',fg='#F0F0F0')
	clock.place(relx=0.85,rely=0.2)
	tick()

	dateprt=Label(frm4,text=datetoday,font=('arial',10,'bold'),bg='#282828',fg='#F0F0F0')
	dateprt.place(relx=0.85,rely=0.52)
	date()

	lb1=Label(frm1,image=img,compound=LEFT,text="STUDENT MANAGEMENT\nAngels' Academy",font=('impact',25,'bold'),fg='#98F5FF',bg='#8B1A1A')
	lb1.place(relx=0.3,rely=0.1)
	
	"""
	Defining of Menu
	"""

	def close():
		frm5.destroy


	def stureg():
		global ent1,ent2,ent3,ent4,ent5
		Id = ent1.get()
		name = ent2.get()
		email = ent3.get()
		contact = ent4.get()
		clas = ent5.get()

		addstud = "insert into "+StudentTable+" values('"+Id+"','"+name+"','"+email+"','"+contact+"','"+clas+"');"
		if Id=="" or name=="" or email=="" or contact=="" or clas=="":
			messagebox.showerror("Error","Fill all the required fields")
		else:
			try:
				cur.execute(addstud)
				con.commit()
				messagebox.showinfo("success","Details Added")
			except:
				messagebox.showerror("Error","Can't add data into database")

		ent1.delete(0,END)
		ent2.delete(0,END)
		ent3.delete(0,END)
		ent4.delete(0,END)
		ent5.current(0)
			




	def add():
		global frm5,ent1,ent2,ent3,ent4,ent5
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

		lab1=Label(frm5,text='Student Id:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab1.place(relx=0.1,rely=0.05)

		ent1=Entry(frm5,font=('Monaco',15,'bold'))
		ent1.place(relx=0.35,rely=0.05,relwidth=0.4)

		lab2=Label(frm5,text='Student Name:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab2.place(relx=0.1,rely=0.15)

		ent2=Entry(frm5,font=('Monaco',15))
		ent2.place(relx=0.35,rely=0.15,relwidth=0.4)

		lab3=Label(frm5,text='Email:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab3.place(relx=0.1,rely=0.25)

		ent3=Entry(frm5,font=('Monaco',15,'bold'))
		ent3.place(relx=0.35,rely=0.25,relwidth=0.4)

		lab4=Label(frm5,text='Contact:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab4.place(relx=0.1,rely=0.35)

		ent4=Entry(frm5,font=('Monaco',15,'bold'))
		ent4.place(relx=0.35,rely=0.35,relwidth=0.4)

		lab5=Label(frm5,text='Class:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab5.place(relx=0.1,rely=0.45)

		ent5=ttk.Combobox(frm5, font=('arial', 10, 'bold'), state='readonly', width=10)
		ent5['values']=('','11','12')
		ent5.current(0)
		ent5.place(relx=0.35,rely=0.45,relwidth=0.3,relheight=0.075)

		Btn1=Button(frm5,text='ADD STUDENT',font=('arial',15,'bold'),bd=1,bg='#B5B5B5',activebackground='#B5B5B5',command=stureg)
		Btn1.place(relx=0.4,rely=0.6,relheight=0.1,relwidth=0.2)



	def find_id():
		global frm5,ent1
		Id=ent1.get()
		std="select * from "+StudentTable+" where StudId = '"+Id+"';"
		if Id=="":
			messagebox.showerror('Error',"Nothing found in Entry Box")
		else:
			try:
				cur.execute(std)
				for i in cur:
					stid = i[0]
					stnam= i[1]
					stem = i[2]
					stcon= i[3]
					stcls= i[4]
				info="studentId = "+stid+"\n Student Name = "+stnam+"\n Student Email = "+stem+"\n Student contact = "+stcon+"\n student class ="+stcls
				messagebox.showinfo('found',info)
			except:
				messagebox.showerror("error","Cannot Fetch The data")
		ent1.delete(0,END)

	def find_Name():
		global frm5,ent2
		Name=ent2.get()
		std="select * from "+StudentTable+" where Stud_name = '"+Name+"';"
		if Name=="":
			messagebox.showerror('Error',"Nothing found in Entry Box")
		else:
			try:
				cur.execute(std)
				for i in cur:
					stid = i[0]
					stnam= i[1]
					stem = i[2]
					stcon= i[3]
					stcls= i[4]
				info="studentId = "+stid+"\n Student Name = "+stnam+"\n Student Email = "+stem+"\n Student contact = "+stcon+"\n student class ="+stcls
				messagebox.showinfo('found',info)
			except:
				messagebox.showerror("error","Cannot Fetch The data")
		ent2.delete(0,END)






	def find():
		global frm5,ent1,ent2
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)
		
		lab1=Label(frm5,text='Student Id:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab1.place(relx=0.1,rely=0.05)

		ent1=Entry(frm5,font=('Monaco',15,'bold'))
		ent1.place(relx=0.35,rely=0.05,relwidth=0.4)

		lab2=Label(frm5,text='Student Name:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab2.place(relx=0.1,rely=0.15)

		ent2=Entry(frm5,font=('Monaco',15,'bold'))
		ent2.place(relx=0.35,rely=0.15,relwidth=0.4)

		Btn1=Button(frm5,text='Find by ID',font=('arial',15,'bold'),bd=1,bg='#B5B5B5',activebackground='#B5B5B5',command=find_id)
		Btn1.place(relx=0.2,rely=0.6,relheight=0.1,relwidth=0.2)

		Btn2=Button(frm5,text='Find by Name',font=('arial',15,'bold'),bd=1,bg='#B5B5B5',activebackground='#B5B5B5',command=find_Name)
		Btn2.place(relx=0.6,rely=0.6,relheight=0.1,relwidth=0.2)


	def Studentlst():
		global frm5
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

		show = "Select * from "+StudentTable+ " order by Stud_class;"

		scroll_y=Scrollbar(frm5,orient=VERTICAL)
		StdTable=ttk.Treeview(frm5,columns=('StudId','Stud_name','Stud_Email','Stud_Contact','Stud_class'),yscrollcommand=scroll_y.set)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=StdTable.yview)
		StdTable.heading("StudId",text="Id")
		StdTable.heading("Stud_name",text="Name")
		StdTable.heading("Stud_Email",text="Email")
		StdTable.heading("Stud_Contact",text="Contect")
		StdTable.heading("Stud_class",text="Class")
		StdTable["show"]="headings"
		StdTable.column("StudId",width=20)
		StdTable.column("Stud_name",width=30)
		StdTable.column("Stud_Email",width=60)
		StdTable.column("Stud_Contact",width=40)
		StdTable.column("Stud_class",width=20)
		StdTable.pack(fill=BOTH,expand=1)

		try:
			cur.execute(show)
			con.commit()
			for i in cur:
				StdTable.insert('',END,values=i)

		except:
			messagebox.showerror("Failure","Failed to fetch Data")


	def updt_id():
		global ent2,ent3,ent4,ent5,ent6
		Id=ent2.get()
		Name=ent3.get()
		Email=ent4.get()
		Contact=ent5.get()
		Clas=ent6.get()
		updt="update "+StudentTable+" set Stud_name = '"+Name+"',Stud_Email = '"+Email+"',Stud_Contact = '"+Contact+"',Stud_class = '"+Clas+"' where StudId = '"+Id+"';"
		if Id=="":
			messagebox.showerror('error',"No data in Entry box")
		else:
			try:
				con.execute(updt)
				con.commit()
				messagebox.showinfo('Success',"Data Updated successfully")
			except:
				messagebox.showerror("Error","Can't find the data")
		ent2.delete(0,END)
		ent3.delete(0,END)
		ent4.delete(0,END)
		ent5.delete(0,END)
		ent6.delete(0,END)

	def updt_nam():
		global ent2,ent3,ent4,ent5,ent6
		Id=ent2.get()
		Name=ent3.get()
		Email=ent4.get()
		Contact=ent5.get()
		Clas=ent6.get()
		updt="update "+StudentTable+" set StudId = '"+Id+"',Stud_Email = '"+Email+"',Stud_Contact = '"+Contact+"',Stud_class = '"+Clas+"' where Stud_name = '"+Name+"';"
		if Name=="":
			messagebox.showerror('error',"No data in Entry box")
		else:
			try:
				con.execute(updt)
				con.commit()
				messagebox.showinfo('Success',"Data Updated successfully")
			except:
				messagebox.showerror("Error","Can't find the data")
		ent2.delete(0,END)
		ent3.delete(0,END)
		ent4.delete(0,END)
		ent5.delete(0,END)
		ent6.delete(0,END)

	def update():
		global frm5
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

		def by_id():
			global ent2,ent3,ent4,ent5,ent6
			lab2=Label(frm5,text='Student Id:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab2.place(relx=0.1,rely=0.35)

			ent2=Entry(frm5,font=('Monaco',15,'bold'))
			ent2.place(relx=0.35,rely=0.35,relwidth=0.4)
			
			lab3=Label(frm5,text='Student Name:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab3.place(relx=0.1,rely=0.45)
			
			ent3=Entry(frm5,font=('Monaco',15,'bold'))
			ent3.place(relx=0.35,rely=0.45,relwidth=0.4)
			
			lab4=Label(frm5,text='Email:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab4.place(relx=0.1,rely=0.55)
			
			ent4=Entry(frm5,font=('Monaco',15,'bold'))
			ent4.place(relx=0.35,rely=0.55,relwidth=0.4)
			
			lab5=Label(frm5,text='Contact:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab5.place(relx=0.1,rely=0.65)
			
			ent5=Entry(frm5,font=('Monaco',15,'bold'))
			ent5.place(relx=0.35,rely=0.65,relwidth=0.4)
			
			lab6=Label(frm5,text='Class:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab6.place(relx=0.1,rely=0.75)
			
			ent6=ttk.Combobox(frm5, font=('arial', 10, 'bold'), state='readonly', width=10)
			ent6['values']=('','11','12')
			ent6.current(0)
			ent6.place(relx=0.35,rely=0.75,relwidth=0.3,relheight=0.075)
			
			Btn1=Button(frm5,text='Update',font=('Monaco',15,'bold'),bd=1,bg='#B5B5B5',activebackground='#B5B5B5',command=updt_id)
			Btn1.place(relx=0.7,rely=0.75)

		def by_name():
			lab2=Label(frm5,text='Student Id:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab2.place(relx=0.1,rely=0.35)

			ent2=Entry(frm5,font=('Monaco',15,'bold'))
			ent2.place(relx=0.35,rely=0.35,relwidth=0.4)
			
			lab3=Label(frm5,text='Student Name:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab3.place(relx=0.1,rely=0.45)
			
			ent3=Entry(frm5,font=('Monaco',15,'bold'))
			ent3.place(relx=0.35,rely=0.45,relwidth=0.4)
			
			lab4=Label(frm5,text='Email:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab4.place(relx=0.1,rely=0.55)
			
			ent4=Entry(frm5,font=('Monaco',15,'bold'))
			ent4.place(relx=0.35,rely=0.55,relwidth=0.4)
			
			lab5=Label(frm5,text='Contact:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab5.place(relx=0.1,rely=0.65)
			
			ent5=Entry(frm5,font=('Monaco',15,'bold'))
			ent5.place(relx=0.35,rely=0.65,relwidth=0.4)
			
			lab6=Label(frm5,text='Class:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab6.place(relx=0.1,rely=0.75)
			
			ent5=ttk.Combobox(frm5, font=('arial', 10, 'bold'), state='readonly', width=10)
			ent5['values']=('','11','12')
			ent5.current(0)
			ent5.place(relx=0.35,rely=0.75,relwidth=0.3,relheight=0.075)
			
			Btn1=Button(frm5,text='Update',font=('Monaco',15,'bold'),bd=1,bg='#B5B5B5',activebackground='#B5B5B5',command=updt_nam)
			Btn1.place(relx=0.7,rely=0.75)

		lab1=Label(frm5,text='Edit By:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab1.place(relx=0.1,rely=0.1)

		ent1=ttk.Combobox(frm5, font=('arial', 10, 'bold'), state='readonly', width=10)
		ent1['values']=('','Id','Name')
		ent1.current(0)
		ent1.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.075)

		def prcd():
			update=ent1.get()
			if (update=='Id'):
				by_id()
			elif (update=='Name'):
				by_name()
			else:
				messagebox.showerror('Nothing found','No field Selected')

		btn1=Button(frm5,text='Proceed',bd=3,relief=FLAT,font=('arial',10,'bold'),command=prcd)
		btn1.place(relx=0.7,rely=0.1)

	


	def delt_id():
		global ent2
		Id=ent2.get()
		dlet="delete from "+StudentTable+" where StudId = '"+Id+"';"
		if Id=="":
			messagebox.showerror('error',"No data in Entry box")
		else:
			try:
				con.execute(dlet)
				con.commit()
				messagebox.showinfo('Success',"Data deleted successfully")
			except:
				messagebox.showinfo("Error","Can't find the data")
		ent2.delete(0,END)

	def delt_nam():
		global ent2
		nam=ent2.get()
		dlet="delete from "+StudentTable+" where Stud_name = '"+nam+"';"
		if nam=="":
			messagebox.showerror('error',"No data in Entry box")
		else:
			try:
				con.execute(dlet)
				con.commit()
				messagebox.showinfo('Success',"Data deleted successfully")
			except:
				messagebox.showinfo("Error","Can't find the data")
		ent2.delete(0,END)


	def Delete():
		global frm5,ent2
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)
		lab2=''
		ent2=''
		btn=''


		def by_id():
			global ent2
			lab2=Label(frm5,text='Student Id:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab2.place(relx=0.1,rely=0.35)

			ent2=Entry(frm5,font=('Monaco',15,'bold'))
			ent2.place(relx=0.35,rely=0.35,relwidth=0.4)

			btn=Button(frm5,text='Delete',font=('Monaco',15,'bold'),bd=3,relief=FLAT,command=delt_id)
			btn.place(relx=0.4,rely=0.6)

		def by_name():
			global ent2
			lab2=Label(frm5,text='Student Name:',font=('Monaco',15,'bold'),bg='#B5B5B5')
			lab2.place(relx=0.1,rely=0.35)

			ent2=Entry(frm5,font=('Monaco',15,'bold'))
			ent2.place(relx=0.35,rely=0.35,relwidth=0.4)

			btn=Button(frm5,text='Delete',font=('Monaco',15,'bold'),bd=3,relief=FLAT,command=delt_nam)
			btn.place(relx=0.4,rely=0.6)

		lab1=Label(frm5,text='Delete By:',font=('Monaco',15,'bold'),bg='#B5B5B5')
		lab1.place(relx=0.1,rely=0.1)

		ent1=ttk.Combobox(frm5, font=('arial', 10, 'bold'), state='readonly', width=10)
		ent1['values']=('','Id','Name')
		ent1.current(0)
		ent1.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.075)

		def prcd():
			delete=ent1.get()
			if (delete=='Id'):
				by_id()
			elif (delete=='Name'):
				by_name()
			else:
				messagebox.showerror('Nothing found','No field Selected')

		btn1=Button(frm5,text='Proceed',bd=3,relief=FLAT,font=('arial',10,'bold'),command=prcd)
		btn1.place(relx=0.7,rely=0.1)

	def cls11lst():
		global frm5
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

		show = "select * from "+StudentTable+" where Stud_class = '11';"

		scroll_y=Scrollbar(frm5,orient=VERTICAL)
		StdTable=ttk.Treeview(frm5,columns=('StudId','Stud_name','Stud_Email','Stud_Contact','Stud_class'),yscrollcommand=scroll_y.set)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=StdTable.yview)
		StdTable.heading("StudId",text="Id")
		StdTable.heading("Stud_name",text="Name")
		StdTable.heading("Stud_Email",text="Email")
		StdTable.heading("Stud_Contact",text="Contect")
		StdTable.heading("Stud_class",text="Class")
		StdTable["show"]="headings"
		StdTable.column("StudId",width=20)
		StdTable.column("Stud_name",width=30)
		StdTable.column("Stud_Email",width=60)
		StdTable.column("Stud_Contact",width=40)
		StdTable.column("Stud_class",width=20)
		StdTable.pack(fill=BOTH,expand=1)

		try:
			cur.execute(show)
			con.commit()
			for i in cur:
				StdTable.insert('',END,values=i)

		except:
			messagebox.showerror("Failure","Failed to fetch Data")

	def cls12lst():
		global frm5
		close()
		frm5=Frame(frm3,bg='#B5B5B5')
		frm5.place(relx=0,rely=0,relheight=0.85,relwidth=1)

		show = "select * from "+StudentTable+" where Stud_class = '12';"

		scroll_y=Scrollbar(frm5,orient=VERTICAL)
		StdTable=ttk.Treeview(frm5,columns=('StudId','Stud_name','Stud_Email','Stud_Contact','Stud_class'),yscrollcommand=scroll_y.set)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=StdTable.yview)
		StdTable.heading("StudId",text="Id")
		StdTable.heading("Stud_name",text="Name")
		StdTable.heading("Stud_Email",text="Email")
		StdTable.heading("Stud_Contact",text="Contect")
		StdTable.heading("Stud_class",text="Class")
		StdTable["show"]="headings"
		StdTable.column("StudId",width=20)
		StdTable.column("Stud_name",width=30)
		StdTable.column("Stud_Email",width=60)
		StdTable.column("Stud_Contact",width=40)
		StdTable.column("Stud_class",width=20)
		StdTable.pack(fill=BOTH,expand=1)

		try:
			cur.execute(show)
			con.commit()
			for i in cur:
				StdTable.insert('',END,values=i)

		except:
			messagebox.showerror("Failure","Failed to fetch Data")





	"""
	Making of Working Menu
	"""
	def menu():
		btn1=Button(frm2,text='Add student',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=add)
		btn1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
		btn2=Button(frm2,text='Find student',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=find)
		btn2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
		btn3=Button(frm2,text='Student List',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=Studentlst)
		btn3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
		btn4=Button(frm2,text='Update Student',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=update)
		btn4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
		btn5=Button(frm2,text='Delete student',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=Delete)
		btn5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
		btn6=Button(frm2,text='Class 11 List',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=cls11lst)
		btn6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
		btn7=Button(frm2,text='Class 12 List',bd=0,bg='#228B22',activebackground='#228B22',font=('impact',15),command=cls12lst)
		btn7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)



	menu()

	root2.mainloop()


"""
getting details for register
"""

def gettingDetails():
    
    Id = ent1.get()
    password = ent2.get()
    try:
        if (type(int(Id)) == int):
            pass
        else:
            messagebox.showerror("Invalid Value","Unique ID should be an integer")
            return
    except:
        messagebox.showerror("Invalid Value","Unique ID should be an integer")
        return
    
    sql="insert into "+AdminTable+" values ('"+Id+"','"+password+"');"
    try:
        cur.execute(sql)
        con.commit()
        messagebox.showinfo("Success", "Successfully registered")
    except:
    	messagebox.showerror("Invalid Value","Already Exists")
    ent1.delete(0, END)
    ent2.delete(0, END)




"""
getting details for login
"""

def gettingLoginDetails(event=""):

    Id = ent1.get()
    password = ent2.get()
    sqlLoginID = "select adminId from "+AdminTable+" where Password = '"+password+"';"
    try:
        cur.execute(sqlLoginID)
        for i in cur:
            getLoginID = i[0]
        if (getLoginID == Id):
            messagebox.showinfo("SUCCESS","You have successfully logged in")
            root.destroy()
            win2()
        else:
            messagebox.showerror("Failure","Can't log in, check your credentials")
            ent1.delete(0, END)
            ent2.delete(0, END)
    except:
        messagebox.showerror("Failure","Can't find credentials")
        ent1.delete(0, END)
        ent2.delete(0, END)




"""
login frame
"""

frm1=Frame(root,bg='white')
frm1.place(relx=0.3,rely=0.4,relwidth=0.4,relheight=0.5)

lab1=Label(frm1,text='LOGIN',font=("bookman old style",35,'bold'),fg='dark Orange',bg='white')
lab1.place(relx=0.275,rely=0.05)

lab2=Label(frm1,text='UserID:',font=("impact",15),fg='black',bg='white')
lab2.place(relx=0.15,rely=0.3)

ent1=Entry(frm1,font=('arial',20))
ent1.place(relx=0.15,rely=0.4,relwidth=0.8)

lab3=Label(frm1,text='Password:',font=("impact",15),fg='black',bg='white')
lab3.place(relx=0.15,rely=0.5)

ent2=Entry(frm1,font=('arial',20),show="\u2022")
ent2.place(relx=0.15,rely=0.6,relwidth=0.8)

button2=Button(frm1,text='Register',font=('algerian',10,'bold'),bd=1,bg='White',fg='dark green',command=gettingDetails)
button2.place(relx=0.15,rely=0.8)

button3=Button(frm1,text='Login',font=('algerian',10,'bold'),bd=1,bg='White',fg='dark Red',command=gettingLoginDetails)
button3.place(relx=0.65,rely=0.8)

root.mainloop()