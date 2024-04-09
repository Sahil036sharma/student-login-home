from tkinter import *
from tkinter import messagebox 
from tkinter .ttk import Combobox
from PIL import Image,ImageTk
from PIL import Image
from tkcalendar import Calendar, DateEntry
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sahilsharma"
)
cursor = db.cursor()
#login window
def login():
    root1=Tk()
    root1.geometry("800x600+120+10")
    root1.title("login page")
    root1.configure(bg="grey81")
    root1.resizable(width = True, height = True)
    l2 = Label(root1, text = '$@LOGIN FORM$',width= '42',height= "2",
               font=('Monotype Corsiva',60,'bold')
               ,bg="green",fg="white")
    l2.pack()
    
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sahilsharma"
    )
    cursor = db.cursor()
    def forget():
        root4 = Tk()
        root4.geometry('600x500')
        root4.title('forget password')
        root4.resizable(width = True, height = True)
        root4.config(bg='grey81')  

        def submitfg():
            password=e3.get()
            USER=e2.get()
            query="UPDATE info2 SET password = %s where username = %s"
            values=(password,USER)
            cursor.execute(query,values)
            db.commit()
            db.close()
            messagebox.showinfo("update","Password updated succesfully")
            root4.destroy()

        l1 = Label(root4, text = 'Reset Password',width= '42',height= "2",font=("Monotype Corsiva",60,'bold'),bg="green",fg="white")
        l1.pack()

        l0 = Label(root4,text='Username:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
        l0.place(x=200,y=246)

        l1 = Label(root4,text='New Pasword:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
        l1.place(x=200,y=346)

        l2 = Label(root4,text='Confirm Pasword:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
        l2.place(x=200,y=446)

        e2= Entry(root4,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
        e2.place(x=540,y=246)

        e3= Entry(root4,width=18,show="*",font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
        e3.place(x=540,y=346)

        e4= Entry(root4,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
        e4.place(x=540,y=464)


        btn = Button( root4 ,text = 'Submit', font = ('italic',25,'bold'),
                width = 7, height = 1, bg = 'grey81', fg = 'black',
                bd = 10, relief = 'groove',activebackground='grey',command=submitfg)
        btn.place(x = 640, y = 550)
    def submit():
    
        name = e1.get()
        passwd = e2.get()
        query="use sahilsharma"
        cursor.execute(query)
     
        query = "SELECT * FROM info2 WHERE username=%s and password=%s"
        cursor.execute(query, (name,passwd))
        user_data = cursor.fetchone()

        if user_data ==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showinfo("Welcome","you are login sucessfully")
            
            
        
    l0 = Label(root1,text='Username:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
    l0.place(x=200,y=246)
    
    l3 = Label(root1,text='Password:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
    l3.place(x=200,y=320)
    e1= Entry(root1,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    
    e1.place(x=440,y=250)
    
    e2= Entry(root1,width=18,show="*",font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e2.place(x=440,y=330)
    
    b0 = Button( root1 ,text = '*Forget Password?*', font = ('Monotype Corsiva',20,'bold'),
            width = 15, height = 1, bg = 'grey81', fg = 'black',
            bd = 10, relief = 'groove',activebackground='grey',command=forget)
    b0.place(x = 600, y = 450)
    b4 = Button( root1 ,text = 'Login', font = ('italic',25,'bold'),
            width = 7, height = 1, bg = 'grey81', fg = 'black',
            bd = 10, relief = 'groove',activebackground='grey',command=submit)
    b4.place(x = 640, y = 550)
#signup###################################################
def signup():
    root.destroy()
    root2 = Tk()
    root2.geometry('600x500')
    root2.title('LOGIN')
    root2.resizable(width = True, height = True)
    root2.config(bg="grey81")
    
    
    def submit_form():
        firstname=e1.get()
        lastname=e2.get()
        email=e3.get()
        phne=e4.get()
        dob=cal.get()
        pincode=e5.get()
        address = e6.get()
        state=lstr.get()
        
        Query="CREATE TABLE IF NOT EXISTS ps_info (firstname VARCHAR(50),lastname VARCHAR(50),email VARCHAR(80),phoneno VARCHAR(50),DOB DATE,pincode int(50),address VARCHAR(150),state VARCHAR(90) )"
        cursor.execute(Query)

        query="INSERT INTO ps_info (firstname,lastname,email,phoneno,DOB,pincode,address,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(firstname,lastname,email,phne,dob,pincode,address,state)
        cursor.execute(query,values)
        
        messagebox.showinfo("SUBMIT","SUBMITION SUCCESS ")
        root2.destroy()
        next_window()

    
    l1 = Label(root2, text = '@  SIGNUP PAGE',width= '42',height= "2",font=('Monotype Corsiva',60,'bold')
               ,bg="green",fg="white")
    l1.pack()

    l2 = Label(root2,text='Name:*',fg='black',bg="grey81",font=('Monotype Corsiva', 25 , "bold"))
    l2.place(x=60,y=250)

    e1= Entry(root2,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e1.place(x=60,y=300)
    e2= Entry(root2,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e2.place(x=420,y=300)
    l3 = Label(root2,text='First Name',fg='black' ,bg="grey81",font=('italic', 18 ))
    l3.place(x=60,y=350)

    l4 = Label(root2,text='Last Name',fg='black' ,bg="grey81",font=('italic', 18 ))
    l4.place(x=420,y=350)

    l2 = Label(root2,text='Email-Id:*',bg="grey81",fg='black',font=('Monotype Corsiva', 23 , "bold"))
    l2.place(x=60,y=430)

    e3= Entry(root2,font=('Monotype Corsiva', 23 , "bold"),bg='white',fg='red')
    e3.place(x=60,y=470)

    l2 = Label(root2,text='Phone:*',bg="grey81",fg='black',font=('Monotype Corsiva', 23 , "bold"))
    l2.place(x=60,y=520)

    e4= Entry(root2,bg='white',fg='red',font=('Monotype Corsiva', 23 , "bold"))
    e4.place(x=60,y=570)
      
    l2 = Label(root2,text='DOB:*',bg="grey81",fg='black',font=('Monotype Corsiva', 23 , "bold"))
    l2.place(x=1000,y=300)

    cal = DateEntry(root2,font=('Monotype Corsiva', 23 , "bold"), width= 20, background= "green", foreground= "white",bd=2)
    cal.place(x=1000,y=350)
    l3 = Label(root2,text='Pin Code:*',bg="grey81",fg='black',font=('Monotype Corsiva',28,'bold'))
    l3.place(x=1000,y=430)
    e5= Entry(root2,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e5.place(x=1000,y=480)
    l4 = Label(root2,text='Address:* ',bg="grey81",fg='black',font=('Monotype Corsiva',28,'bold'))
    l4.place(x=450,y=400)
    e6= Entry(root2,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e6.place(x=450,y=480)
    
    l5 = Label(root2,text='State:* ',bg="grey81",fg='black',font=('Monotype Corsiva',28,'bold'))
    l5.place(x=1000,y=530)
    lst1=[
        "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh"
        ,"Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka"
        ,"Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram"
        ,"Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana"
        ,"Tripura","Uttarakhand","Uttar Pradesh","West Bengal"]

    lstr=StringVar()
    lstr.set("Select:")
    A=OptionMenu(root2,lstr,*lst1)
    A.config(bg="white",fg='red',font=('Monotype Corsiva',28,'bold'))
    A.place(x=1000,y=580)

    
    btn6 =Button( root2 ,text = 'Submit & Next', font = ('italic',25,'bold'),
        width = 15, height = 1, bg = 'black', fg = 'white',
        bd = 10, relief = 'groove',activebackground='green',command=submit_form)
    btn6.place(x = 100, y = 700)
    
    
def next_window():
    root3 = Tk()
    root3.geometry('600x500')
    root3.title('NEXT')
    root3.resizable(width = True, height = True)
    root3.config(bg='grey81')

    l1 = Label(root3, text = 'Personal Info',width= '42',height= "2",font=("monotype Corsiva",60,'bold'),bg="green",fg="white")
    l1.pack()
    
    

    def ps_submit():
        gender = V.get()
        coures = lstr1.get()
        user = e1.get()
        passwrd = e2.get()

        query = "CREATE TABLE IF NOT EXISTS  info2 (gender varchar(80),course VARCHAR(80),username VARCHAR(50) ,password VARCHAR (50))"
        cursor.execute(query)

        qey = "INSERT INTO info2 (gender,course,username,password )VALUES(%s,%s,%s,%s)"
        vls = (gender, coures, user, passwrd)
        cursor.execute(qey, vls)
        db.commit()
        messagebox.showinfo("Done", "Submitted")
        A = messagebox.askyesno("LOGIN", "you want to go on login page")
        if A > 0:
            root3.destroy()
            login()
        else:
            root3.destroy()
                    

    l2 = Label(root3,text='Gender:* ',bg="grey81",fg='black',font=('Monotype Corsiva',28,'bold'))
    l2.place(x=200,y=300)
    V = StringVar()
    V.set("Male") 

    D = Radiobutton(root3, text = 'MALE',bg="grey81",activebackground='grey81',fg='black',font=('arial',20,), variable = V, value = "Male")
    D.place(x=200,y=370)

    B = Radiobutton(root3, text = 'FEMALE',bg="grey81",activebackground='grey81',fg='black',font=('arial',20,), variable = V, value = "Female")
    B.place(x = 300, y = 370)

    C = Radiobutton(root3, text = 'OTHER',bg="grey81",activebackground='grey81',fg='black',font=('arial',20,), variable = V, value = "Other")
    C.place(x = 440, y = 370)

    l6 = Label(root3,text='Course:* ',bg="grey81",fg='black',font=('Monotype Corsiva',28,'bold'))
    l6.place(x=200,y=420)

    #combo box
    lst=["BA","B-PHARMACY","D-PHARMACY","BCA","MCA","B-TECH","M-TECH","B.ed","Hotal management","BBA","B.Sc","M.Sc"
        ]
    lstr1=StringVar()
    lstr1.set("Select:")
    Anop=OptionMenu(root3,lstr1,*lst)
    Anop.config(font=('Monotype Corsiva', 20), bg='white', fg='red', height =1,bd=2,relief="ridge" )
    Anop.place(x=200,y=500,width=300) 

    l0 = Label(root3,text='Username:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
    l0.place(x=1000,y=300)
    e1= Entry(root3,width=18,font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e1.place(x=1000,y=380)

    l3 = Label(root3,text='Password:*',bg="grey81",fg='black',font=('Monotype Corsiva',30,'bold'))
    l3.place(x=1000,y=450)

    e2= Entry(root3,width=18,show="*",font=('Monotype Corsiva', 25 , "bold"),bg='white',fg='red')
    e2.place(x=1000,y=520)

    btn7 = Button(root3 ,text = 'Submit & Done', font = ('algerian',25,'bold'),
                  width = 15, height = 1, bg = 'black', fg = 'white',
                  bd = 10, relief = 'groove',activebackground='green',command=ps_submit)
    btn7.place(x = 550, y = 650)    

def quit():
    root.destroy()
    A=messagebox.askyesno("EXIT","Click ok for quit")
    if A>0:
        root.destroy()
root=Tk()
root.geometry("800x600+120+10")
root.title("Hello Python")
root.configure(bg="white")
root.resizable(width = True, height = True)
photo=ImageTk.PhotoImage(Image.open("sahil.png"))
label=Label(root,text="label1",image=photo,height=2500,width=1700)

l1= Label(root, text = "* Registration Form *", font = ('italic',40,'bold'), width = 20,
          height = 1, bg="white", fg = 'black')
l1.pack()
b1 = Button(root, text = 'LOGIN', font = ('italic',25,'bold'),width = 7, 
            height = 1,bd=7, fg = 'black',  
            relief = 'solid',activebackground = 'grey81',command = login)
b1.place(x = 100, y = 400)
b2 = Button(root, text = 'SIGNUP', font = ('italic',25,'bold'),width = 8, 
            height = 1, bd=7, fg = 'black', relief = 'solid',
           activebackground = 'grey81', command = signup)
b2.place(x = 100, y = 500)
b3 = Button(root, text = 'QUIT', font = ('italic',25,'bold'),width = 6, 
            height = 1, fg = 'Black',bd=7,  relief = 'solid',
           activebackground = 'grey81',command = quit)
b3.place(x = 100, y = 600)
label.pack()
root.mainloop()
