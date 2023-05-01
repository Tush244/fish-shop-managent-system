from tkinter import*
from tkinter import font
#from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierclass:
  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()


        # all variable

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()  
       
       
        self.var_supp_id=StringVar()   
        self.var_name=StringVar()
        self.var_contact=StringVar() 
        self.var_desc=StringVar()
        



        ################ search frame ##########
        #searchFrame=LabelFrame(self.root,text="Search Supplier",font=("times new roman",15,"italic","bold"),bd=2,bg="white")
       # searchFrame.place(x=300,y=20,width=600,height=70)
       



       ###############options#################
      
        lbl_search=LabelFrame(self.root,text="Search by supp_id",font=("times new roman",15,"italic"))
        lbl_search.place(x=700,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("times new roman",15,"italic"),bg="lightyellow").place(x=750,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=930,y=80,width=130,height=26)



        #=====title======
        title=Label(self.root,text="Supplier Details",font=("times new roman",20,"italic","bold"),bg="black",fg="white").place(x=60,y=10,width=1000,height=40)



        #===content====
        # row1

        lbl_suppid=Label(self.root,text="Supp ID",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=80)
        txt_suppid=Entry(self.root,textvariable=self.var_supp_id,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=180,y=80,width=200)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=150,width=200)
       
       # ==row 2==
        lbl_Name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=180,y=120,width=200)
        
       #==row3==
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=180,y=160,width=200)
        
        #===row4==
        lbl_desc=Label(self.root,text="Description",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=200)
        
        self.txt_desc=Entry(self.root,textvariable=self.var_desc,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=180,y=200,width=470,height=50)
       # self.txt_desc.place(x=150,y=270,width=300,height=60)
      
        #==buttons===
        btn_Add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=180,y=380,width=110,height=35)
        btn_Upadate=Button(self.root,text="Upadate",command=self.update,font=("times new roman",15,"italic"),bg="pink",cursor="hand2").place(x=300,y=380,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="Red",cursor="hand2").place(x=420,y=380,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"italic"),bg="Blue",cursor="hand2").place(x=540,y=380,width=110,height=35)
       
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=400,height=350)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=("supp_id","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("supp_id",text="Supp_id")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
       
        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("supp_id",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
       
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================================================================================
    def add(self):
        con=sqlite3.connect(database=r'TUSHARG244.db')
        cur=con.cursor()
        try:
            if self.var_supp_id.get()=="":
             messagebox.showerror("Error","Supplier ID Must be required",parent=self.root)
            else:
              cur.execute("Select * from supplier where supp_id=?",(self.var_supp_id.get(),))
              row=cur.fetchone()
              if row!=None:
                messagebox.showerror("Error","This  Supplier ID already assigned, try different",parent=self.root)
              else:
                cur.execute("Insert into supplier(supp_id,name,contact,desc) values(?,?,?,?)",(
                self.var_supp_id.get(),
                self.var_name.get(),
                self.var_contact.get(),
                self.var_desc.get(),
             
                ))
                con.commit()
                messagebox.showinfo('Success','Supplier Added Successfully',parent=self.root)
                self.show()
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from supplier")
        rows=cur.fetchall()
        self.SupplierTable.delete(*self.SupplierTable.get_children())
        for row in rows:
          self.SupplierTable.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
      f=self.SupplierTable.focus()
      content=(self.SupplierTable.item(f))
      row=content['values']
      # print(row)
      self.var_supp_id.set(row[0]),
      self.var_name.set(row[1]),
      self.var_contact.set(row[2]),
     # self.var_desc.delete(),
      self.var_desc.set([3])
      
      
    #==update===
    def update(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_supp_id.get()=="":
          messagebox.showerror("Error","Supplier ID Must be required",parent=self.root)
        else:
          cur.execute("Select * from supplier  where supp_id=?",(self.var_supp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid supplier ID",parent=self.root)
          else:
            cur.execute("Update supplier set name=?,contact=?,desc=? where supp_id=?",(

             
            self.var_name.get(),
            self.var_contact.get(),
            self.var_desc.get(),
            self.var_supp_id.get(),
            ))
            con.commit()
            messagebox.showinfo('success','Supplier Updated Successfully',parent=self.root)
            self.show()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_supp_id.get()=="":
          messagebox.showerror("Error","Supplier ID Must be required",parent=self.root)
        else:
          cur.execute("Select * from supplier where supp_id=?",(self.var_supp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
          if op==True:
            cur.execute("delete from Supplier where supp_id=?",(self.var_supp_id.get(),))
            con.commit()
            messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
            self.clear()

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
      self.var_supp_id.set("")
      self.var_name.set("")
      self.var_contact.set("")
      self.var_desc.set("")
      self.var_searchtxt.set("")
      self.show()


    def search(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_searchtxt.get()=="":
          messagebox.showerror("Error","Supplier id must be reuired",parent=self.root)
        else:
          cur.execute("Select * from supplier where supp_id=?",(self.var_searchtxt.get(),))
          row=cur.fetchone()
          if row!=None:
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            
            self.SupplierTable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found!!!",parent=self.root)
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
  root=Tk()
  obj=supplierclass(root)
  root.mainloop()