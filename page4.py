from tkinter import *
from PIL import Image,ImageTk
from tkinter import Tk, ttk
import mysql.connector as mysql
from datetime import date

class Myproducts:
  def productforbid():
    # setup treeview
    columns = ('Prod_ID', 'Product_type', 'Product_name', 'prod_detail')
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.place(x=50,y=320)       
    # setup columns attributes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=300, anchor=CENTER)
    # fetch data
    con = mysql.connect(host='localhost', user='root', password='', database='auction')
    c = con.cursor()
    ddate=date.today()
    c.execute(f'SELECT * FROM product LEFT JOIN bid_table ON bid_enddate>{ddate}')
    # populate data to treeview
    for rec in c:
        tree.insert('', 'end', value=rec)
  def myproduct():
    columns = ('Prod_ID', 'Product_type', 'Product_name', 'prod_detail')
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.place(x=50,y=320)       
    # setup columns attributes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=300, anchor=CENTER)
    # fetch data
    con = mysql.connect(host='localhost', user='root', password='', database='auction')
    c = con.cursor()
    custid= cust_id.get()
    c.execute(f'SELECT * FROM product where cust_ID={custid}')
    # populate data to treeview
    for rec in c:
        tree.insert('', 'end', value=rec)   
  def bidoneproduct():
      root.destroy()
      import page5
  def addproduct():
      root.destroy()
      import page3
  def homepage():
      root.destroy()
      import page1
  def aboutus():
      root.destroy()
      import page6
 
#-----------------------------------------------------
root = Tk()
root.geometry("1300x700")
root.title("E-Auction")
root.maxsize(width=1300,height=700)
root.minsize(width=1300,height=700)
# root['bg'] = 'dodger blue'
root.iconbitmap('E:\\Itvedant project\\code\\auct.ico')
image = Image.open('E:\\Itvedant project\\code\\8.png')
image = image.resize((1270, 200), Image. ANTIALIAS)
my_img = ImageTk. PhotoImage(image)
labl=Label(root,image=my_img)
labl.place(x=10,y=10)
image1 = Image.open('E:\\Itvedant project\\code\\6.png')
image1 = image1.resize((1270, 100), Image. ANTIALIAS)
my_img1 = ImageTk. PhotoImage(image1)
labl=Label(root,image=my_img1)
labl.place(x=10,y=590)

lbl=Label(root,text="Your customer Id :",font="Arial 12 bold")
lbl.place(x=10,y=280)
cust_id = IntVar()
cust_entry= Entry(root,textvariable=cust_id,font="Arial 12 bold",width=8)
cust_entry.place(x=155,y=280)

b1=Button(root,text="Products for bid",command = Myproducts.productforbid,font="Arial 14 bold",bg='wheat1',width=20)
b1.place(x=10,y=230)
b2=Button(root,text="Your products",command = Myproducts.myproduct,font="Arial 14 bold",bg='wheat1',width=21)
b2.place(x=260,y=230)
b3=Button(root,text="Add product for bid",command = Myproducts.addproduct,font="Arial 14 bold",bg='wheat1',width=20)
b3.place(x=522,y=230)
b4=Button(root,text="Bid your interested product",command = Myproducts.bidoneproduct,font="Arial 14 bold",bg='wheat1',width=26)
b4.place(x=772,y=230)
b5=Button(root,text="Log out",command = Myproducts.homepage,font="Arial 14 bold",bg='wheat1',width=14)
b5.place(x=1095,y=230)

root.mainloop()