from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector import Error, connect
from tkinter import messagebox
#-----------------------------------------------------
global custid

class Homepage:
   
   def register():
      root.destroy()
      import page2
  
   def login():
      try:
         uservalue1 = uservalue.get()
         paswvalue1 = paswvalue.get()
         conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
         mycursor = conn.cursor(dictionary=True)
         sql = f"select * from customer where cust_ID={uservalue1}"
         mycursor.execute(sql)
         records = mycursor.fetchall()
         conn.commit()  
         for row in records:
            cust_id1 = row["cust_ID"]
            cust_name1 = row["cust_name"]
            cust_pwd1 = row["cust_pwd"]
         print("DB input :",cust_id1,cust_name1,cust_pwd1)
         print("user input:",uservalue1,paswvalue1)
         if cust_id1==int(uservalue1) and cust_pwd1==paswvalue1:
            user = Label(root,text = "You are valid user!!!",font="Arial 12 bold",bg='dodger blue')
            user.place(x=950,y=270)
            root.destroy() 
            import page4
                
      except Error as e:
         print("Error reading data from MySQL table", e)       
      finally: 
         mycursor.close()
         conn.close() 
         
     
   def forgetpwd1():
      try:
         user = Label(root,text = "Enter registered contact number as Login ID ",font="Arial 12 bold",bg='wheat1')
         user.place(x=950,y=270)
         contact1 = uservalue.get()
         conn = mysql.connector.connect(user="root",password="",host="localhost",database="auction")
         mycursor = conn.cursor()
         mycursor.execute(f"select cust_ID,cust_name,cust_pwd from customer where cust_contact='{contact1}'")
         msg= mycursor.fetchone()
         print("msg -",msg)
         cid=msg[0]
         cname=msg[1]
         cpwd =msg[2]
         print("custmer id:",cid,cname,cpwd)
         uservalue.set(" ")
         messagebox.showinfo('Already exist !!!',f"Dear {cname},\n Your customer Id is  {cid} \n your password is  {cpwd}")
      except Exception as e:
         print(e)
      finally:
         mycursor.close()
         conn.close()
         # root.destroy() 
         # import page4         
#-----------------------------------------------------
print("Welcome..............")
root = Tk()
root.geometry("1300x700")
root.title("E-Auction")
root.maxsize(width=1300,height=650)
root.minsize(width=1300,height=650)
root['bg'] = 'wheat1'
root.iconbitmap('E:\\Itvedant project\\code\\auct.ico')

image = Image.open('E:\\Itvedant project\\code\\8.png')
image = image.resize((1270, 200), Image. ANTIALIAS)
my_img = ImageTk. PhotoImage(image)
labl=Label(root,image=my_img)
labl.place(x=10,y=10)
#-------------------------------------------
user = Label(root,text = "Login ID :",font="Arial 16 bold",bg='wheat1')
pwd = Label(root,text="Password  :",font="Arial 16 bold",bg='wheat1')
user.place(x=950,y=300)
pwd.place(x=950,y=350)

uservalue = StringVar()
paswvalue = StringVar()

userentry = Entry(root,textvariable=uservalue,font="Arial 16 bold")
passentry = Entry(root,textvariable=paswvalue,font="Arial 16 bold")
userentry.place(x=1100,y=300,height=25,width=150)
passentry.place(x=1100,y=350,height=25,width=150)

hproduct = Label(root,text="Home products \n\n ARTwork\n Gifts \n Travel tickets \n Home decorator \n Furniture",font="Arial 14 bold",bg='wheat1')
hproduct.place(x=50,y=250)
vproduct = Label(root,text="Vehicles \n\n Cycle \n Motor Bike \n Race car \n Autorikshaw \n Cars",font="Arial 14 bold",bg='wheat1')
vproduct.place(x=270,y=250)
product = Label(root,text="Cloths & garmments \n\n Leather jackets\n Princes dresses \n Hanloom cloths \n Shoes \n Fashionabale dresses ",font="Arial 14 bold",bg='wheat1')
product.place(x=450,y=250)
product = Label(root,text="Real Estate \n\n Plots \n Banglow \n 2BHK Flats \n 3BHK Flats ",font="Arial 14 bold",bg='wheat1')
product.place(x=750,y=250)
product = Label(root,text="!!!  Open  your  Store  and  start selling  today  !!! ",font="Arial 22 bold",bg='wheat1')
product.place(x=100,y=500)
product = Label(root,text="",font="Arial 22 bold",bg='white',width=70)
product.place(x=1,y=600)

but11 = Button(root,text="Register",command=Homepage.register,font="Arial 14 bold",bg='wheat1',width=10)
but11.place(x=960,y=430)
but1 = Button(root,text="Login",command=Homepage.login,font="Arial 14 bold",bg='wheat1',width=10)
but1.place(x=1120,y=430)
but2= Button(root,text="Forget password",command=Homepage.forgetpwd1,font="Arial 10 bold",bg='wheat1',width=15)
but2.place(x=1120,y=480)
custid=uservalue.get()
root.mainloop()
#-----------------------------------------------
