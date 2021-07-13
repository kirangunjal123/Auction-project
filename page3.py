import random
from tkinter import *
from typing import List
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os, shutil
from datetime import date,timedelta

class Product:
   global filename
   def pathofimage():      
    Product.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
    lablpath=Label(root,text= Product.fileName ,font="Arial 10 bold ",bg="wheat1")
    lablpath.place(x=120,y=570)    
    image1 = Image.open(Product.fileName )
    image1 = image1.resize((370,370), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    labl=Label(root,image=my_img1)
    labl.place(x=70,y=200)      
    os.chdir('c:\\')
    os.system('mkdir BACKUP')
    Product.fileName=shutil.move(Product.fileName ,'c:\\')    
    

   def additem():
    try:
     imagepath= Product.fileName 
     cust_id=int(custid.get())
     prod_id= random.randint(100,200)
     prod_name=prodname.get()
     prod_type=lst.get(lst.curselection())
     print("Data type :",type(prod_type))
     if prod_type is None:
         prod_type="Other"
     prod_detail=proddetail.get("1.0",END)
     start_bid=float(maxbid.get())
     day_bid=int(durbid.get())
     startdate=date.today()
     enddate=(startdate + timedelta(days = day_bid))
     print(prod_id,cust_id,prod_name,prod_type,prod_detail,imagepath,Product.fileName )
     flag=False
     conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
     mycursor = conn.cursor()     

    #  sql11=f"select cust_ID from customer"
    #  mycursor.execute(sql11)
    #  idcust=mycursor.fetchall()
     
    #  for cid in idcust:
    #     if cust_id == cid:   
    #         flag= True
       
     sql1 =f"insert into product(prod_ID,prod_type,prod_name,prod_detail,prodpic_path,cust_ID) values({prod_id},'{prod_type}','{prod_name}','{prod_detail}','{imagepath}',{cust_id})"
     mycursor.execute(sql1)
     conn.commit()
     
     
     sql2 =f"insert into bid_table(prod_id,prod_bidvalue,bid_enddate,cust_ID,bid_startdate) values({prod_id},{start_bid},'{enddate}',{cust_id},'{startdate}')"
     mycursor.execute(sql2)
     conn.commit()

     messagebox.showinfo('Success',f"Dear Customer,\nYou have successfully submitted your product.\n Poduct ID is {prod_id}")
          
    except Exception as e:
      print(e)
   
    finally:         
     print(prod_id,prod_name,prod_type,prod_detail,start_bid)
    #  mycursor.close()
    #  conn.close()         
 
   def homepage():
       root.destroy()
       import page4
   
#-----------------------------------------------------
root = Tk()
root.geometry("1300x700")
root.title("E-Auction")
root.maxsize(width=1300,height=700)
root.minsize(width=1300,height=700)
root['bg'] = 'wheat1'
root.iconbitmap('E:\\Itvedant project\\code\\auct.ico')
print("************ WELCOME ******************")
image = Image.open('E:\\Itvedant project\\code\\8.png')
image = image.resize((1270,150), Image. ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
labl=Label(root,image=my_img)
labl.place(x=10,y=10)
#----------------------------------------------------------
b=Button(root,text="Upload Product Image(.png)",command = Product.pathofimage,font="Arial 12 bold",bg='wheat1')
b.place(x=100,y=600)
# lablpath=Label(root,text="file path",font="Arial 10 bold ",bg="dodger blue")
# lablpath.place(x=80,y=570)

lablID=Label(root,text="Customer ID:",font="Arial 14 bold ",bg="wheat1")
lablID.place(x=495,y=230)
custid= StringVar()
custid1=Entry(root,text="customer id",textvariable =custid,font="Arial 14 bold",width=15)
custid1.place(x=650,y=230,height=30)

labl=Label(root,text="Product name:",font="Arial 14 bold ",bg="wheat1")
labl.place(x=495,y=270)

prod_name= StringVar()
prodname=Entry(root,text="Product name:",textvariable =prod_name,font="Arial 14 bold",width=15)
prodname.place(x=650,y=270,height=30)

prodtype=Label(root,text="Product type:",font="Arial 14 bold",width=10,bg="wheat1")
prodtype.place(x=850,y=240,height=30)

prod_typelist=StringVar()
list1 = ['Furniture','Home decorator','Tickets','Vehicle-Cycle','Vehicle-Bike','Vehicle-4wheeler','Jewellary','Cloths','Antique item','Flats','Plots','Bungalow','Other']
lst= Listbox(root,listvariable=prod_typelist,font="Arial 12 bold",height=13)
lst.place(x=1000,y=240)
for item in list1:
    lst.insert(END,item)
#data=lst.get(lst.curselection())  -To read the selected data from list
labl1=Label(root,text="Product details:",font="Arial 14 bold ",bg="wheat1")
labl1.place(x=495,y=310)

prod_detail= StringVar()
proddetail=Text(root,font="Arial 14 bold",width=40,height=6)
proddetail.place(x=500,y=350)

labl1=Label(root,text="Add product ",font="Arial 18 bold",bg="wheat1")
labl1.place(x=50,y=170)

# labl=Label(root,text="Current bid(Rupees)   :",font="Arial 14 bold",bg="dodger blue",borderwidth=4)
# labl.place(x=500,y=500)
# curbid=Label(root,text="current bid",font="Arial 14 bold",bg="dodger blue",borderwidth=4)
# curbid.place(x=730,y=500,width=150)
labl2=Label(root,text="Starting bid(Rupees)  :",font="Arial 14 bold",bg="wheat1",borderwidth=4)
labl2.place(x=500,y=500)

labl22=Label(root,text="Duration of bid(Days) :",font="Arial 14 bold",bg="wheat1",borderwidth=4)
labl22.place(x=500,y=550)
durbid=IntVar()
durbid=Entry(root,bg="white",textvariable=durbid,font="Arial 14 bold")
durbid.place(x=730,y=550,height=30,width=150)
maxbid=IntVar()
curbid=Entry(root,bg="white",textvariable=maxbid,font="Arial 14 bold")
curbid.place(x=730,y=500,height=30,width=150)
b1=Button(root,text="Submit",command = Product.additem,width =12,font="Arial 14 bold",bg='wheat1',bd=6,relief=RAISED)
b1.place(x=730,y=600)

b4=Button(root,text="Home page",command =Product.homepage,width =12,font="Arial 14 bold",bg='wheat1',bd=6,relief=RAISED)
b4.place(x=1000,y=600)

root.mainloop()