import tkinter as tk
import tkinter.font as tkfont
import random
import cx_Oracle
from tkinter import *
from PIL import ImageTk, Image
#AGENT
def agent_option():
    #home page or exit
    for widget in root.winfo_children():
        widget.destroy()
    root.title('')
    root.geometry("300x200")
    f1=tkfont.Font(family='Bahnschrift SemiCondensed', size=16)
    mess=tk.Label(root, text='Car registered!',font=f1)
    mess.pack()
    op1=tk.Button(root, text="EXIT", bg='pink',font=f1,command=exit)
    op1.place(x=110,y=80, width=70,height=25)
    #op1.place(x=30,y=140, width=80)
    op2=tk.Button(root, text="Home Page",font=f1, bg='lavender', command= agent_form1)
    op2.place(x=90,y=130,width=120,height=25)
    #op2.place(x=150,y=140, width=120)
    root.mainloop()
def agent_insertnewcar():
    conn=cx_Oracle.connect('scott/tiger@localhost:1521/orcle123')
    click=clicked.get()
    r=rno.get()
    m=mod.get()
    t=tarr.get()
    a=availability.get()
    curr=conn.cursor()
    data=[r,click,m,t,a]
    curr.execute("insert into car values(:1,:2,:3,:4,:5)",data)
    conn.commit()
    agent_option()
def agent_displaycars():
    conn=cx_Oracle.connect('scott/tiger@localhost:1521/orcle123')
    cur = conn.cursor()
    cur.execute("select * from car")
    row=cur.fetchall()
    print("\n",row)
def agent_newcar():
    #choose type
    for widget in root.winfo_children():
        widget.destroy()
    root.title('NEW CAR')
    root.geometry("300x400")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    #reg no
    regno = tk.Label(root, text='REG. NO',font=f)
    regno.place(x=50, y=50)
    regno1 = tk.Entry(root, textvariable=rno, width=50)
    regno1.place(x=140, y=50, width=100)

    drop=tk.Label(root, text='TYPE',font=f)
    drop.place(x=50, y=100)
    drop1=tk.Entry(root, textvariable=clicked, width=50)
    drop1.place(x=140, y=100, width=100)

    
    #model
    model=tk.Label(root, text='Model',font=f)
    model.place(x=50, y=150)
    model1=tk.Entry(root,textvariable=mod,width=50)
    model1.place(x=140,y=150,width=100)
    
    #tariff
    tariff=tk.Label(root, text='Tariff (day wise)',font=f)
    tariff.place(x=50, y=200)
    tariff1=tk.Entry(root, textvariable=tarr, width=50)
    tariff1.place(x=170,y=200,width=70)

    #avaiablitiy
    avail=tk.Label(root, text='Available-Y/N',font=f)
    avail.place(x=50, y=250)
    avail1=tk.Entry(root, textvariable=availability)
    avail1.place(x=170, y=250,width=50)
    
    button = Button( root , text = "Next" ,font=f ,bg='#c8b9d6',command =agent_insertnewcar)
    button.place(x=100, y=300, width=70)

    btn=tk.Button(root,text='Back',font=f,bg='light green',command=agent_form1)
    btn.place(x=10,y=350, width=50)
    root.mainloop()
def agent_showdb():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    root.title('DATABASE')
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    cur=conn.cursor()
    cur.execute('select * from car')
    row=cur.fetchall()
    m=tk.Label(root,text='REGNO     TYPE     MODEL    TARIFF      A',font=f1)
    m.pack()
    for i in row:
        
        t1=(i[0],i[1],i[2],i[3],i[4])
        mess=Label(root,text=t1, font=f1, width=500)
        mess.pack(expand='True')
        
    btn=tk.Button(root,text='Back', font=f1,bg='light green',command=agent_form1)
    btn.place(x=20,y=450,width=70,height=30)

    btn1=tk.Button(root,text='Exit', font=f1,bg='light green',command=exit)
    btn1.place(x=570,y=450, width=70,height=30)
    agent_displaycars()
    root.mainloop()
def agent_form1():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    root.title('HOME PAGE')
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=18)
    op1=tk.Button(root, text="View Database", font=f1,bg='pink', command=agent_showdb)
    op1.place(x=210,y=60,width=206,height=30)
    op2=tk.Button(root, text="Enter New Car", font=f1, bg='lavender', command= agent_newcar)
    op2.place(x=210,y=140,width=208,height=30)

    op3=tk.Button(root, text="Remove a Car", font=f1, bg='pink', command=agent_delcar)
    op3.place(x=210,y=220,width=206,height=30)
    op4=tk.Button(root, text="Update Car", font=f1, bg='lavender', command= agent_update)
    op4.place(x=210,y=300,width=208,height=30)
    op5=tk.Button(root, text="View Bookings", font=f1, bg='pink', command= agent_showbooking)
    op5.place(x=210,y=380,width=208,height=30)
    
    btn=tk.Button(root,text='Back', font=f1,bg='light green',command=agent_login )
    btn.place(x=20,y=450,width=70,height=30)
    root.mainloop()
def agent_logged():
    id=var1.get()
    passw=var2.get()
    root.geometry("650x500")
    cur=conn.cursor()
    cur.execute('select id,passw from agent')
    row=cur.fetchall()
    for i in row:
        
        if i[0]==id:
            if i[1]==passw:
                agent_form1()
                break
            else:
                mess=tk.Message(root,text="Invalid",width=50)
                mess.place(x=100,y=200)
        else:
            mess=tk.Message(root,text="Invalid",width=50)
            mess.place(x=100,y=200)        
def agent_login():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    root.configure(bg='#11887d')
    f=tkfont.Font(size=22, weight="bold")
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=18)
    row1 = tk.Label(root, text='ID - ',font=f1)
    row1.place(x=180, y=160)
    enter1 = tk.Entry(root, textvariable=var1)
    enter1.place(x=250, y=160, width=150, height=30)

    row2 = tk.Label(root,text='Password - ',font=f1)
    row2.place(x=110, y=260)
    enter2 = tk.Entry(root, textvariable=var2)
    enter2.place(x=250, y=260, width=150, height=30)

    submitbtn=tk.Button(root, text="Enter",font=f1,bg='lavender', command=agent_logged)
    submitbtn.place(x=245,y=370, width=100, height=33)

    btn=tk.Button(root,text='Back',font=f1,bg='light green',command=agent_user)
    btn.place(x=30,y=420, width=80,height=30)
    root.mainloop()
def agent_addnewuser():
    newid=val1.get()
    newpass=val2.get()
    data=[newid,newpass]
    cur=conn.cursor()
    cur.execute('insert into agent values(:1,:2)',data)
    conn.commit()
    agent_user()
def agent_newuser():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    root.configure(bg='#11887d')
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=18)
    row1 = tk.Label(root, text='Create ID - ',font=f1)
    row1.place(x=120, y=160)
    enter1 = tk.Entry(root, textvariable=val1)
    enter1.place(x=320, y=160, width=150, height=30)

    row2 = tk.Label(root,text='Create Password - ',font=f1)
    row2.place(x=70, y=260)
    enter2 = tk.Entry(root, textvariable=val2)
    enter2.place(x=320, y=260, width=150, height=30)

    submitbtn=tk.Button(root, text="Enter",bg='lavender',font=f1, command=agent_addnewuser)
    submitbtn.place(x=255,y=370, width=100, height=33)

    btn=tk.Button(root,text='Back',font=f1,bg='light green',command=agent_user )
    btn.place(x=30,y=420, width=80,height=30)
    root.mainloop()
def agent_user():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    root.geometry("650x500")
    canvas1 = Canvas(root, width=650, height=500)
    canvas1.pack(fill="both", expand=True)
    image = Image.open(
        r"C:\Users\aravi\OneDrive\Desktop\pic2.jpg")
    image = image.resize((650, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=img,
                        anchor="nw")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=22)
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=18)
    mess=tk.Message(root, text='AGENT LOGIN AND REGISTRATION', width=500, font=f)
    mess.place(x=120,y=70)
    op1=tk.Button(root, text="New User",font=f1, bg='lavender', command=agent_newuser)
    op1.place(x=100,y=250, width=120, height=50)
    op2=tk.Button(root, text="Existing User", font=f1,bg='lavender', command=agent_login)
    op2.place(x=380,y=250, width=170, height=50)

    btn=tk.Button(root,text='Back',font=f1,bg='light green',command=homepage)
    btn.place(x=30,y=440, width=80,height=30) 
    root.mainloop()
def agent_del0():
    dell=delr.get()
    cur = conn.cursor()
    data=[dell]
    cur.execute("delete from car where regno=(:1)", data)
    conn.commit()
    agent_form1()
def agent_delcar():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=12)
    root.title('Delete Car')
    cur=conn.cursor()
    cur.execute('select * from car')
    row=cur.fetchall()
    d=tk.Label(root, text='Enter Reg No of the car to be removed', font=f1)
    d.place(x=90, y=340,width=500,height=27)
    d1=tk.Entry(root, textvariable=delr)
    d1.place(x=260, y=390,width=100,height=27)

    b=tk.Button(root, text='Delete',font=f1,command= agent_del0)
    b.place(x=260, y=430, width=100,height=30)
    btn=tk.Button(root,text='Back', font=f1,bg='light green',command=agent_form1)
    btn.place(x=20,y=450,width=70,height=30)
    for i in row:
        t=(i[0],i[1],i[2],i[3])
        mess=tk.Label(root,text=t, font=f1, width=650)
        mess.pack()
    
    root.mainloop()
def agent_updatecar():
    no=upd.get()
    newval=updval.get()
    data=[newval,no]
    cur = conn.cursor()
    cur.execute("update car set tariff=(:1) where regno=(:2)", data)
    conn.commit()
def agent_update():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("300x300")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    d=tk.Label(root, text='Enter Reg No of the car to be Updated',font=f)
    d.place(x=40, y=70)
    d1=tk.Entry(root, textvariable=upd)
    d1.place(x=90, y=100)

    row1 = tk.Label(root, text='Updated tariff-',font=f)
    row1.place(x=110, y=130)
    enter1 = tk.Entry(root, textvariable=updval)
    enter1.place(x=90, y=160)

    op2=tk.Button(root, text="Update", bg='lavender',font=f, command=agent_updatecar)
    op2.place(x=120,y=200)

    btn=tk.Button(root,text='Back',bg='light green',font=f,command=agent_form1)
    btn.place(x=10,y=250, width=40)
    root.mainloop()
    
def tc():
    root1=tk.Tk()
    root1.geometry("850x250")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=4)
    root1.title("TERMS & CONDITIONS")
    t=("""
    These Terms and Conditions are an agreement between you and AKA Agency. 

    1. The customer must provide his/her identification proof(Aadhar/Driving Lisence).
    2. The customer must pick up and drop the car at the agency (Address- 7/15, Kellys, Chennai)
    3. Payment must be done at the agency via Cash/Card/UPI.
    4. Pickup and Drop time of the car is 10am.
    5. In case of any damage to the car, the customer must pay the required fines fo the same.
    6. In case of any accidents, the agency is not held accountable.
    """)

    l=tk.Label(root1, text=t,font=f)
    l.pack()
    root1.mainloop()
#CUSTOMER
def displaycust():
    conn=cx_Oracle.connect('scott/tiger@localhost:1521/orcle123')
    cur = conn.cursor()
    cur.execute("select * from customer")
    row=cur.fetchall()
    print("\n",row)
def cust_enter():
    id=c_id.get()
    phone=c_ph.get()
    name=c_name.get()
    age=c_age.get()
    l=c_l.get()
    billid=b

    data=[id,name,age,phone,l,billid]
    cur=conn.cursor()
    cur.execute('insert into customer values(:1,:2,:3,:4,:5,:6)',data)
    conn.commit()
    cust_login()
    '''
    cur.execute('select cid,ph from customer')
    row=cur.fetchall()
    for i in row:
        if i[0]==id:
            if i[1]==phone:
                #proceed nooking
                p=tk.Button(root, text= 'book', command='')
                p.place(x=100, y=250)
                break
            else:
                mess=tk.Message(root,text="Invalid phone no",width=100)
                mess.place(x=50,y=200)
        else:
            mess=tk.Message(root,text="Not Registered")
            mess.place(x=100,y=270)
            
            but=tk.Button(root, text='Register now', command=cur.execute('insert into customer values(:1,:2,:3,:4,:5,:6)',data))
            but.place(x=250, y=270)
            root.mainloop()
    '''
    root.mainloop()
def cust_details():
    for widget in root.winfo_children():
        widget.destroy()
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    root.title('CUSTOMER')
    root.geometry("300x400")
    drop=tk.Label(root, text='ID',font=f)
    drop.place(x=50, y=50)
    drop1=tk.Entry(root, textvariable=c_id, width=50)
    drop1.place(x=130, y=50, width=100)

    cname = tk.Label(root, text='Name',font=f)
    cname.place(x=50, y=100)
    cname1 = tk.Entry(root, textvariable=c_name, width=50)
    cname1.place(x=130, y=100, width=100)
    
    cage=tk.Label(root, text='Age',font=f)
    cage.place(x=50, y=150)
    cage1=tk.Entry(root,textvariable=c_age,width=50)
    cage1.place(x=130,y=150,width=100)
    
    cph=tk.Label(root, text='Phone Number',font=f)
    cph.place(x=50, y=200)
    cph1=tk.Entry(root, textvariable=c_ph, width=50)
    cph1.place(x=160,y=200,width=70)

    cl=tk.Label(root, text='License Number',font=f)
    cl.place(x=50, y=250)
    cl1=tk.Entry(root, textvariable=c_l, width=50)
    cl1.place(x=160,y=250,width=70)
    

    button = Button( root , text = "Next" ,font=f, command =cust_enter)
    button.place(x=240, y=350, width=50)

    btn=tk.Button(root,text='Back',bg='light green',font=f,command=cust_login)
    btn.place(x=10,y=350, width=40)
    root.mainloop()
def cust_check():
    id=tempid.get()
    phone=tempph.get()
    cur=conn.cursor()
    cur.execute('select cid,phone from customer')
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=16)
    row=cur.fetchall()
    selected_id=[i[0] for i in row]
    selected_ph=[i[1] for i in row]
    if id in selected_id:
        if phone in selected_ph:
            #proceed nooking
            p=tk.Button(root, text= 'Book ->',font=f,bg='#80c880', command=booking)
            p.place(x=150, y=300,width=100,height=30)
           
        else:
            mess=tk.Message(root,text="Invalid phone no",width=100)
            mess.place(x=100,y=170)
            
    else:
        mess=tk.Message(root,text="Not Registered", width=100)
        mess.place(x=70,y=360)
            
        but=tk.Button(root, text='Register now', command=cust_details)
        but.place(x=250, y=360)
       
    root.mainloop()
def cust_login():
    for widget in root.winfo_children():
        widget.destroy()
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=16)
    root.title('CUSTOMER LOGIN')
    root.configure(bg='#d5cae4')
    root.geometry("400x400")
    drop=tk.Label(root, text='ID',font=f)
    drop.place(x=150, y=70)
    drop1=tk.Entry(root, textvariable=tempid)
    drop1.place(x=200, y=70, width=100, height=25)

    cph=tk.Label(root, text='Phone Number',font=f)
    cph.place(x=50, y=140)
    cph1=tk.Entry(root, textvariable=tempph)
    cph1.place(x=200,y=140,width=100,height=25)

    button = Button( root , text = "Login" ,font=f,bg='#11887d', command =cust_check)
    button.place(x=150, y=220, width=100, height=30)

    btn=tk.Button(root,text='Back',bg='light green',command=homepage)
    btn.place(x=10,y=370, width=40)
    tc()
    root.mainloop()


#BOOKING
def showbookingtable():#should be accessible by admin only. change code
    cur=conn.cursor()
    cur.execute("select * from booking")
    rows=cur.fetchall()
    print(rows)
def delbooking():
    cur=conn.cursor()
    a=dbook.get()
    data3=[a]
    cur.execute("select choice from booking where bid=(:1)",data3)
    row=cur.fetchone()
    data1=row[0]
    cur.execute("delete from booking where bid=(:1)",data3)
    
    cur.execute("update car set availability='Y' where regno=(:1)",data1)
    d=tk.Label(root, text= 'Booking Cancelled')
    d.place(x=50, y=160, width=150 )

    n=tk.Button(root, text='New Booking', command=booking)
    n.place(x=220, y=170)

    btn=tk.Button(root,text='Back',bg='light green',command=displaybill)
    btn.place(x=10,y=170, width=40,height=25)
    btn1=tk.Button(root,text='EXIT',command=exit)
    btn1.place(x=250,y=170,width=40)
    root.mainloop()


def agent_showbooking():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('Bookings')

    f1=tkfont.Font(family='Bahnschrift SemiCondensed',size=12)
    root.geometry("650x500")
    cur=conn.cursor()
    cur.execute('select bid,start_date,type,amount,choice,cust_id from booking ')
    row=cur.fetchall()
    h=tk.Label(root,text='Id               Date             Model Total    rno        cid ',font=f1,width=650)
    h.pack()
    for i in row:
        dis=tk.Label(root, text=i,font=f1,width=650)
        #dis.place(x=50, y=80, width=500)
        dis.pack()
    btn=tk.Button(root,text='Back', font=f1,bg='light green',command=agent_form1)
    btn.place(x=20,y=450,width=70,height=30)
    l=tk.Label(root,text='Enter the BillId of record required to be deleted: ')
    l.place(x=0,y=360,width=650)
    l1=tk.Entry(root,textvariable=dbook)
    l1.place(x=280,y=410,width=100)
    btn2=tk.Button(root,text='CANCEL BOOKING',command=delbooking)
    btn2.place(x=280,y=460)
    root.mainloop()

def displaybill():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('BILL')
    root.geometry("500x600")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    cur=conn.cursor()
    data=[b]
    cur.execute('select bid from booking where bid=(:1)',data)
    row1=cur.fetchone()
    cur.execute('select start_date from booking where bid=(:1)',data)
    row2=cur.fetchone()
    cur.execute('select type from booking where bid=(:1)',data)
    row3=cur.fetchone()
    cur.execute('select nod from booking where bid=(:1)',data)
    row4=cur.fetchone()
    cur.execute('select choice from booking where bid=(:1)',data)
    row5=cur.fetchone()
    cur.execute('select cust_id from booking where bid=(:1)',data)
    row6=cur.fetchone()
    cur.execute('select amount from booking where bid=(:1)',data)
    row7=cur.fetchone()

    GButton_225=tk.Button(root,font=f)
    GButton_225["text"] = "BACK"
    GButton_225.place(x=30,y=460,width=80,height=30)
    GButton_225["command"] = choosecar

    GButton_359=tk.Button(root,font=f)
    GButton_359["text"] = "EXIT"
    GButton_359.place(x=160,y=460,width=80,height=30)
    GButton_359["command"] = exit

    GLabel_717=tk.Label(root,font=f)
    GLabel_717["text"] = "Booking Id"
    GLabel_717.place(x=40,y=40,width=80,height=30)

    GLabel_790=tk.Label(root,font=f)
    GLabel_790["text"] = "Type"
    GLabel_790.place(x=40,y=150,width=80,height=30)

    GLabel_910=tk.Label(root,font=f)
    GLabel_910["text"] = row1
    GLabel_910.place(x=120,y=40,width=80,height=30)

    GLabel_50=tk.Label(root,font=f)
    GLabel_50["text"] = "Date"
    GLabel_50.place(x=40,y=100,width=80,height=30)

    GLabel_197=tk.Label(root,font=f)
    GLabel_197["text"] = "Days"
    GLabel_197.place(x=40,y=200,width=80,height=30)

    GLabel_643=tk.Label(root,font=f)
    GLabel_643["text"] = row2
    GLabel_643.place(x=120,y=100,width=180,height=30)

    GLabel_907=tk.Label(root,font=f)
    GLabel_907["text"] = row4
    GLabel_907.place(x=120,y=200,width=80,height=30)

    GLabel_124=tk.Label(root,font=f)
    GLabel_124["text"] = "Total"
    GLabel_124.place(x=40,y=380,width=80,height=30)

    GLabel_449=tk.Label(root,font=f)
    GLabel_449["text"] = "Car No."
    GLabel_449.place(x=40,y=260,width=80,height=30)

    GLabel_66=tk.Label(root,font=f)
    GLabel_66["text"] = row3
    GLabel_66.place(x=120,y=150,width=80,height=30)

    GLabel_845=tk.Label(root,font=f)
    GLabel_845["text"] = row5
    GLabel_845.place(x=120,y=260,width=80,height=30)

    GLabel_869=tk.Label(root,font=f)
    GLabel_869["text"] = "Customer Id"
    GLabel_869.place(x=40,y=320,width=80,height=30)

    GLabel_460=tk.Label(root,font=f)
    GLabel_460["text"] = row6
    GLabel_460.place(x=120,y=320,width=80,height=30)

    GLabel_444=tk.Label(root,font=f)
    GLabel_444["text"] = row7
    GLabel_444.place(x=120,y=380,width=80,height=30)

    root.mainloop()

def f1():
    cur1=conn.cursor()
    cur1.execute("update (select booking.amount as amt, booking.nod as n, car.tariff as t from booking inner join car on booking.choice=car.regno) u set u.amt=u.n*u.t")
    conn.commit()
def f2():
    cur2=conn.cursor()
    chosen_car=cregno.get()
    data=[chosen_car]
    cur2.execute("update car set availability=\'N\' where car.regno=(:1)",data)
    conn.commit()
def insertbooking():
    bookingid=b
    id=tempid.get()#foreign key customer
    start_date=sdate.get()
    nd=nod.get()
    choose_type=ctype.get()
    chosen_car=cregno.get()
    cur=conn.cursor()
   
    
    data=[bookingid,start_date,nd,choose_type,chosen_car,id]
    cur.execute("insert into booking(bid,start_date,nod,type,choice,cust_id) values(:1,:2,:3,:4,:5,:6)",data)
    f1()
    f2()
    
    conn.commit()
    displaybill()
    showbookingtable()

def choosecar():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("300x400")
    root.title("SELECT CAR")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    cur = conn.cursor()
    choose_type=ctype.get()
    data=[choose_type]
    cur.execute("select regno,type,model,tariff from car where type=(:1) and availability=\'Y\'",data)
    row=cur.fetchall()
    for i in row:
        mess=tk.Label(root, text=i,font=f,width=300)
        mess.pack()

    a=tk.Label(root, text='Enter REG.NO of chosen car',font=f)
    a.place(x=30,y=290)
    a1=tk.Entry(root, textvariable=cregno)
    a1.place(x=220, y=290, width=60)

    booked=tk.Button(root, text='BOOK',font=f,bg='#eee4a9',command=insertbooking)
    booked.place(x=130, y=320, width=50)

    btn=tk.Button(root,text='Back',font=f,bg='light green',command=booking)
    btn.place(x=10,y=355, width=40)
    root.mainloop()
   
def booking():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('BOOKING')
    root.geometry("300x400")
    root.configure(bg='#c8b3e0')
    #reg no
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=11)
    cur = conn.cursor()
    GLabel_800=tk.Label(root,font=f)
    GLabel_800["text"] = "Booking ID"
    GLabel_800.place(x=50,y=50,width=70,height=25)
    GMessage_304=tk.Label(root,font=f)
    GMessage_304["text"] = b
    GMessage_304.place(x=140,y=50,width=100,height=25)

    GLabel_23=tk.Label(root,font=f)
    GLabel_23["text"] = "Start Date"
    GLabel_23.place(x=50,y=100,width=70,height=25)
    GLineEdit_351=tk.Entry(root)
    GLineEdit_351["textvariable"] = sdate
    GLineEdit_351.place(x=150,y=100,width=70,height=25)

    GLabel_682=tk.Label(root,font=f)
    GLabel_682["text"] = "No.of Days"
    GLabel_682.place(x=50,y=150,width=70,height=25)

    GLineEdit_511=tk.Entry(root)
    GLineEdit_511["textvariable"] = nod
    GLineEdit_511.place(x=150,y=150,width=70,height=25)
    

    cur.execute("select distinct(type) from car")
    t=cur.fetchall()
    
    GMessage_436=tk.Label(root,text=t,bg='#11887d',font=f)
    GMessage_436.place(x=45,y=230,width=180,height=35)

    l=tk.Label(root, text='Types of Cars', font=f)
    l.place(x=40, y=195, width=200)
    GLabel_816=tk.Label(root,font=f)
    GLabel_816["text"] = "Choose Type"
    GLabel_816.place(x=50,y=300,width=90,height=25)
    GLineEdit_823=tk.Entry(root)
    GLineEdit_823["textvariable"] = ctype
    GLineEdit_823.place(x=150,y=300,width=70,height=25)

    GButton_637=tk.Button(root,font=f,bg='#eee4a9')
    GButton_637["text"] = "See Available Cars"
    GButton_637.place(x=80,y=350,width=120,height=30)
    GButton_637["command"] =choosecar

    root.mainloop()

def homepage():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("650x500")
    canvas1 = Canvas(root, width=650, height=500)
    canvas1.pack(fill="both", expand=True)
    image = Image.open(
        r"C:\Users\aravi\OneDrive\Desktop\pic1.jpg")
    image = image.resize((650, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=img,
                        anchor="nw")
    f=tkfont.Font(family='Bahnschrift SemiCondensed',size=25)
    l=tk.Label(root,text='AKA CAR RENTAL AGENCY',font=f,bg='light blue')
    l.place(x=160,y=30)
    l1=tk.Label(root,text="Contact us at : 9884092705 ")
    l1.place(x=470,y=460)
    b1=tk.Button(root, text='AGENT', bg='lavender',font=f, command=agent_user)
    b1.place(x=270,y=200)

    b2=tk.Button(root, text='CUSTOMER',bg='lavender',font=f, command=cust_login)
    b2.place(x=240,y=300)
    root.mainloop()

conn=cx_Oracle.connect('scott/tiger@localhost:1521/orcle123')
root=tk.Tk()
#root.geometry("700x200")
root.title("AKA CAR RENTAL AGENCY")

#setting tkinter window size
root.geometry("650x500")

delr=tk.StringVar()

upd=tk.StringVar()
updval=tk.IntVar()

var1=tk.StringVar()
var2=tk.StringVar()

val1=tk.StringVar()
val2=tk.StringVar()

clicked = tk.StringVar()
rno=tk.StringVar()
mod=tk.StringVar()
tarr=tk.IntVar()
availability=tk.StringVar()
#agent_user()
#del0()
#delcar()
#agent_displaycars()

c_id=tk.StringVar()
c_name=tk.StringVar()
c_age=tk.IntVar()
c_ph=tk.IntVar()
c_l=tk.StringVar()


tempid=tk.StringVar()
tempph=tk.IntVar()

#displaycust()
b=random.randrange(100,10000000,1)

sdate=tk.StringVar()
edate=tk.StringVar()
ctype=tk.StringVar()
cregno=tk.StringVar()
nod=tk.IntVar()

dbook=tk.IntVar()

homepage()
conn.commit()
conn.close()
