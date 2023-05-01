from random import randint, random
from re import L
#from re import L
from tkinter import*
from tkinter import messagebox

from mysqlx import Column
#from tkinter.ttk import Labelframe
#from turtle import title
root=Tk()
root.title("Billing ")
root.geometry("1280x720")

c_name=StringVar()
c_mobile=StringVar()
item=StringVar()
Rate=IntVar()
Weight=IntVar()
bill_no=StringVar()
x=random,randint(1000,9999)
bill_no.set(str(x))
global l
l=[]
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t Welcome our shop")
    textarea.insert(END,f"\n\n Bill Number :\t\t{bill_no.get()}")
    textarea.insert(END,f"\n\n Customer Name :\t\t{c_name.get()}")
    textarea.insert(END,f"\n\n Mobile no. :\t\t{c_mobile.get()}")
    textarea.insert(END,f"\n====================================")
    textarea.insert(END,f"\n Product\t\t weight \t\t Price")
    textarea.insert(END,f"\n====================================")
    textarea.config(font=("times new roman",14,"italic","bold"))



def additm():
    n=Rate.get()
    m=Weight.get()*n
    l.append(m)
    #if item.get()==" ":
    if item.get()=='':
        messagebox.showerror('Error','please enter the item')
    else:
        textarea.insert(END,f'{item.get()}\t\t{Weight.get()}\t\t{m}')


def gbill():
    welcome()
    textarea.insert(END,f"\n====================================")
    textarea.insert(END,f"\n Total Paybill Ammount :\t\t\t{sum(l)}")
    textarea.insert(END,f"\n====================================")


#=====tiitle


title=Label(root,text="Billing Software",bg="red",fg="white",font=('times new roman',20,'italic','bold'),bd=12)

title.pack(fill=X)
#=====customer detail
F1=LabelFrame(root,text="Customer Details",font=("times new roman",20,'italic',"bold"),relief=GROOVE,bd=10,bg="black",fg="gold")
F1.place(x=0,y=80,relwidth=1)
cname_lbl=Label(F1,text="Customer Name",font=('times new roman',17,'italic','bold'),bg="black",fg="white")
cname_lbl.grid(row=0,column=0,padx=10,pady=5)

cname_txt=Entry(F1,width=15,font=("times new roman",15,"italic","bold"),relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cmobile_lbl=Label(F1,text="Mobile no.",font=('times new roman',17,'italic','bold'),bg="black",fg="white")
cmobile_lbl.grid(row=0,column=2,padx=10,pady=5)

cmobile_txt=Entry(F1,width=15,font=("times new roman",15,"italic","bold"),relief=SUNKEN,textvariable=c_mobile)
cmobile_txt.grid(row=0,column=3,padx=10,pady=5)

#====product Details
F2=LabelFrame(root,text="Product Details",font=("times new roman",20,'italic',"bold"),relief=GROOVE,bd=10,bg="black",fg="gold")
F2.place(x=20,y=180,width=630,height=500)

item=Label(F2,text="Product Name",font=("times new roman",17,"italic","bold"),bg="black",fg="lightgreen")
item.grid(row=0,column=0,padx=30,pady=20)
item_txt=Entry(F2,width=20,font=("times new roman",17,"italic","bold"),textvariable=item)
item_txt.grid(row=0,column=1,padx=30,pady=20)

rate=Label(F2,text="Product Rate",font=("times new roman",17,"italic","bold"),bg="black",fg="lightgreen")
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font=("times new roman",17,"italic","bold"),textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

weight=Label(F2,text="Product weight",font=("times new roman",17,"italic","bold"),bg="black",fg="lightgreen")
weight.grid(row=2,column=0,padx=30,pady=20)
weight_txt=Entry(F2,width=20,font=("times new roman",17,"italic","bold"),textvariable=Weight)
weight_txt.grid(row=2,column=1,padx=30,pady=20)

#====button

btn1=Button(F2,text="Add item",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text="Generate Bill",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text="Clear",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",)
btn3=Button(F2,text="Clear",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",)
btn3=Button(F2,text="Clear",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4=Button(F2,text="Exit",font=("times new roman",17,"italic","bold"),padx=5,pady=10,bg="lime",width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

#======bill area
F3=Frame(root,relief=GROOVE,bd=18)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text="Bill Area",font=("times new roman",17,"italic","bold"),relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()


welcome()

root.mainloop()