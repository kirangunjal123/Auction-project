from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import random
#------------------------------------------
class DetailsException(Exception):
    def __init__(self,name1=None,pass11=None,passlen=None,pass1pass2=None,contact1=None,emailid1=None):
      self.name1=name1
      self.pass11=pass11
      self.passlen=passlen
      self.pass1pass2=pass1pass2
      self.contact1=contact1
      self.emailid1=emailid1

class Register:

  def pwd(pass1):
    if any(x.isdigit() for x in pass1):
      if any(x in("@","#","$") for x in pass1) :
        if any(x.isalpha() for x in pass1):
          return True
 
  def details():   
    try:
      name1=name.get()
      pass11=pass1.get()
      pass12=pass2.get()
      contact1=contact.get()
      emailid1=emailid.get()
      print(name1,pass11,pass12,contact1,emailid1)

      if name1 == '':
        raise DetailsException(name1="Please enter your good name")
      flag= Register.pwd(pass11)
      if flag is not True:
        raise DetailsException(pass11="Password should be alphnumeric and @,#,$")
      elif len(pass11)< 8:
        raise DetailsException(passlen="Password length should be greater than 8")
      elif pass11 != pass12:
        raise DetailsException(pass1pass2="Verified password not match with entered password")
      elif len(contact1)!= 10 and contact1.isdigit() == False:
        raise DetailsException(contact1="Contact number should be 10 digit number")
      elif '@' not in emailid1:
        raise DetailsException(emailid1="Enter the valid Email ID")
    except DetailsException as a:
      if a.name1 != None or a.pass11 != None or a.passlen != None or a.pass1pass2 != None or contact1 != None or a.emailid1 != None :
        note.config(text=a.name1,width ="100")
        note.config(text=a.pass11,width="50")
        note.config(text=a.passlen,width="50")
        note.config(text=a.pass1pass2,width="50")
        note.config(text=a.contact1,width="50")
        note.config(text=a.emailid1,width="50")                
    else:       
        note.config(text='')     
        print("All the bests")
        cust_id=random.randint(100,200)
        try:
          conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
          mycursor = conn.cursor()
          mycursor.execute(f"select cust_ID from customer where cust_name='{name1}' and cust_contact='{contact1}'")
          msg= mycursor.fetchone()
          print("msg -",msg)
          if msg is None:
            print("It does not exist")
            sql1 =f"insert into customer(cust_ID,cust_name,cust_pwd,cust_contact,cust_emailid) values({cust_id},'{name1}','{pass11}','{contact1}','{emailid1}')"
            mycursor.execute(sql1)
            conn.commit()
            messagebox.showinfo('Success',f"Welcome to E-Auction\n Your customer Id is {cust_id}")
          else :
            cid=msg[0]
            print("custmer id:",cid)
            messagebox.showinfo('Already exist !!!',f"Dear {name1}, you have already registered in E-Auction\n Your customer Id is {cid}")
        except Exception as e:
          print(e)
        finally:
          print(name1,pass11,pass12,contact1,emailid1)
          mycursor.close()
          conn.close()
          del conn         
          root.destroy()
          import page1       
#------------------------------------------
root = Tk()
root.geometry("1300x700")
root.title("E-Auction")
root.maxsize(width=1300,height=650)
root.minsize(width=1300,height=650)
root['bg'] = 'wheat1'

image = Image.open('E:\\Itvedant project\\code\\8.png')
image = image.resize((1270, 200), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
labl=Label(root,image=my_img)
labl.place(x=10,y=10)

#------------------------------------------
wel = Label(root,text="!!!  Welcome to E-Auction !!!",font="Arial 22 bold",bg='white')
wel.place(x=350,y=160)
label0 = Label(root,text="USER DETAILS :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=230)
label0 = Label(root,text="User name             :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=300)
label0 = Label(root,text="Password              :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=350)
label0 = Label(root,text="Verified password :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=400)
label0 = Label(root,text="Contact number    :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=450)
label0 = Label(root,text="Email ID                 :",font="Arial 16 bold",bg='wheat1')
label0.place(x=230,y=500)  

name= StringVar()
pass1= StringVar()
pass2= StringVar()
contact= StringVar()
emailid= StringVar()
en_name=Entry(root,textvariable=name,font="Arial 14 ")
en_name.place(x=430,y=300,height=28,width=200)
en_pass1=Entry(root,textvariable=pass1,font="Arial 14 ")
en_pass1.place(x=430,y=350,height=28,width=200)
en_pass2=Entry(root,textvariable=pass2,font="Arial 14 ")
en_pass2.place(x=430,y=400,height=28,width=200)
en_contact=Entry(root,textvariable=contact,font="Arial 14 ")
en_contact.place(x=430,y=450,height=28,width=200)
en_email=Entry(root,textvariable=emailid,font="Arial 14 ")
en_email.place(x=430,y=500,height=28,width=200)

image1 = Image.open('E:\\Itvedant project\\code\\3.png')
image1 = image1.resize((400, 300), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)
labl1=Label(root,image=my_img1)
labl1.place(x=750,y=290)

b1= Button(root,text = 'SUBMIT',font="Arial 16 bold",bg='wheat1',command=Register.details)
b1.place(x=440,y=550)
note = Label(root,text="Note-Contact number should be unique for each user",font="Arial 12 bold",bg='wheat1',fg="red")
note.place(x=230,y=260)
#-----------------------------------------
root.mainloop()
