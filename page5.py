from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
#-----------------------------------------------------
class Bidproduct:
   def homepage():
      root.destroy()
      import page4
   def submitbtn():
      custid1=custid.get()
      prodid1=prodid.get()
      conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
      mycursor = conn.cursor()
      mycursor.execute(f"select * from product where cust_ID={custid1} and prod_id={prodid1}")
      msg= mycursor.fetchone()
      conn.commit()
      print(msg)
      prodname.config(text=msg[2])
      prodtype.config(text=msg[1])
      proddetail.config(text=msg[3])

      mycursor.execute(f"select prod_bidvalue from bid_table where prod_id={prodid1}")
      msg1= mycursor.fetchone()
      conn.commit()
      print("max value of bid",msg1[0])
      textstr.set(msg1[0])

   def submitbidvalue():
      prodid1=prodid.get()
      newbid=float(curbid1.get())
      conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
      mycursor = conn.cursor()
      mycursor.execute(f"select prod_bidvalue from bid_table where prod_id={prodid1}")
      msg1= mycursor.fetchone()
      conn.commit()
      currbidval=float(msg1[0])
      if newbid>currbidval:
         print(newbid,currbidval,prodid1)
           
         mycursor.execute(f"UPDATE bid_table SET prod_bidvalue={newbid} where prod_id={prodid1}")
         conn.commit()
         messagebox.showinfo("Alert","Submitted successfully")

      else:
         messagebox.showinfo("Alert","New bid value should be maximum than existng value")

      # image1 = Image.open(msg[4])
      # image1 = image1.resize((370,370), Image.ANTIALIAS)
      # my_img1 = ImageTk.PhotoImage(image1)
      # labl=Label(root,image=my_img1)
      # labl.place(x=70,y=300)      
#-----------------------------------------------------
root = Tk()
root.geometry("1300x700")
root.title("E-Auction")
root.maxsize(width=1300,height=700)
root.minsize(width=1300,height=700)
root['bg'] = 'wheat1'
root.iconbitmap('E:\\Itvedant project\\code\\auct.ico')
image = Image.open('E:\\Itvedant project\\code\\8.png')
image = image.resize((1270, 200), Image. ANTIALIAS)
my_img = ImageTk. PhotoImage(image)
labl=Label(root,image=my_img)
labl.place(x=10,y=10)
labl1=Label(root,text="Product for bid :",font="Ariel 14 bold",bg='wheat1')
labl1.place(x=20,y=230)

lablID=Label(root,text="Customer ID:",font="Arial 14 bold ",bg="wheat1")
lablID.place(x=300,y=230)
custid= IntVar()
custid1=Entry(root,text="customer id",textvariable =custid,font="Arial 14 bold",width=12)
custid1.place(x=450,y=230,height=30)

prodID=Label(root,text="Product ID:",font="Arial 14 bold ",bg="wheat1")
prodID.place(x=600,y=230)
prodid= IntVar()
prodid1=Entry(root,text="Product id",textvariable =prodid,font="Arial 14 bold",width=12)
prodid1.place(x=750,y=230,height=30)

labl=Label(root,text="Product name:",font="Arial 14 bold ",bg="wheat1")
labl.place(x=300,y=300)

prodname=Label(root,font="Arial 14 bold",width=10)
prodname.place(x=450,y=300,height=30)

prodtype=Label(root,text="Product type:",font="Arial 14 bold",width=10,bg="wheat1")
prodtype.place(x=600,y=300,height=30)

prodtype=Label(root,font="Arial 14 bold",width=15)
prodtype.place(x=750,y=300,height=30)

labl1=Label(root,text="Product details:",font="Arial 14 bold ",bg="wheat1")
labl1.place(x=300,y=350)

proddetail=Label(root,font="Arial 14 bold",width=50,height=4)
proddetail.place(x=300,y=400)

labl=Label(root,text="Current bid(Rupees)   :",font="Arial 14 bold",bg="wheat1",borderwidth=4)
labl.place(x=300,y=520)

textstr=DoubleVar()
curbid=Entry(root,textvariable=textstr,state=DISABLED,font="Arial 14 bold",bg="wheat1",)
curbid.place(x=540,y=520,width=150)

labl2=Label(root,text="Enter bid value(Rupees):",font="Arial 14 bold",bg="wheat1",borderwidth=4)
labl2.place(x=300,y=570)

maxbid=IntVar()
curbid1=Entry(root,bg="white",textvariable=maxbid,font="Arial 14 bold")
curbid1.place(x=540,y=570,height=30,width=150)

b1=Button(root,text="Get details",command = Bidproduct.submitbtn,width =10,font="Arial 14 bold",bg='wheat1',bd=4,relief=RAISED)
b1.place(x=900,y=230)

b2=Button(root,text="Submit Bid value",command = Bidproduct.submitbidvalue,width =15,font="Arial 14 bold",bg='wheat1',bd=4,relief=RAISED)
b2.place(x=500,y=630)

b4=Button(root,text="Home page",command =Bidproduct.homepage,width =12,font="Arial 14 bold",bg='wheat1',bd=6,relief=RAISED)
b4.place(x=750,y=630)

root.mainloop()