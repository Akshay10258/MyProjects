import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox

#WINDOWS
#MAIN WINDOW

root=Tk()
root.title("STUDENT RECORD MANAGEMENT")
root.geometry("1750x900")

stu_db=sqlite3.connect('STUDENT DATABASE.db') #CREATING DATABASE

c=stu_db.cursor() #CREATING CURSOR

#CREATING A TABLE STUDENT:
#TABLE 1:
c.execute("""CREATE TABLE if not exists student(    
    SL_NO integer,
    Name text,                                        
    SRN varchar,
    Ph_number integer,
    Cycle text)
    """)

#TABLES FOR MARKS ENTRY:
c.execute("""CREATE TABLE if not exists ISA_1 (  
    Name text,
    SRN varchar,
    sub1 integer,                                        
    sub2 integer,
    sub3 integer,
    sub4 integer,
    sub5 integer)
    """)

c.execute("""CREATE TABLE if not exists ISA_2 (    
    Name text,
    SRN varchar,
    sub1 integer,                                        
    sub2 integer,
    sub3 integer,
    sub4 integer,
    sub5 integer)
    """)

c.execute("""CREATE TABLE if not exists ESA (    
    Name text,
    SRN varchar,
    sub1 integer,                                        
    sub2 integer,
    sub3 integer,
    sub4 integer,
    sub5 integer)
    """)
#TABLE FOR ATTENDANCE ENTRY
c.execute("""CREATE TABLE if not exists ATTENDANCE (    
    Name text,
    SRN varchar,
    sub1 real,                                        
    sub2 real,
    sub3 real,
    sub4 real,
    sub5 real)
    """)

stu_db.commit()

stu_db.close()

#QUERYING THE DATABASE TABLE "STUDENT":    
def query():

    for record in stu_tview.get_children():
        stu_tview.delete(record)

    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    c.execute("SELECT rowid,* FROM student")

    records=c.fetchall()
    #print(records)

    stu_tview.tag_configure('evenrow',background='light blue')

    global count
    count=0
    for rec in records:
        if count%2==0:
            stu_tview.insert(parent='',index='end',iid=count,text="",values=(rec[0],rec[2],rec[3],rec[4],rec[5]),tags=('evenrow',))
        else:
            stu_tview.insert(parent='',index='end',iid=count,text="",values=(rec[0],rec[2],rec[3],rec[4],rec[5]),tags=('oddrow',))
        count+=1

    #print(records) IT PRINTS INTO THE TERMINAL

    stu_db.commit()

    stu_db.close()

#QUERYING THE DATABASE TABLE "ISA_1":    
def query_ISA1_MARKS():

    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    c.execute("SELECT rowid,* FROM ISA_1")

    records=c.fetchall()

    stu_db.commit()

    stu_db.close()

#QUERYING THE DATABASE TABLE "ISA_2":    
def query_ISA2_MARKS():

    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    c.execute("SELECT rowid,* FROM ISA_2")

    records=c.fetchall()

    stu_db.commit()

    stu_db.close()

#QUERYING THE DATABASE TABLE "ESA":    
def query_ESA_MARKS():
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    c.execute("SELECT rowid,* FROM ESA")

    records=c.fetchall()

    stu_db.commit()

    stu_db.close()

#MESSAGEBOXES
def wrong_marks_entry_ISA():
    messagebox.showerror("WARNING","Marks Entered Should Be Less than the total (40 marks)")

def wrong_marks_entry_ESA():
    messagebox.showerror("WARNING","Marks Entered Should Be Less than the total (100 marks)")

def wrong_attend_entry():
    messagebox.showerror("WARNING","Attended classes should be less than the Total classes")

#FETCHING ATTENDANCE
def fetch_attendance():
    att_disp=Frame(top3,bg="lightgrey")
    att_disp.place(x=25,y=150,width=570,height=400)
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR
    #fetching from student table
    req_r= "SELECT * FROM student WHERE SRN = ?"

    global stu_srn 
    stu_srn=Ent1.get()  

    c.execute(req_r, (stu_srn,))
    res = c.fetchone()

    global fetched_cyc
    global fetched_name

    fetched_cyc=res[4]
    fetched_name=res[1]

    #fetching from attendance table
    req_rec= "SELECT * FROM ATTENDANCE WHERE SRN = ?"

    global st_srn
    st_srn=Ent1.get()  

    c.execute(req_rec, (st_srn,))
    global result
    result = c.fetchone()

    #print(result)

    stu_db.commit()
    stu_db.close()

    c_la0=Label(top3,text="SUBJECTS :",font=("Algerian",20,"bold"))
    c_la0.place(x=35,y=100)


    lab2=Label(top3,text=f"Name : {fetched_name}",font=("Comic Sans MS",18,"bold"))
    lab2.grid(row=2,column=1,padx=5,pady=10)

    lab3=Label(top3,text=f"Cycle : {fetched_cyc}",font=("Comic Sans MS",18,"bold"))
    lab3.grid(row=2,column=2,padx=30,pady=10)
    
    at_percent=[result[2],result[3],result[4],result[5],result[6]]
    status="No Shortage of Attendance"
    color="green"
    for i in at_percent:
        if i<85:
            status="Shortage of attendance"
            color="red"
        else:
            pass

    if fetched_cyc=="Chemistry":

        c_la1=Label(att_disp,text="Python Programming",font=("Arial",15,"bold"))
        c_la1.grid(row=5,column=1,padx=35,pady=20)

        c_LaB1=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        c_LaB1.grid(row=5,column=3,padx=35,pady=20)

        c_La1=Label(att_disp,text=f"{result[2]} %",font=("Arial",15,"bold"))
        c_La1.grid(row=5,column=5,padx=35,pady=20)

        c_la2=Label(att_disp,text="Engg.Mechanics",font=("Arial",15,"bold"))
        c_la2.grid(row=7,column=1,padx=35,pady=20)

        c_LaB2=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        c_LaB2.grid(row=7,column=3,padx=35,pady=20)

        c_La2=Label(att_disp,text=f"{result[3]} %",font=("Arial",15,"bold"))
        c_La2.grid(row=7,column=5,padx=35,pady=20)

        c_la3=Label(att_disp,text="Engg.Chemistry",font=("Arial",15,"bold"))
        c_la3.grid(row=9,column=1,padx=35,pady=20)

        c_LaB3=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        c_LaB3.grid(row=9,column=3,padx=35,pady=20)

        c_La3=Label(att_disp,text=f"{result[3]} %",font=("Arial",15,"bold"))
        c_La3.grid(row=9,column=5,padx=35,pady=20)

        c_la4=Label(att_disp,text="Elec.Principles & Devices",font=("Arial",15,"bold"))
        c_la4.grid(row=11,column=1,padx=35,pady=20)

        c_LaB4=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        c_LaB4.grid(row=11,column=3,padx=35,pady=20)

        c_La4=Label(att_disp,text=f"{result[4]} %",font=("Arial",15,"bold"))
        c_La4.grid(row=11,column=5,padx=35,pady=20)

        c_la6=Label(att_disp,text="Engg.Mathematics",font=("Arial",15,"bold"))
        c_la6.grid(row=13,column=1,padx=35,pady=20)

        c_LaB6=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        c_LaB6.grid(row=13,column=3,padx=35,pady=20)

        c_La6=Label(att_disp,text=f"{result[5]} %",font=("Arial",15,"bold"))
        c_La6.grid(row=13,column=5,padx=35,pady=20)

        c_status=Label(att_disp,text=f"Status of attedence : {status}",font=("Arial",15,"bold"),fg=f"{color}4",bg=f"{color}1")
        c_status.place(x=65,y=350)

    else:
        p_la1=Label(att_disp,text="Python Programming",font=("Arial",15,"bold"))
        p_la1.grid(row=5,column=1,padx=35,pady=20)

        p_LaB1=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        p_LaB1.grid(row=5,column=3,padx=35,pady=20)

        p_La1=Label(att_disp,text=f"{result[2]} %",font=("Arial",15,"bold"))
        p_La1.grid(row=5,column=5,padx=35,pady=20)

        p_la2=Label(att_disp,text="Engg.Mechanical",font=("Arial",15,"bold"))
        p_la2.grid(row=7,column=1,padx=35,pady=20)

        p_LaB2=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        p_LaB2.grid(row=7,column=3,padx=35,pady=20)

        p_La2=Label(att_disp,text=f"{result[3]} %",font=("Arial",15,"bold"))
        p_La2.grid(row=7,column=5,padx=35,pady=20)

        p_la3=Label(att_disp,text="Engg.Physics",font=("Arial",15,"bold"))
        p_la3.grid(row=9,column=1,padx=35,pady=20)

        p_LaB3=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        p_LaB3.grid(row=9,column=3,padx=35,pady=20)

        p_La3=Label(att_disp,text=f"{result[3]} %",font=("Arial",15,"bold"))
        p_La3.grid(row=9,column=5,padx=35,pady=20)

        p_la4=Label(att_disp,text="Electricals",font=("Arial",15,"bold"))
        p_la4.grid(row=11,column=1,padx=35,pady=20)

        p_LaB4=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        p_LaB4.grid(row=11,column=3,padx=35,pady=20)

        p_La4=Label(att_disp,text=f"{result[4]} %",font=("Arial",15,"bold"))
        p_La4.grid(row=11,column=5,padx=35,pady=20)

        p_la6=Label(att_disp,text="Engg.Mathematics",font=("Arial",15,"bold"))
        p_la6.grid(row=13,column=1,padx=35,pady=20)

        p_LaB6=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
        p_LaB6.grid(row=13,column=3,padx=35,pady=20)

        p_La6=Label(att_disp,text=f"{result[5]} %",font=("Arial",15,"bold"))
        p_La6.grid(row=13,column=5,padx=35,pady=20)

        p_status=Label(att_disp,text=f"Status of attedence : {status}",font=("Arial",15,"bold"),fg=f"{color}4",bg=f"{color}1")
        p_status.place(x=65,y=350)

#FETCHING MARKS

def fetch_marks():
    att_disp=Frame(top4,bg="lightgrey")
    att_disp.place(x=120,y=100,width=580,height=520)
    def display():
        if fetched_cyc=="Chemistry":
            c_la1=Label(att_disp,text="Python Programming",font=("Arial",15,"bold"))
            c_la1.grid(row=5,column=1,padx=35,pady=35)

            c_LaB1=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            c_LaB1.grid(row=5,column=3,padx=35,pady=35)

            c_La1=Label(att_disp,text=f"{result[2]}",font=("Arial",15,"bold"))
            c_La1.grid(row=5,column=5,padx=35,pady=35)

            c_la2=Label(att_disp,text="Engg.Mechanics",font=("Arial",15,"bold"))
            c_la2.grid(row=7,column=1,padx=35,pady=35)

            c_LaB2=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            c_LaB2.grid(row=7,column=3,padx=35,pady=35)

            c_La2=Label(att_disp,text=f"{result[3]}",font=("Arial",15,"bold"))
            c_La2.grid(row=7,column=5,padx=35,pady=35)

            c_la3=Label(att_disp,text="Engg.Chemistry",font=("Arial",15,"bold"))
            c_la3.grid(row=9,column=1,padx=35,pady=35)

            c_LaB3=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            c_LaB3.grid(row=9,column=3,padx=35,pady=35)

            c_La3=Label(att_disp,text=f"{result[3]}",font=("Arial",15,"bold"))
            c_La3.grid(row=9,column=5,padx=35,pady=35)

            c_la4=Label(att_disp,text="Elec.Principles & Devices",font=("Arial",15,"bold"))
            c_la4.grid(row=11,column=1,padx=35,pady=35)

            c_LaB4=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            c_LaB4.grid(row=11,column=3,padx=35,pady=35)

            c_La4=Label(att_disp,text=f"{result[4]}",font=("Arial",15,"bold"))
            c_La4.grid(row=11,column=5,padx=35,pady=35)

            c_la6=Label(att_disp,text="Engg.Mathematics",font=("Arial",15,"bold"))
            c_la6.grid(row=13,column=1,padx=35,pady=35)

            c_LaB6=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            c_LaB6.grid(row=13,column=3,padx=35,pady=35)

            c_La6=Label(att_disp,text=f"{result[5]}",font=("Arial",15,"bold"))
            c_La6.grid(row=13,column=5,padx=35,pady=35)

        else:
            p_la1=Label(att_disp,text="Python Programming",font=("Arial",15,"bold"))
            p_la1.grid(row=5,column=1,padx=35,pady=35)

            p_LaB1=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            p_LaB1.grid(row=5,column=3,padx=35,pady=35)

            p_La1=Label(att_disp,text=f"{result[2]}",font=("Arial",15,"bold"))
            p_La1.grid(row=5,column=5,padx=35,pady=35)

            p_la2=Label(att_disp,text="Engg.Mechanical",font=("Arial",15,"bold"))
            p_la2.grid(row=7,column=1,padx=35,pady=35)

            p_LaB2=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            p_LaB2.grid(row=7,column=3,padx=35,pady=35)

            p_La2=Label(att_disp,text=f"{result[3]}",font=("Arial",15,"bold"))
            p_La2.grid(row=7,column=5,padx=35,pady=35)

            p_la3=Label(att_disp,text="Engg.Physics",font=("Arial",15,"bold"))
            p_la3.grid(row=9,column=1,padx=35,pady=35)

            p_LaB3=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            p_LaB3.grid(row=9,column=3,padx=35,pady=35)

            p_La3=Label(att_disp,text=f"{result[3]}",font=("Arial",15,"bold"))
            p_La3.grid(row=9,column=5,padx=35,pady=35)

            p_la4=Label(att_disp,text="Electricals",font=("Arial",15,"bold"))
            p_la4.grid(row=11,column=1,padx=35,pady=35)

            p_LaB4=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            p_LaB4.grid(row=11,column=3,padx=35,pady=35)

            p_La4=Label(att_disp,text=f"{result[4]}",font=("Arial",15,"bold"))
            p_La4.grid(row=11,column=5,padx=35,pady=35)

            p_la6=Label(att_disp,text="Engg.Mathematics",font=("Arial",15,"bold"))
            p_la6.grid(row=13,column=1,padx=35,pady=35)

            p_LaB6=Label(att_disp,text=":",font=("Arial",15,"bold"),bg="lightgrey")
            p_LaB6.grid(row=13,column=3,padx=35,pady=35)

            p_La6=Label(att_disp,text=f"{result[5]}",font=("Arial",15,"bold"))
            p_La6.grid(row=13,column=5,padx=35,pady=35)

    
    def disp_marks():
        if E_TYPE=="ISA-1":

            stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

            c=stu_db.cursor() #CREATING CURSOR

            req_record= "SELECT * FROM ISA_1 WHERE SRN = ?"
            c.execute(req_record, (stu_srn,))
            global result
            result = c.fetchone()

            display()

            stu_db.commit()

            stu_db.close()

        elif E_TYPE=="ISA-2":

            stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

            c=stu_db.cursor() #CREATING CURSOR
            req_record= "SELECT * FROM ISA_2 WHERE SRN = ?"
            c.execute(req_record, (stu_srn,))
            result = c.fetchone()

            #print(result)
            display()

            stu_db.commit()

            stu_db.close()
        else:

            stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

            c=stu_db.cursor() #CREATING CURSOR
            req_record= "SELECT * FROM ESA WHERE SRN = ?"
            c.execute(req_record, (stu_srn,))
            result = c.fetchone()

            #print(result)
            display()

            stu_db.commit()

            stu_db.close()

            
    disp_marks()

def get_button():
    global B_TYPE
    B_TYPE=BUT1.cget('text') 

def get_exam_for_ISA1():
    global E_TYPE
    E_TYPE=BUT1.cget('text')

def get_exam_for_ISA2():
    global E_TYPE
    E_TYPE=BUT2.cget('text')

def get_exam_for_ESA():
    global E_TYPE
    E_TYPE=BUT3.cget('text')      


def attend_display():
    global top3
    top3=Toplevel()
    top3.title("ATTENDANCE DISPLAY")
    top3.geometry("620x600")

    Lab1=Label(top3,text="Enter SRN",font=("Arial",20,"bold"))
    Lab1.grid(row=1,column=1)

    global Ent1
    Ent1=Entry(top3,font=("Arial",20,"bold"),)
    Ent1.grid(row=1,column=2,padx=2)

    But1=Button(top3,text="OK",font=("Arial",12,"bold"),command=fetch_attendance)
    But1.grid(row=1,column=3)

    top3.mainloop()

def marks_display():
    global top4
    top4=Toplevel()
    top4.title("MARKS DISPLAY")
    top4.geometry("720x640")

    Lab1=Label(top4,text="Enter SRN",font=("Arial",20,"bold"))
    Lab1.grid(row=1,column=1)

    global Ent1
    Ent1=Entry(top4,font=("Arial",20,"bold"),)
    Ent1.grid(row=1,column=2,padx=2)

    def exam_type_display():
        global BUT1
        BUT1=Button(top4,text="ISA-1",font=("Arial",20,"bold"),command=lambda:[get_exam_for_ISA1(),fetch_marks()])
        BUT1.place(x=10,y=200)
        global BUT2
        BUT2=Button(top4,text="ISA-2",font=("Arial",20,"bold"),command=lambda:[get_exam_for_ISA2(),fetch_marks()])
        BUT2.place(x=10,y=300)
        global BUT3
        BUT3=Button(top4,text="ESA",font=("Arial",20,"bold"),command=lambda:[get_exam_for_ESA(),fetch_marks()])
        BUT3.place(x=10,y=400)

        stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

        c=stu_db.cursor() #CREATING CURSOR
        #fetching from student table
        global stu_srn 
        stu_srn=Ent1.get()  

        req_r= "SELECT * FROM student WHERE SRN = ?"

        c.execute(req_r, (stu_srn,))
        res = c.fetchone()

        global fetched_cyc
        global fetched_name

        fetched_cyc=res[4]
        fetched_name=res[1]

        lab2=Label(top4,text=f"Name : {fetched_name}",font=("Comic Sans MS",18,"bold"))
        lab2.grid(row=2,column=1,padx=5,pady=10)

        lab3=Label(top4,text=f"Cycle : {fetched_cyc}",font=("Comic Sans MS",18,"bold"))
        lab3.grid(row=2,column=2,padx=30,pady=10)

    But4=Button(top4,text="OK",font=("Arial",12,"bold"),command=exam_type_display)
    But4.grid(row=1,column=3)

    top4.mainloop()

#CREATING ATTENDANCE SHORTAGE WINDOW
def attendance_shortage_wind():
    global top5
    top5=Toplevel()
    top5.title("ATTENDANCE SHORTAGE LIST")
    top5.geometry("600x700")

    Name_list=[]
    Srn_list=[]
    count_list=[]
    for l in shortage_list:
        Name_list.append(l[0])
        Srn_list.append(l[1])
        count_list.append(str(l[2]))

    #print(Name_list)
    #print(Srn_list)
    #print(count_list)

    Name_list_as_string='\n'.join(Name_list)
    Srn_list_as_string='\n'.join(Srn_list)
    count_list_as_string='\n'.join(count_list)

    head1=Label(top5,text="NAME",font=('Arial,20'))
    head1.grid(row=1,column=1,padx=40,pady=15)

    head2=Label(top5,text="SRN",font=('Arial,20'))
    head2.grid(row=1,column=3,padx=40,pady=15)

    head3=Label(top5,text="No of subjects",font=('Arial,20'))
    head3.grid(row=1,column=5,padx=40,pady=15)

    name_lab=Label(top5,text=Name_list_as_string,font=('Arial,15'))
    name_lab.grid(row=3,column=1,padx=40,pady=15)

    srn_lab=Label(top5,text=Srn_list_as_string,font=('Arial,15'))
    srn_lab.grid(row=3,column=3,padx=40,pady=15)

    count_lab=Label(top5,text=count_list_as_string,font=('Arial,15'))
    count_lab.grid(row=3,column=5,padx=40,pady=15)

    top5.mainloop()

#CREATING HIGHEST ATTENDANCE WINDOW
def highest_attendance_wind():

    global top6
    top6=Toplevel()
    top6.title("ATTENDANCE SHORTAGE LIST")
    top6.geometry("790x700")

    Name_list=[]
    Srn_list=[]
    count_list=[]
    for l in greater_than_95:
        Name_list.append(l[0])
        Srn_list.append(l[1])
        count_list.append(str(l[2]))
    Name_list_as_string='\n'.join(Name_list)
    Srn_list_as_string='\n'.join(Srn_list)
    count_list_as_string='\n'.join(count_list)

    head1=Label(top6,text="NAME",font=('Arial',18,"bold"))
    head1.grid(row=2,column=1,padx=50,pady=37)

    head2=Label(top6,text="SRN",font=('Arial',18,"bold"))
    head2.grid(row=2,column=3,padx=50,pady=37)

    head3=Label(top6,text="No of subjects",font=('Arial',18,"bold"))
    head3.grid(row=2,column=5,padx=50,pady=37)
    
    head4=Label(top6,text="STUDENTS WITH ATTENDANCE GREATER THAN 95% :",font=('Helvetica',20,"bold"),fg="darkgreen",bg="lightgreen")
    head4.place(x=40,y=2)
    
    name_lab=Label(top6,text=Name_list_as_string,font=('Arial',15))
    name_lab.grid(row=5,column=1,padx=50,pady=15)

    srn_lab=Label(top6,text=Srn_list_as_string,font=('Arial',15))
    srn_lab.grid(row=5,column=3,padx=50,pady=15)

    count_lab=Label(top6,text=count_list_as_string,font=('Arial',15))
    count_lab.grid(row=5,column=5,padx=50,pady=15)

    top6.mainloop()

def get_cycle_for_srn():
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    #GETTING THE ENTIRE RECORD OF THE INPUT SRN
    required_rec= "SELECT * FROM student WHERE SRN = ?"
    
    global stu_srn
    stu_srn=str(srn)

    c.execute(required_rec, (stu_srn,))
    resu = c.fetchone()
    
    global fetched_cyc
    fetched_cyc=resu[4]

    stu_db.commit()
    stu_db.close()


def top_perf_sub():
    global srn
    for r in resu2:
        s1=[r[0],r[2]]
        srn=r[1]
        get_cycle_for_srn()
        if fetched_cyc=="Chemistry":
            sub1c.append(s1)
        else:
            sub1p.append(s1)

    for r in resu3:
        s2=[r[0],r[3]]
        srn=r[1]
        get_cycle_for_srn()
        if fetched_cyc=="Chemistry":
            sub2c.append(s2)
        else:
            sub2p.append(s2)

    for r in resu4:
        s3=[r[0],r[4]]
        srn=r[1]
        get_cycle_for_srn()
        if fetched_cyc=="Chemistry":
            sub3c.append(s3)
        else:
            sub3p.append(s3)

    for r in resu5:
        s4=[r[0],r[5]]
        srn=r[1]
        get_cycle_for_srn()
        if fetched_cyc=="Chemistry":
            sub4c.append(s4)
        else:
            sub4p.append(s4)

    for r in resu6:
        s5=[r[0],r[6]]
        srn=r[1]
        get_cycle_for_srn()
        if fetched_cyc=="Chemistry":
            sub5c.append(s5)
        else:
            sub5p.append(s5)

    #print(sub1c)
    #print(sub2c)
    #print(sub3c)
    #print(sub4c)
    #print(sub5c)


#Creating top performers window:
def top_performers_window():

    global top7
    top7=Toplevel()
    top7.title("Top performers")
    top7.geometry("1600x900")

    def repeat_frame():
        global fr1  
        fr1=Frame(top7,borderwidth=5,bg="darkgrey")
        fr1.place(x=20,y=85,width=1550,height=800)

        fr2=Frame(top7,borderwidth=2,bg="lightgrey")
        fr2.place(x=20,y=160,width=1550,height=50)

        fr3=Frame(top7,borderwidth=2,bg="lightgrey")
        fr3.place(x=20,y=525,width=1550,height=50)

        name_lab=Label(fr1,text="Chem Cycle :",font=('Algerian',25))
        name_lab.grid(row=1,column=1,padx=50,pady=15)

        name_lab=Label(fr1,text="Phy Cycle :",font=('Algerian',25))
        name_lab.place(x=50,y=380)

        S1_lab=Label(fr2,text="Python Programming",font=('Algerian',15))
        S1_lab.grid(row=1,column=1,padx=45,pady=10)
        S2_lab=Label(fr2,text="Engg.Mechanics",font=('Algerian',15))
        S2_lab.grid(row=1,column=2,padx=45,pady=10)
        S3_lab=Label(fr2,text="Engg.Chemistry",font=('Algerian',15))
        S3_lab.grid(row=1,column=3,padx=45,pady=10)
        S4_lab=Label(fr2,text="Elec.Princ & Devices",font=('Algerian',15))
        S4_lab.grid(row=1,column=4,padx=45,pady=10)
        S5_lab=Label(fr2,text="Engg.Mathematics",font=('Algerian',15))
        S5_lab.grid(row=1,column=5,padx=45,pady=10)

        S1p_lab=Label(fr3,text="Python Programming",font=('Algerian',15))
        S1p_lab.grid(row=1,column=1,padx=45,pady=10)
        S2p_lab=Label(fr3,text="Engg.Mechanical",font=('Algerian',15))
        S2p_lab.grid(row=1,column=2,padx=45,pady=10)
        S3p_lab=Label(fr3,text="Engg.Physics",font=('Algerian',15))
        S3p_lab.grid(row=1,column=3,padx=45,pady=10)
        S4p_lab=Label(fr3,text="Electricals",font=('Algerian',15))
        S4p_lab.grid(row=1,column=4,padx=45,pady=10)
        S5p_lab=Label(fr3,text="Engg.Mathematics",font=('Algerian',15))
        S5p_lab.grid(row=1,column=5,padx=45,pady=10)


    #Called using buttons of the same window :
    def top_perf_get_db():
        stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

        c=stu_db.cursor()
        global resu2
        global resu3
        global resu4
        global resu5
        global resu6
        global sub1c
        global sub1p
        global sub2c
        global sub2p
        global sub3c
        global sub3p
        global sub4c
        global sub4p
        global sub5c
        global sub5p
        global mm
        if E_TYPE=="ISA-1":

            
            c.execute('''
                SELECT * FROM ISA_1 WHERE sub1 >= 30 ''')
            resu2=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_1 WHERE sub2 >= 30 ''')      
            resu3=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_1 WHERE sub3 >= 30 ''')       
            resu4=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_1 WHERE sub4 >= 30 ''')        
            resu5=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_1 WHERE sub5 >= 30 ''')      
            resu6=c.fetchall()

            mm=30

            sub1c=[]
            sub1p=[]

            sub2c=[]
            sub2p=[]
                    
            sub3c=[]
            sub3p=[]
                    
            sub4c=[]
            sub4p=[]
                    
            sub5c=[]
            sub5p=[]

            #print(resu2)
            top_perf_sub()
        elif E_TYPE=="ISA-2":
            
            
            c.execute('''
                SELECT * FROM ISA_2 WHERE sub1 >= 30 ''')
            resu2=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_2 WHERE sub2 >= 30 ''')
            resu3=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_2 WHERE sub3 >= 30 ''')
            resu4=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_2 WHERE sub4 >= 30 ''')
            resu5=c.fetchall()

            c.execute('''
                SELECT * FROM ISA_2 WHERE sub5 >= 30 ''')
            resu6=c.fetchall()
            
            mm=30

            sub1c=[]
            sub1p=[]
            
            sub2c=[]
            sub2p=[]
                    
            sub3c=[]
            sub3p=[]
                    
            sub4c=[]
            sub4p=[]
                    
            sub5c=[]
            sub5p=[]

            #print(resu2)
            top_perf_sub()
        else:
            
            c.execute('''
                SELECT * FROM ESA WHERE sub1 >= 80 ''')
            resu2=c.fetchall()

            c.execute('''
                SELECT * FROM ESA WHERE sub2 >= 80 ''')
            resu3=c.fetchall()

            c.execute('''
                SELECT * FROM ESA WHERE sub3 >= 80 ''')
            resu4=c.fetchall()

            c.execute('''
                SELECT * FROM ESA WHERE sub4 >= 80 ''')
            resu5=c.fetchall()

            c.execute('''
                SELECT * FROM ESA WHERE sub5 >= 80 ''')
            resu6=c.fetchall()
            mm=80

            sub1c=[]
            sub1p=[]
                    
            sub2c=[]
            sub2p=[]
                    
            sub3c=[]
            sub3p=[]
                    
            sub4c=[]
            sub4p=[]
                    
            sub5c=[]
            sub5p=[]

            #print(resu2)
            top_perf_sub()
        stu_db.commit()
        stu_db.close()

        print(sub1c)
        print(sub1p)
        #FOR CHEM CYCLE SUBJ
        S1C_Name_list=[]
        M1C_marks_list=[]
        for l in sub1c:
            S1C_Name_list.append(l[0])
            M1C_marks_list.append(str(l[1]))

        S2C_Name_list=[]
        M2C_marks_list=[]
        for l in sub2c:
            S2C_Name_list.append(l[0])
            M2C_marks_list.append(str(l[1]))

        S3C_Name_list=[]
        M3C_marks_list=[]
        for l in sub3c:
            S3C_Name_list.append(l[0])
            M3C_marks_list.append(str(l[1]))

        S4C_Name_list=[]
        M4C_marks_list=[]
        for l in sub4c:
            S4C_Name_list.append(l[0])
            M4C_marks_list.append(str(l[1]))

        S5C_Name_list=[]
        M5C_marks_list=[]
        for l in sub5c:
            S5C_Name_list.append(l[0])
            M5C_marks_list.append(str(l[1]))

        S1C_Name_string='\n'.join(S1C_Name_list)
        M1C_Marks_string='\n'.join(M1C_marks_list)

        S2C_Name_string='\n'.join(S2C_Name_list)
        M2C_Marks_string='\n'.join(M2C_marks_list)

        S3C_Name_string='\n'.join(S3C_Name_list)
        M3C_Marks_string='\n'.join(M3C_marks_list)

        S4C_Name_string='\n'.join(S4C_Name_list)
        M4C_Marks_string='\n'.join(M4C_marks_list)

        S5C_Name_string='\n'.join(S5C_Name_list)
        M5C_Marks_string='\n'.join(M5C_marks_list)


        #FOR C CYCLE
        Name1_lab=Label(fr1,text=S1C_Name_string,font=('Arial',15),bg="darkgrey")
        Name1_lab.place(x=40,y=150)
        
        Marks1_lab=Label(fr1,text=M1C_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks1_lab.place(x=230,y=150)

        Name2_lab=Label(fr1,text=S2C_Name_string,font=('Arial',15),bg="darkgrey")
        Name2_lab.place(x=370,y=150)

        Marks2_lab=Label(fr1,text=M2C_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks2_lab.place(x=500,y=150)
        
        Name3_lab=Label(fr1,text=S3C_Name_string,font=('Arial',15),bg="darkgrey")
        Name3_lab.place(x=620,y=150)

        Marks3_lab=Label(fr1,text=M3C_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks3_lab.place(x=770,y=150)
        
        Name4_lab=Label(fr1,text=S4C_Name_string,font=('Arial',15),bg="darkgrey")
        Name4_lab.place(x=880,y=150)

        Marks4_lab=Label(fr1,text=M4C_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks4_lab.place(x=1050,y=150)
        
        Name5_lab=Label(fr1,text=S5C_Name_string,font=('Arial',15),bg="darkgrey")
        Name5_lab.place(x=1180,y=150)

        Marks5_lab=Label(fr1,text=M5C_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks5_lab.place(x=1380,y=150)

        #FOR PHY CYCLE SUBJ
        S1P_Name_list=[]
        M1P_marks_list=[]
        for l in sub1p:
            S1P_Name_list.append(l[0])
            M1P_marks_list.append(str(l[1]))

        S2P_Name_list=[]
        M2P_marks_list=[]
        for l in sub2p:
            S2P_Name_list.append(l[0])
            M2P_marks_list.append(str(l[1]))

        S3P_Name_list=[]
        M3P_marks_list=[]
        for l in sub3p:
            S3P_Name_list.append(l[0])
            M3P_marks_list.append(str(l[1]))

        S4P_Name_list=[]
        M4P_marks_list=[]
        for l in sub4p:
            S4P_Name_list.append(l[0])
            M4P_marks_list.append(str(l[1]))

        S5P_Name_list=[]
        M5P_marks_list=[]
        for l in sub5p:
            S5P_Name_list.append(l[0])
            M5P_marks_list.append(str(l[1]))

        S1P_Name_string='\n'.join(S1P_Name_list)
        M1P_Marks_string='\n'.join(M1P_marks_list)

        S2P_Name_string='\n'.join(S2P_Name_list)
        M2P_Marks_string='\n'.join(M2P_marks_list)

        S3P_Name_string='\n'.join(S3P_Name_list)
        M3P_Marks_string='\n'.join(M3P_marks_list)

        S4P_Name_string='\n'.join(S4P_Name_list)
        M4P_Marks_string='\n'.join(M4P_marks_list)

        S5P_Name_string='\n'.join(S5P_Name_list)
        M5P_Marks_string='\n'.join(M5P_marks_list)

        #LABELS FOR P CYCLE
        Name1P_lab=Label(fr1,text=S1P_Name_string,font=('Arial',15),bg="darkgrey")
        Name1P_lab.place(x=40,y=550)
        
        Marks1P_lab=Label(fr1,text=M1P_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks1P_lab.place(x=230,y=550)

        Name2P_lab=Label(fr1,text=S2P_Name_string,font=('Arial',15),bg="darkgrey")
        Name2P_lab.place(x=370,y=550)

        Marks2P_lab=Label(fr1,text=M2P_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks2P_lab.place(x=500,y=550)
        
        Name3P_lab=Label(fr1,text=S3P_Name_string,font=('Arial',15),bg="darkgrey")
        Name3P_lab.place(x=620,y=550)

        Marks3P_lab=Label(fr1,text=M3P_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks3P_lab.place(x=770,y=550)
        
        Name4P_lab=Label(fr1,text=S4P_Name_string,font=('Arial',15),bg="darkgrey")
        Name4P_lab.place(x=860,y=550)

        Marks4P_lab=Label(fr1,text=M4P_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks4P_lab.place(x=990,y=550)
        
        Name5P_lab=Label(fr1,text=S5P_Name_string,font=('Arial',15),bg="darkgrey")
        Name5P_lab.place(x=1100,y=550)

        Marks5P_lab=Label(fr1,text=M5P_Marks_string,font=('Arial',15),bg="darkgrey")
        Marks5P_lab.place(x=1280,y=550)
        
    global BUT1
    BUT1=Button(top7,text="ISA-1",font=("Arial",30),command=lambda:[get_exam_for_ISA1(),repeat_frame(),top_perf_get_db()])
    BUT1.grid(row=1,column=1,padx=50,pady=10)
    global BUT2
    BUT2=Button(top7,text="ISA-2",font=("Arial",30),command=lambda:[get_exam_for_ISA2(),repeat_frame(),top_perf_get_db()])
    BUT2.grid(row=1,column=4,padx=50,pady=10)
    global BUT3
    BUT3=Button(top7,text="ESA",font=("Arial",30),command=lambda:[get_exam_for_ESA(),repeat_frame(),top_perf_get_db()])
    BUT3.grid(row=1,column=6,padx=50,pady=10)
    


    top7.mainloop()



#defining toggle menu
def toggle_menu():

    #defining collapse toggle
    def collapse_toggle_menu():
        tmf.destroy()
        toggle_btn.config(text="☰")
        toggle_btn.config(command=toggle_menu)


 #toggle menu frame
    tmf=Frame(root,bg="lightgrey")

    attendance_btn=Button(tmf,text="Attendance Display",fg="white",font=("bold",20),bd=0,bg="darkgrey",activebackground="blue",activeforeground="black",command=attend_display)
    attendance_btn.place(x=10,y=20,width=280)

    marks_btn=Button(tmf,text="Marks Display",fg="white",font=("bold",20),bd=0,bg="darkgrey",activebackground="blue",activeforeground="black",command=marks_display)
    marks_btn.place(x=10,y=80,width=280)
    

    def list_display():
        options=[" Attendance shortage "," Highest attendance "," Top performers "]
        analy_list=Listbox(tmf,bg="darkgrey")
        analy_list.place(x=10,y=200,width=280,height=180)

        
        for item in options:
            analy_list.insert(END, item)

        def class_analytics(event):
            if analy_list.get(ANCHOR)==" Attendance shortage ":
                stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                c=stu_db.cursor() #CREATING CURSOR
                min_att=80
                c.execute('''
                    SELECT * FROM ATTENDANCE WHERE sub1 < ? OR sub2 < ? OR sub3 < ? OR sub4 < ? OR sub5 < ? ''',
                    (min_att,min_att,min_att,min_att,min_att))

                resu=c.fetchall()

                global shortage_list
                shortage_list=[]
                for r in resu:
                    count=0
                    for i in range(2,7):
                        if r[i]<80:
                            count+=1
                        else:
                            pass
                    #print(r[0])
                    #print(r[1])
                    #print(count)
                    s_list=[r[0],r[1],count]
                    shortage_list.append(s_list)

                #print(shortage_list)
                stu_db.commit()

                stu_db.close()

                attendance_shortage_wind()
            elif analy_list.get(ANCHOR)==" Highest attendance ":
                stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                c=stu_db.cursor()

                high_att1=95
                c.execute('''
                    SELECT * FROM ATTENDANCE WHERE sub1 >= ? OR sub2 >= ? OR sub3 >= ? OR sub4 >= ? OR sub5 >= ? ''',
                    (high_att1,high_att1,high_att1,high_att1,high_att1))

                resu1=c.fetchall()

                global greater_than_95
                greater_than_95=[]
                for r in resu1:
                    count=0
                    for i in range(2,7):
                        if r[i]>=95:
                            count+=1
                        else:
                            pass
                    #print(r[0])
                    #print(r[1])
                    #print(count)

                    h1_list=[r[0],r[1],count]
                    greater_than_95.append(h1_list)
                #print(greater_than_95)
                stu_db.commit()
                stu_db.close()

                highest_attendance_wind()
            elif analy_list.get(ANCHOR)==" Top performers ":

                stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                c=stu_db.cursor()
                g1=30
                c.execute('''
                    SELECT * FROM ISA_1 WHERE sub1 >= 30 ''')
                global resu2
                resu2=c.fetchall()

                c.execute('''
                    SELECT * FROM ISA_1 WHERE sub2 >= 30 ''')
                global resu3
                resu3=c.fetchall()

                c.execute('''
                    SELECT * FROM ISA_1 WHERE sub3 >= 30 ''')
                global resu4
                resu4=c.fetchall()

                c.execute('''
                    SELECT * FROM ISA_1 WHERE sub4 >= 30 ''')
                global resu5
                resu5=c.fetchall()

                c.execute('''
                    SELECT * FROM ISA_1 WHERE sub5 >= 30 ''')
                global resu6
                resu6=c.fetchall()

                global sub1
                sub1=[]
                global sub2
                sub2=[]
                global sub3
                sub3=[]
                global sub4
                sub4=[]
                global sub5
                sub5=[]


                #print(resu2)
                top_performers_window()
                top_perf_sub()
                
  


        analy_list.configure(font=("Arial",20),fg="white",bd=0)
        analy_list.bind("<<ListboxSelect>>", class_analytics)

    class_analy_btn=Button(tmf,text="Class Analytics",font=("Arial",20),bg="darkgrey",fg="white",bd=0,command=list_display)
    class_analy_btn.place(x=10,y=140,width=280)
    
    window_height=root.winfo_height()

    tmf.place(x=0,y=82,height=window_height,width="300")
    toggle_btn.config(text="X")
    toggle_btn.config(command=collapse_toggle_menu)

f1=Frame(root,bg="black",highlightbackground="white",highlightthickness=1,borderwidth=0)
toggle_btn=Button(f1,text="☰",fg="black",bg="lightgrey",font=('bold',40),bd=0,activebackground="lightgrey",activeforeground="black",command=toggle_menu)
toggle_btn.pack(side=LEFT)

mainlable=Label(f1,text="STUDENT RECORD MANAGEMENT SYSTEM",font=("Algerian",40,"bold"),border=10,width=1000,height=80,bg="lightgrey",fg="Black")
mainlable.pack(side=TOP)


f1.pack(side=TOP,fill='x')
f1.pack_propagate(False)
f1.configure(height=80)     

def get_cycle_marks():
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    #GETTING THE ENTIRE RECORD OF THE INPUT SRN
    req_rec= "SELECT * FROM student WHERE SRN = ?"

    global st_srn ####
    st_srn=ent1.get()  

    c.execute(req_rec, (st_srn,))
    result = c.fetchone()

    global fetched_cyc
    global fetched_name

    fetched_cyc=result[4]
    fetched_name=result[1]

    #TO PRINT THE CYCLE OF THE RECORD
    #print(result[4])

    lab2=Label(top1,text=f"Name of student : {fetched_name}",font=("Comic Sans MS",18,"bold"))
    lab2.grid(row=2,column=2,padx=20,pady=10)

    lab3=Label(top1,text=f"Cycle : {fetched_cyc}",font=("Comic Sans MS",18,"bold"))
    lab3.grid(row=2,column=3,padx=20,pady=10)


    stu_db.commit()


    stu_db.close()

def get_cycle_attendance():
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    #GETTING THE ENTIRE RECORD OF THE INPUT SRN
    req_rec= "SELECT * FROM student WHERE SRN = ?"

    global st_srn
    st_srn=Ent1.get()  

    c.execute(req_rec, (st_srn,))
    result = c.fetchone()


    global fetched_cyc
    global fetched_name

    fetched_cyc=result[4]
    fetched_name=result[1]

    #TO PRINT THE CYCLE OF THE RECORD
    #print(result[4])

    lab2=Label(top2,text=f"Name of student : {fetched_name}",font=("Comic Sans MS",18,"bold"))
    lab2.grid(row=2,column=2,padx=20,pady=10)

    lab3=Label(top2,text=f"Cycle : {fetched_cyc}",font=("Comic Sans MS",18,"bold"))
    lab3.grid(row=2,column=3,padx=20,pady=10)


    stu_db.commit()

    stu_db.close()

def create_mframe():
    global marks_frame
    marks_frame=LabelFrame(top1,text="Marks Entry Field",font=("Arial",15,"bold"),border=5,width=300) #DATA ENTRY DRAME
    marks_frame.place(x=170,y=120,width=700,height=300)
def create_aframe():
    global attendance_frame
    attendance_frame=LabelFrame(top2,text="Attendance Entry Field",font=("Arial",15,"bold"),border=5,width=300) #DATA ENTRY DRAME
    attendance_frame.place(x=10,y=120,width=950,height=370) 

def sub_for_cycle():
    def marks_submit():
            if fetched_cyc=="Chemistry":
                s1=c_en1.get()
                s2=c_en2.get()     #check this out
                s3=c_en3.get()
                s4=c_en4.get()
                s5=c_en6.get()
                subm_c=[s1,s2,s3,s4,s5]

            else:
                s1=p_en1.get()
                s2=p_en2.get()
                s3=p_en3.get()
                s4=p_en4.get()
                s5=p_en6.get()
                subm_c=[s1,s2,s3,s4,s5]
            
            marks_list_isa1=[[],['s1',],['s2',],['s3',],['s4',],['s5',]] 
            marks_list_isa2=[[],['s1',],['s2',],['s3',],['s4',],['s5',]]
            marks_list_esa=[[],['s1',],['s2',],['s3',],['s4',],['s5',]]

            if E_TYPE=="ISA-1":
                marks_list_isa1[0].append(fetched_name)
                marks_list_isa1[0].append(st_srn)
                c=0
                for i in subm_c:
                    if int(i)<=40:
                        pass
                    else:
                        wrong_marks_entry_ISA()
                        c+=1
                if c==0:
                    marks_list_isa1[1].append(s1)
                    marks_list_isa1[2].append(s2)
                    marks_list_isa1[3].append(s3)
                    marks_list_isa1[4].append(s4)
                    marks_list_isa1[5].append(s5)

                
                #connect to db here         #CREATE TABLES BASED ON ETYPE - I-1,I-2 AND E ,THEN IG PUTTING THE NAMES OF SUB INTO LIST INTZ WILL BE REQ
                
                #print(marks_list_isa1)


                stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                c=stu_db.cursor()
    
                c.execute("INSERT INTO ISA_1 VALUES(:Name, :SRN, :sub1, :sub2, :sub3, :sub4, :sub5)",
                    {
                        'Name':marks_list_isa1[0][0],
                        'SRN':marks_list_isa1[0][1],
                        'sub1':int(marks_list_isa1[1][1]),
                        'sub2':int(marks_list_isa1[2][1]),
                        'sub3':int(marks_list_isa1[3][1]),
                        'sub4':int(marks_list_isa1[4][1]),
                        'sub5':int(marks_list_isa1[5][1])
                    })

                stu_db.commit()

                stu_db.close()

                query_ISA1_MARKS()

            elif E_TYPE=="ISA-2":
                marks_list_isa2[0].append(fetched_name)
                marks_list_isa2[0].append(st_srn)
                c=0
                for i in subm_c:
                    if int(i)<=40:
                        pass
                    else:
                        wrong_marks_entry_ISA()
                        c+=1
                if c==0:
                    marks_list_isa2[1].append(s1)
                    marks_list_isa2[2].append(s2)
                    marks_list_isa2[3].append(s3)
                    marks_list_isa2[4].append(s4)
                    marks_list_isa2[5].append(s5)

                
                    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                    c=stu_db.cursor()
    
                    c.execute("INSERT INTO ISA_2 VALUES(:Name, :SRN, :sub1, :sub2, :sub3, :sub4, :sub5)",
                        {
                            'Name':marks_list_isa2[0][0],
                            'SRN':marks_list_isa2[0][1],
                            'sub1':int(marks_list_isa2[1][1]),
                            'sub2':int(marks_list_isa2[2][1]),
                            'sub3':int(marks_list_isa2[3][1]),
                            'sub4':int(marks_list_isa2[4][1]),
                            'sub5':int(marks_list_isa2[5][1])
                        })

                    stu_db.commit()

                    stu_db.close()

                    query_ISA2_MARKS()
            else:
                marks_list_esa[0].append(fetched_name)
                marks_list_esa[0].append(st_srn)
                c=0
                for i in subm_c:
                    if int(i)<=100:
                        pass
                    else:
                        wrong_marks_entry_ESA()
                        c+=1
                if c==0:
                    marks_list_esa[1].append(s1)
                    marks_list_esa[2].append(s2)
                    marks_list_esa[3].append(s3)
                    marks_list_esa[4].append(s4)
                    marks_list_esa[5].append(s5)

                
                    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                    c=stu_db.cursor()
    
                    c.execute("INSERT INTO ESA VALUES(:Name, :SRN, :sub1, :sub2, :sub3, :sub4, :sub5)",
                        {
                            'Name':marks_list_esa[0][0],
                            'SRN':marks_list_esa[0][1],
                            'sub1':int(marks_list_esa[1][1]),
                            'sub2':int(marks_list_esa[2][1]),
                            'sub3':int(marks_list_esa[3][1]),
                            'sub4':int(marks_list_esa[4][1]),
                            'sub5':int(marks_list_esa[5][1])
                        })

                    stu_db.commit()

                    stu_db.close()

                    query_ESA_MARKS()

    def clear_entries():
            if fetched_cyc=="Chemistry":

                c_en1.delete(0, END)

                c_en2.delete(0, END)

                c_en3.delete(0, END)

                c_en4.delete(0, END)

                c_en6.delete(0, END)

            else:
                p_en1.delete(0, END)

                p_en2.delete(0, END)

                p_en3.delete(0, END)

                p_en4.delete(0, END)

                p_en6.delete(0, END)

    #$
    if fetched_cyc=="Chemistry":
        #labels(subj names)
        c_la1=Label(marks_frame,text="Python Programming",font=("Arial",15,"bold"))
        c_la1.grid(row=1,column=1,padx=8,pady=10)

        c_la2=Label(marks_frame,text="Engg.Mechanics",font=("Arial",15,"bold"))
        c_la2.grid(row=3,column=1,padx=8,pady=10)

        c_la3=Label(marks_frame,text="Engg.Chemistry",font=("Arial",15,"bold"))
        c_la3.grid(row=5,column=1,padx=8,pady=10)

        c_la4=Label(marks_frame,text="Elec.Principles",font=("Arial",15,"bold"))
        c_la4.grid(row=1,column=4,padx=8,pady=10)

        c_la5=Label(marks_frame,text="& Devices",font=("Arial",15,"bold"))
        c_la5.grid(row=2,column=4,padx=8,pady=2)

        c_la6=Label(marks_frame,text="Engg.Mathematics",font=("Arial",15,"bold"))
        c_la6.grid(row=3,column=4,padx=8,pady=10)

        #marks entry fields
        c_en1=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        c_en1.grid(row=1,column=2,padx=8,pady=10)

        c_en2=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        c_en2.grid(row=3,column=2,padx=8,pady=10)

        c_en3=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        c_en3.grid(row=5,column=2,padx=8,pady=10)

        c_en4=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        c_en4.grid(row=1,column=5,padx=8,pady=10)

        c_en6=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        c_en6.grid(row=3,column=5,padx=8,pady=10)

         
        #Submit button
        c_but=Button(marks_frame,text="Submit Marks",font=("Arial",18,"bold"),command=lambda:[marks_submit(),clear_entries()])
        c_but.place(x=270,y=200)
    else:
        #labels(subj names)
        p_la1=Label(marks_frame,text="Python Programming",font=("Arial",15,"bold"))
        p_la1.grid(row=1,column=1,padx=8,pady=10)

        p_la2=Label(marks_frame,text="Engg.Mechanical",font=("Arial",15,"bold"))
        p_la2.grid(row=3,column=1,padx=8,pady=10)

        p_la3=Label(marks_frame,text="Engg.Physics",font=("Arial",15,"bold"))
        p_la3.grid(row=5,column=1,padx=8,pady=10)

        p_la4=Label(marks_frame,text="Electricals",font=("Arial",15,"bold"))
        p_la4.grid(row=1,column=4,padx=8,pady=10)

        p_la6=Label(marks_frame,text="Engg.Mathematics",font=("Arial",15,"bold"))
        p_la6.grid(row=3,column=4,padx=8,pady=10)

        #marks entry fields
        p_en1=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        p_en1.grid(row=1,column=2,padx=8,pady=10)

        p_en2=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        p_en2.grid(row=3,column=2,padx=8,pady=10)

        p_en3=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        p_en3.grid(row=5,column=2,padx=8,pady=10)

        p_en4=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        p_en4.grid(row=1,column=5,padx=8,pady=10)

        p_en6=Entry(marks_frame,font=("Arial",15,"bold"),width=10)
        p_en6.grid(row=3,column=5,padx=8,pady=10)

        p_but=Button(marks_frame,text="Submit Marks",font=("Arial",18,"bold"),command=lambda:[marks_submit(),clear_entries()])
        p_but.place(x=270,y=200)

#SUB WINDOW 1
def marks_entry_window():
    global top1
    top1=Toplevel()
    top1.title("MARKS ENTRY")
    top1.geometry("900x500")
    def exam_type():
        global BUT1
        BUT1=Button(top1,text="ISA-1",font=("Arial",20,"bold"),command=lambda:[sub_for_cycle(),get_exam_for_ISA1()])
        BUT1.grid(row=3,column=1,padx=30,pady=30)
        global BUT2
        BUT2=Button(top1,text="ISA-2",font=("Arial",20,"bold"),command=lambda:[sub_for_cycle(),get_exam_for_ISA2()])
        BUT2.grid(row=4,column=1,padx=30,pady=30)
        global BUT3
        BUT3=Button(top1,text="ESA",font=("Arial",20,"bold"),command=lambda:[sub_for_cycle(),get_exam_for_ESA()])
        BUT3.grid(row=5,column=1,padx=30,pady=30)

    but1=tk.Button(top1,text="OK",font=("Arial",12,"bold"),command=lambda:[exam_type(),get_cycle_marks(),create_mframe()])  ##NOTE THIS
    but1.grid(row=1,column=3)

    lab1=Label(top1,text="Enter SRN",font=("Arial",20,"bold"))
    lab1.grid(row=1,column=1,)

    global ent1
    ent1=Entry(top1,font=("Arial",20,"bold"),)
    ent1.grid(row=1,column=2)
    
    top1.mainloop()


#SUB WINDOW 2
def attendance_entry_window():
    global top2
    top2=Toplevel()
    top2.title("ATTENDANCE ENTRY")
    top2.geometry("1000x500")


    Lab1=Label(top2,text="Enter SRN",font=("Arial",20,"bold"))
    Lab1.grid(row=1,column=1,)

    global Ent1
    Ent1=Entry(top2,font=("Arial",20,"bold"),)
    Ent1.grid(row=1,column=2)

    #global ent1
    
    def disp_subj():

        def attendance_submit():

            attend_list_chem=[[],['s1',],['s2',],['s3',],['s4',],['s5',]] 
            attend_list_phy=[[],['s1',],['s2',],['s3',],['s4',],['s5',]]

            if fetched_cyc=="Chemistry":
                s1=c_en1_att.get()
                s2=c_en2_att.get()     #check this out
                s3=c_en3_att.get()
                s4=c_en4_att.get()
                s5=c_en6_att.get()
                subm_c_att=[s1,s2,s3,s4,s5]

                S1=c_en1_tot.get()
                S2=c_en2_tot.get()     #check this out
                S3=c_en3_tot.get()
                S4=c_en4_tot.get()
                S5=c_en6_tot.get()
                subm_c_tot=[S1,S2,S3,S4,S5]

                A1=(int(s1)/int(S1))*100
                A1=round(A1,2)
                A2=round(int(s2)/int(S2)*100,2)
                A3=round(int(s3)/int(S3)*100,2)
                A4=round(int(s4)/int(S4)*100,2)
                A5=round(int(s5)/int(S5)*100,2)

                attend_perc=[fetched_name,st_srn,A1,A2,A3,A4,A5]
                #attendance_master_list.append(attend_perc)
                #attend_perc=[]


                attend_list_chem[0].append(fetched_name)
                attend_list_chem[0].append(st_srn)
                
                c=0
                for i in range(0,5):
                    if int(subm_c_att[i])<=int(subm_c_tot[i]):
                        pass
                    else:
                        wrong_attend_entry()
                        c+=1
                if c==0:
                    attend_list_chem[1].append(A1)
                    attend_list_chem[2].append(A2)
                    attend_list_chem[3].append(A3)
                    attend_list_chem[4].append(A4)
                    attend_list_chem[5].append(A5)

                    #print(attend_list_chem)

                    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                    c=stu_db.cursor()
    
                    c.execute("INSERT INTO ATTENDANCE VALUES(:Name, :SRN, :sub1, :sub2, :sub3, :sub4, :sub5)",
                        {
                            'Name':attend_list_chem[0][0],
                            'SRN':attend_list_chem[0][1],
                            'sub1':attend_list_chem[1][1],
                            'sub2':attend_list_chem[2][1],
                            'sub3':attend_list_chem[3][1],
                            'sub4':attend_list_chem[4][1],
                            'sub5':attend_list_chem[5][1]
                        })

                    stu_db.commit()

                    stu_db.close()

                    

            else:
                s1=p_en1_att.get()
                s2=p_en2_att.get()
                s3=p_en3_att.get()
                s4=p_en4_att.get()
                s5=p_en6_att.get()
                subm_c_att=[s1,s2,s3,s4,s5]

                S1=p_en1_tot.get()
                S2=p_en2_tot.get()
                S3=p_en3_tot.get()
                S4=p_en4_tot.get()
                S5=p_en6_tot.get()
                subm_c_tot=[S1,S2,S3,S4,S5]

                A1=round(int(s1)/int(S1)*100,2)
                A2=round(int(s2)/int(S2)*100,2)
                A3=round(int(s3)/int(S3)*100,2)
                A4=round(int(s4)/int(S4)*100,2)
                A5=round(int(s5)/int(S5)*100,2)
            
                attend_perc=[fetched_name,st_srn,A1,A2,A3,A4,A5]
                #attendance_master_list.append(attend_perc)
                #attend_perc=[]

                attend_list_phy[0].append(fetched_name)
                attend_list_phy[0].append(st_srn)
                
                c=0
                for i in range(0,5):
                    if int(subm_c_att[i])<=int(subm_c_tot[i]):
                        pass
                    else:
                        wrong_attend_entry()
                        c+=1
                if c==0:
                    attend_list_phy[1].append(A1)
                    attend_list_phy[2].append(A2)
                    attend_list_phy[3].append(A3)
                    attend_list_phy[4].append(A4)
                    attend_list_phy[5].append(A5)

                    #print(attend_list_phy)

                    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

                    c=stu_db.cursor()
    
                    c.execute("INSERT INTO ATTENDANCE VALUES(:Name, :SRN, :sub1, :sub2, :sub3, :sub4, :sub5)",
                        {
                            'Name':attend_list_phy[0][0],
                            'SRN':attend_list_phy[0][1],
                            'sub1':attend_list_phy[1][1],
                            'sub2':attend_list_phy[2][1],
                            'sub3':attend_list_phy[3][1],
                            'sub4':attend_list_phy[4][1],
                            'sub5':attend_list_phy[5][1]
                        })

                    stu_db.commit()

                    stu_db.close()

        def clear_entries():
            if fetched_cyc=="Chemistry":

                c_en1_att.delete(0, END)
                c_en1_tot.delete(0, END)

                c_en2_att.delete(0, END)
                c_en2_tot.delete(0, END)

                c_en3_att.delete(0, END)
                c_en3_tot.delete(0, END)

                c_en4_att.delete(0, END)
                c_en4_tot.delete(0, END)

                c_en6_att.delete(0, END)
                c_en6_tot.delete(0, END)

            else:
                p_en1_att.delete(0, END)
                p_en1_tot.delete(0, END)

                p_en2_att.delete(0, END)
                p_en2_tot.delete(0, END)

                p_en3_att.delete(0, END)
                p_en3_tot.delete(0, END)

                p_en4_att.delete(0, END)
                p_en4_tot.delete(0, END)

                p_en6_att.delete(0, END)
                p_en6_tot.delete(0, END)



        if fetched_cyc=="Chemistry":
        #labels(subj names)
            c_la1=Label(attendance_frame,text="Python Programming",font=("Arial",15,"bold"))
            c_la1.grid(row=1,column=1,padx=8,pady=30)

            c_la2=Label(attendance_frame,text="Engg.Mechanics",font=("Arial",15,"bold"))
            c_la2.grid(row=3,column=1,padx=8,pady=30)

            c_la3=Label(attendance_frame,text="Engg.Chemistry",font=("Arial",15,"bold"))
            c_la3.grid(row=4,column=1,padx=8,pady=30)

            c_la4=Label(attendance_frame,text="Elec.Principles",font=("Arial",15,"bold"))
            c_la4.grid(row=1,column=5,padx=8,pady=30)

            c_la5=Label(attendance_frame,text="& Devices",font=("Arial",15,"bold"))
            c_la5.grid(row=2,column=5,padx=8,pady=2)

            c_la6=Label(attendance_frame,text="Engg.Mathematics",font=("Arial",15,"bold"))
            c_la6.grid(row=3,column=5,padx=8,pady=30)

            c_la7=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            c_la7.grid(row=1,column=4,padx=8,pady=30)

            c_la8=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            c_la8.grid(row=4,column=4,padx=8,pady=30)

            c_la9=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            c_la9.grid(row=3,column=4,padx=8,pady=30)

            c_la10=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            c_la10.grid(row=1,column=8,padx=8,pady=30)

            c_la11=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            c_la11.grid(row=3,column=8,padx=8,pady=30)

        #marks entry fields
            c_en1_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en1_att.grid(row=1,column=2,padx=8,pady=30)

            c_en1_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en1_tot.grid(row=1,column=3,padx=8,pady=30)

            c_en2_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en2_att.grid(row=3,column=2,padx=8,pady=30)

            c_en2_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en2_tot.grid(row=3,column=3,padx=8,pady=30)

            c_en3_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en3_att.grid(row=4,column=2,padx=8,pady=30)

            c_en3_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en3_tot.grid(row=4,column=3,padx=8,pady=30)

            c_en4_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en4_att.grid(row=1,column=6,padx=8,pady=30)

            c_en4_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en4_tot.grid(row=1,column=7,padx=8,pady=30)

            c_en6_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en6_att.grid(row=3,column=6,padx=8,pady=30)

            c_en6_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            c_en6_tot.grid(row=3,column=7,padx=8,pady=30)

         
        #Submit button
            c_but=Button(attendance_frame,text="Submit Attendance",font=("Arial",18,"bold"),command=lambda:[attendance_submit(),clear_entries()])
            c_but.place(x=330,y=290)

        else:
        #labels(subj names)
            p_la1=Label(attendance_frame,text="Python Programming",font=("Arial",15,"bold"))
            p_la1.grid(row=1,column=1,padx=8,pady=30)

            p_la2=Label(attendance_frame,text="Engg.Mechanical",font=("Arial",15,"bold"))
            p_la2.grid(row=3,column=1,padx=8,pady=30)

            p_la3=Label(attendance_frame,text="Engg.Physics",font=("Arial",15,"bold"))
            p_la3.grid(row=4,column=1,padx=8,pady=30)

            p_la4=Label(attendance_frame,text="Electricals",font=("Arial",15,"bold"))
            p_la4.grid(row=1,column=5,padx=8,pady=30)

            p_la6=Label(attendance_frame,text="Engg.Mathematics",font=("Arial",15,"bold"))
            p_la6.grid(row=3,column=5,padx=8,pady=30)

            p_la7=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            p_la7.grid(row=1,column=4,padx=8,pady=30)

            p_la8=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            p_la8.grid(row=4,column=4,padx=8,pady=30)

            p_la9=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            p_la9.grid(row=3,column=4,padx=8,pady=30)

            p_la10=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            p_la10.grid(row=1,column=8,padx=8,pady=30)

            p_la11=Label(attendance_frame,text="(Attended/Total)",font=("Arial",8,"bold"))
            p_la11.grid(row=3,column=8,padx=8,pady=30)


        #marks entry fields
            p_en1_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en1_att.grid(row=1,column=2,padx=8,pady=30)

            p_en1_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en1_tot.grid(row=1,column=3,padx=8,pady=30)

            p_en2_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en2_att.grid(row=3,column=2,padx=8,pady=30)

            p_en2_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en2_tot.grid(row=3,column=3,padx=8,pady=30)

            p_en3_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en3_att.grid(row=4,column=2,padx=8,pady=30)

            p_en3_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en3_tot.grid(row=4,column=3,padx=8,pady=30)

            p_en4_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en4_att.grid(row=1,column=6,padx=8,pady=30)

            p_en4_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en4_tot.grid(row=1,column=7,padx=8,pady=30)

            p_en6_att=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en6_att.grid(row=3,column=6,padx=8,pady=30)

            p_en6_tot=Entry(attendance_frame,font=("Arial",15,"bold"),width=5)
            p_en6_tot.grid(row=3,column=7,padx=8,pady=30)

            p_but=Button(attendance_frame,text="Submit Attendance",font=("Arial",18,"bold"),command=attendance_submit)
            p_but.place(x=360,y=290)



    But1=Button(top2,text="OK",font=("Arial",12,"bold"),command=lambda:[get_cycle_attendance(),create_aframe(),disp_subj()])
    But1.grid(row=1,column=3)

    top2.mainloop()

def search_name():

    name_to_search = E1.get()

    #CLEAR THE TREEVIEW:
    for record in stu_tview.get_children():
        stu_tview.delete(record)

    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CONNECTING TO DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    c.execute("SELECT rowid,* FROM student WHERE Name like ?", (name_to_search,)) #like is used here instead of = as i doesnt consider case sensitivity

    records=c.fetchall()

    stu_tview.tag_configure('evenrow',background='light blue')

    global count
    count=0
    for rec in records:
        if count%2==0:
            stu_tview.insert(parent='',index='end',iid=count,text="",values=(rec[0],rec[2],rec[3],rec[4],rec[5]),tags=('evenrow',))
        else:
            stu_tview.insert(parent='',index='end',iid=count,text="",values=(rec[0],rec[2],rec[3],rec[4],rec[5]),tags=('oddrow',))
        count+=1
    # Closing the database connection
    stu_db.commit()

    stu_db.close()

# Creating the main window 
#UPDATING NEW DATA INTO TREEVIEW:

def select_record(e):

    #CLEAR THE ENTRY BOXES
    Name.delete(0, END)
    SRN.delete(0, END)
    Ph_number.delete(0, END)
    #Cycle.delete(0, END)

    #GRAB THE RECORD NUM:
    selected=stu_tview.focus()

    #GRAB RECORD VALUES:
    global values
    values=stu_tview.item(selected,'values')

    #print(values)

    #DISPLAYING SELECTED RECORD ELEM INTO THE ENTRY FIELDS:
    SRN.insert(0, values[1])
    Name.insert(0, values[2])
    Ph_number.insert(0, values[3])
    #Cycle.insert(0, values[4])
  

#UPDATING THE NEW EDITED RECORD:
def update_record():
    #GRAB THE REC NUM:
    selected=stu_tview.focus()
    
    #GETTING THE NEW VALUES:
    stu_tview.item(selected,text="",values=(values[0],SRN.get(),Name.get(),Ph_number.get(),Cycle.get()))

    #UPDATING THE CHANGES INTO DB:
    stu_db=sqlite3.connect('STUDENT DATABASE.db')#CREATING DATABASE

    c=stu_db.cursor() #CREATING CURSOR

    o=values[0]
    #print(o)
    c.execute("""UPDATE student SET 
        SRN=:p1,
        Name=:p2,
        Ph_number=:p3,
        Cycle=:p4

        WHERE oid = :oid""",
        {
            'p1':Name.get(),
            'p2':SRN.get(),
            'p3':Ph_number.get(),
            'p4':Cycle.get(),
            'oid':o
        })

    stu_db.commit()

    stu_db.close()

    #CLEAR THE ENTRY BOXES
    Name.delete(0, END)
    SRN.delete(0, END)
    Ph_number.delete(0, END)
    #Cycle.delete(0, END)


#DELETING ONLY SELECTED RECORDS OF THE TREEVIEW:
def remove_record():
    x=stu_tview.selection() #CAN INCLUDE INDEX AS [0] HERE TO ALLOW TO DELETE ONLY ONE RECORD AT A TIME
    for record in x:
        stu_tview.delete(record)



#FUNCTION INSERT NEW RECORD INTO DATABASE:

def add_data_db():
    
    stu_db=sqlite3.connect('STUDENT DATABASE.db') #CONNECTING DATABASE
    
    c=stu_db.cursor() #CREATING CURSOR

    
    #c.execute("SELECT rowid FROM student")
    last_row_id=c.lastrowid #RETURNS THE ROWID OF THE LAST INSERTED ELEMENT
    
    
    #INSERTING RECORDS INTO DB
    c.execute("INSERT INTO student VALUES(:SL_NO, :SRN, :Name, :Ph_number, :Cycle )", 
        {

            'SL_NO':last_row_id,
            'Name':Name.get(),
            'SRN':SRN.get(),
            'Ph_number':Ph_number.get(),
            'Cycle':Cycle.get()
        })
    #count+=1
    stu_db.commit()

    stu_db.close()

    Name.delete(0, END)
    SRN.delete(0, END)
    Ph_number.delete(0, END)
    #Cycle.delete(0, END)

    stu_tview.delete(*stu_tview.get_children()) #TO DELETE ALL CURRENT RECORDS WHICH DOESNT INCLUDE THE NEW ADDED RECORD

    query() #TO GET THE NEW TABLE WITH ADDED RECORD


def delete_all_data_db():
    resp=messagebox.askyesno("DELETE ALL !!","This deletes all the data \n Are you sure ??")

    if resp==1:


        for record in stu_tview.get_children():
            stu_tview.delete(record)

        stu_db=sqlite3.connect('STUDENT DATABASE.db')  #CREATING A TABLE

        c=stu_db.cursor() #CREATING A CURSOR

        c.execute("DROP TABLE student")

        stu_db.commit()

        stu_db.close()


#FRAMES
frame1=LabelFrame(root,text="Input Field",font=("Arial",20,"bold"),border=5,width=400) #DATA ENTRY FRAME
frame1.place(x=60,y=150,width=600,height=700)

frame2=LabelFrame(root,border=5,width=400)     #DATA DISPLAY FRAME
frame2.place(x=670,y=300,width=1000,height=550)

frame3=LabelFrame(root,font=("Arial",20,"bold"),border=5,width=400) #ADD,DELETE AND UPDATE FRAME 
frame3.place(x=85,y=690,width=550,height=140)

frame4=LabelFrame(root,text="Output Field",font=("Arial",20,"bold"),border=5,width=400) #SEARCH,RESET AND SORT FRAME
frame4.place(x=670,y=150,width=1000,height=150)


#TREEVIEW FRAME :
#MAIN DISPLAY FRAME
tree_frame=ttk.Frame(frame2)
tree_frame.pack(fill=tk.BOTH,expand=1)

stu_tview=ttk.Treeview(tree_frame)
stu_tview.pack(fill=tk.BOTH,expand=1)
stu_tview['columns']=("SL_NO","Name","SRN","Ph_Number","Cycle")

stu_tview.column("#0",width=0,stretch=NO)
stu_tview.column("SL_NO",width=50,anchor=W)
stu_tview.column("Name",width=120,anchor=W)
stu_tview.column("SRN",width=120,anchor=W)
stu_tview.column("Ph_Number",width=120,anchor=W)
stu_tview.column("Cycle",width=120,anchor=W)

stu_tview.heading("#0",text="parent",anchor=W)
stu_tview.heading("SL_NO",text="Sl.No",anchor=W)
stu_tview.heading("Name",text="Student Name",anchor=W)
stu_tview.heading("SRN",text="SRN",anchor=W)
stu_tview.heading("Ph_Number",text="Ph number",anchor=W)
stu_tview.heading("Cycle",text="Cycle",anchor=W)

#ADDING SCROLL BARS
y_scroll=tk.Scrollbar(stu_tview,orient=tk.VERTICAL,command=stu_tview.yview)
y_scroll.pack(side=tk.RIGHT,fill=tk.Y)

x_scroll=tk.Scrollbar(stu_tview,orient=tk.HORIZONTAL,command=stu_tview.xview)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

stu_tview.config(yscrollcommand=y_scroll.set)
stu_tview.config(xscrollcommand=x_scroll.set)

#FRAME 1 ENTITIES :
#LABELS OF FRAME1
l1=Label(frame1,text="Student Details :",font=("Arial",15,"bold"))
l1.grid(row=1,column=1,pady=10)

l2=Label(frame1,text="SRN : ",font=("Arial",15,"bold"))
l2.grid(row=3,column=1,padx=55,pady=20)

l3=Label(frame1,text="NAME : ",font=("Arial",15,"bold"))
l3.grid(row=5,column=1,padx=55,pady=20)

l4=Label(frame1,text="Ph NUMBER : ",font=("Arial",15,"bold"))
l4.grid(row=7,column=1,padx=55,pady=20)

l5=Label(frame1,text="CYCLE : ",font=("Arial",15,"bold"))
l5.grid(row=9,column=1,padx=55,pady=20)


#ENTRIES OF FRAME1
Name=Entry(frame1,width=23,font=("Arial",12))
Name.grid(row=3,column=2)
SRN=Entry(frame1,width=23,font=("Arial",12))
SRN.grid(row=5,column=2)

Ph_number=Entry(frame1,width=23,font=("Arial",12))
Ph_number.grid(row=7,column=2)

#DROPDOWN OF FRAME 1:
Cycle=StringVar()
Cycle.set("Chemistry")
Dd1=OptionMenu(frame1,Cycle,"Chemistry","Physics")
Dd1.config(font=("Arial",15))
Dd1.grid(row=9,column=2)


#BUTTONS OF FRAME1
b1=Button(frame1,text="Marks Entry",font=("Arial",15,"bold"),command=marks_entry_window)#Opens a new window MARKS ENTRY
b1.grid(row=12,column=1,columnspan=3,padx=200,pady=15)

b_atten=Button(frame1,text="Attendance Entry",font=("Arial",15,"bold"),command=attendance_entry_window)
b_atten.grid(row=13,column=1,columnspan=3,padx=200,pady=15)


#FRAME 3 ENTITIES:
#BUTTONS OF FRAME 3
b2=Button(frame3,text="ADD",font=("Arial",14,"bold"),command=add_data_db)
b2.grid(row=16,column=2,padx=80,pady=15)

b3=Button(frame3,text="DELETE",font=("Arial",14,"bold"),command=remove_record)
b3.grid(row=16,column=1,padx=30,pady=15)

b4=Button(frame3,text="UPDATE",font=("Arial",14,"bold"),command=update_record)
b4.grid(row=16,column=3,padx=40,pady=15)

b5=Button(frame3,text="DELETE ALL",font=("Arial",14,"bold"),command=delete_all_data_db)
b5.grid(row=17,column=2,padx=20,pady=5)

#FRAME 4 ENTITIES
#LABELS OF FRAME4:
L1=Label(frame4,text="Search by : ",font=("Arial",15,"bold"))
L1.grid(row=1,column=1,padx=5,pady=10)

#BUTTONS OF FRAME4:
B2=Button(frame4,text="SEARCH",font=("Arial",12,"bold"),command=search_name)
B2.grid(row=1,column=4,padx=5,pady=10)

B3=Button(frame4,text="RESET",font=("Arial",12,"bold"),command=query)
B3.place(x=350,y=70)

#ENTRIES OF FRAME4:
E1=Entry(frame4,width=20,font=("Arial",18))
E1.grid(row=1,column=3,padx=5,pady=10)

#DROPDOWN OF FRAME4:
dr_down1=StringVar()
dd1=OptionMenu(frame4,dr_down1,"SRN","NAME")
dr_down1.set("NAME")
dd1.config(font=("Arial",15))
dd1.grid(row=1,column=2)

# BIND THE TREEVIEW TO GET THE SELECTED RECORD directly
stu_tview.bind("<ButtonRelease-1>",select_record)


query()# TO DISPLAY THE DATA OF DB ONTO THE CMD TERMINAL

root.mainloop()