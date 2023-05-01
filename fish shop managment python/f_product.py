from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class f_productclass:
    def __init__(self,root):
      
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()
        #============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()  
        self.var_cat=StringVar()
        self.cat_list=[]
        self.fetch_cat()
        self.var_name=StringVar()
        self.var_QNT=StringVar()
        self.var_Weight=StringVar()
        self.var_Price=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)


         #=====title======
        title=Label(product_Frame,text="F_Product Details",font=("times new roman",20,"italic","bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        
        lbl_category=Label(product_Frame,text="Category ",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=60)
        lbl_name=Label(product_Frame,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=100)
        #lbl_QNT=Label(product_Frame,text="QNT ",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=140)
        lbl_WEIGHT=Label(product_Frame,text="Weight",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=140)
        lbl_price=Label(product_Frame,text="Price",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=180)
        

      #  txt_category=Label(product_Frame,text="Category ",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=60)
        
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)



        #cmb_name=ttk.Combobox(product_Frame,textvariable=self.var_name,values=('Select'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        #cmb_name.place(x=150,y=110,width=200)
        #cmb_name.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=('times new roman',15,'italic'),bg="lightyellow").place(x=150,y=100,width=200)
        #txt_name=Entry(product_Frame,textvariable=self.var_QNT,font=('times new roman',15,'italic'),bg="lightyellow").place(x=150,y=140,width=200)
        
        txt_name=Entry(product_Frame,textvariable=self.var_Price,font=('times new roman',15,'italic'),bg="lightyellow").place(x=150,y=140,width=200)
        txt_name=Entry(product_Frame,textvariable=self.var_Weight,font=('times new roman',15,'italic'),bg="lightyellow").place(x=150,y=180,width=200)
        #===button===

        btn_Add=Button(product_Frame,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=5,y=400,width=100,height=30)
        btn_Upadate=Button(product_Frame,text="Upadate",command=self.update,font=("times new roman",15,"italic"),bg="pink",cursor="hand2").place(x=118,y=400,width=100,height=30)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="Red",cursor="hand2").place(x=230,y=400,width=100,height=30)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("times new roman",15,"italic"),bg="Blue",cursor="hand2").place(x=340,y=400,width=100,height=30)
       #===search frame====
        searchFrame=LabelFrame(self.root,text="Search Employee",font=("times new roman",15,"italic","bold"),bd=2,bg="white")
        searchFrame.place(x=500,y=10,width=600,height=80)
       



       ###############options#################
      
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','Name','Category',),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_search.place(x=12,y=10,width=180)
        cmb_search.current(0)



        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"italic"),bg="lightyellow").place(x=220,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=440,y=10,width=150,height=26)
         #====product details===

        product_Frame=Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=480,y=100,width=600,height=390)
        scrolly=Scrollbar(product_Frame,orient=VERTICAL)
        scrollx=Scrollbar(product_Frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(product_Frame,columns=("p_id","category","name","QNT","weight","price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("p_id",text="p_id")
        self.product_table.heading("category",text="Category")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("QNT",text="Qnt")
        self.product_table.heading("weight",text="weight")
        self.product_table.heading("price",text="price")
        
        self.product_table["show"]="headings"
        
        self.product_table.column("p_id",width=90)
        self.product_table.column("category",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column("QNT",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("weight",width=100)
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
       # self.fetch_cat()

        #=====function======
    def fetch_cat(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
         cur.execute("Select name  from f_category")
         cat=cur.fetchall()
         self.cat_list.append("Empty")
         if len(cat)>0:
            del self.cat_list[:]
            self.cat_list.append("select")
            for i in cat:

             self.cat_list.append(i[0])
        # print(cat)

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   

    def add(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_cat.get()=="select" or self.var_name.get()=="":
          messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:

          cur.execute("Select * from f_product where name=?",(self.var_name.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error","Product already assigned, try different",parent=self.root)
          else:
            cur.execute("Insert into f_product(Category,name,weight,price) values(?,?,?,?)",(
              self.var_cat.get(),
              self.var_name.get(),
              #self.var_QNT.get(),
              self.var_Weight.get(),
              self.var_Price.get(),
              
             
            ))
            con.commit()
            messagebox.showinfo('success','product Added Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from f_product")
        rows=cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
          self.product_table.insert('',END,values=row)

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
      f=self.product_table.focus()
      content=(self.product_table.item(f))
      row=content['values']
      # print(row)
      
      self.var_name.set(row[1]),
      #self.var_.set(row[2]),
      #self.var_gender.set(row[3]),
      #self.var_contact.set(row[4]),
      #self.var_dob.set(row[5]),
      #self.var_doj.set(row[6]),
      #self.var_pass.set(row[7]),
      #self.var_utype.set(row[8]),
      #self.var_address.set(row[9]),
      #self.var_salery.set(row[10]),
      
    #==update===
    def update(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_name.get()=="":
          messagebox.showerror("Error","product name Must be required",parent=self.root)
        else:

          cur.execute("Select * from f_product where name=?",(self.var_name.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid product name",parent=self.root)
          else:
            cur.execute("Update employee set name=?,weight=?,price=?,where cat=?",(
             
              self.var_name.get(),
              self.var_Weight.get(),
              self.var_Price.get(),
              self.var_cat.get(),
              #self.var_dob.get(),
              #self.var_doj.get(),
              #self.var_pass.get(),
              #self.var_utype.get(),
              #self.var_address.get(),
              #self.var_salery.get(),
              #self.var_emp_id.get(),
            ))
            con.commit()
            messagebox.showinfo('success','product Updated Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
         if self.var_name.get()=="":
          messagebox.showerror("Error","product name Must be required",parent=self.root)
         else:

          cur.execute("Select * from f_product where name=?",(self.var_name.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid product name",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
            if op==True:
              cur.execute("delete from f_product where name=?",(self.var_name.get(),))
              con.commit()
              messagebox.showinfo("Delete","product Deleted Successfully",parent=self.root)
              self.clear()

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.var_address.set("")
        self.var_salery.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_searchby.get()=="Select":
          messagebox.showerror("Error","Select Search By Options",parent=self.root)
        elif self.var_searchtxt.get()=="":
          messagebox.showerror("Error","Search input should be reuired",parent=self.root)
        else:
          cur.execute("Select * from f_product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
             self.product_table.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found!!!",parent=self.root)
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":

  root=Tk()
  obj=f_productclass(root)
  root.mainloop()
        