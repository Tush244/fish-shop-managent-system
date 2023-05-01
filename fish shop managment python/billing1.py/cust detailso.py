from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class customerclass:
    def __init__(self,root):
      
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()
        # all variable

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()  
       
       
        self.var_cust_id=StringVar() 
        self.var_name=StringVar()  
        self.var_add=StringVar() 
        self.var_mob=StringVar()
         



        ################search frame##########
        searchFrame=LabelFrame(self.root,text="Search customer",font=("times new roman",15,"italic","bold"),bd=2,bg="white")
        searchFrame.place(x=300,y=20,width=600,height=70)
       



       ###############options#################
      
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','cust_id','Name','mobile'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_search.place(x=12,y=10,width=180)
        cmb_search.current(0)



        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"italic"),bg="lightyellow").place(x=220,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=440,y=10,width=150,height=26)



        #=====title======
        title=Label(self.root,text="Customer Details",font=("times new roman",20,"italic","bold"),bg="black",fg="white").place(x=60,y=100,width=1000)



        #===content====
        # row1

        lbl_custid=Label(self.root,text="Cust_ID",font=("times new roman",15,"italic","bold"),bg="white").place(x=30,y=150)
        lbl_name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=290,y=150)
      
        lbl_mob=Label(self.root,text="Mobile no.",font=("times new roman",15,"italic","bold"),bg="white").place(x=540,y=150)
        lbl_add=Label(self.root,text="Address",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=150)
      

        txt_custid=Entry(self.root,textvariable=self.var_cust_id,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=120,y=150,width=150)
       # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=150,width=200       
        
        ##cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female','other'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        ##cmb_gender.place(x=500,y=150,width=180)
        ##cmb_gender.current(0)
        
        
        ##txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=900,y=150,width=200)
       # ==row 2==
       ## lbl_Name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=190)
       ## lbl_dob=Label(self.root,text="DOB",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=190)
        ##lbl_doj=Label(self.root,text="DOJ",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=190)
      
      

        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=360,y=150,width=150)
        ##txt_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=190,width=200)
        ##txt_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=900,y=190,width=200)
      
       #==row3==
        ##lbl_email=Label(self.root,text="Email",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=230)
        ##lbl_pass=Label(self.root,text="Password",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=230)
        ##lbl_utype=Label(self.root,text="User Type",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=230)
             
      

        ##txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=150,y=230,width=200)
        ##txt_pass=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=230,width=200)
       # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=930,y=230,width=200)
        ##cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=('Admin','Employee'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        ##cmb_utype.place(x=930,y=230,width=200)
        ##cmb_utype.current(0)

       #===row4==
        ##lbl_address=Label(self.root,text="Address",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=270)
        ##lbl_salery=Label(self.root,text="Salery",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=270)
        self.txt_mob=Entry(self.root,textvariable=self.var_mob,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=650,y=150,width=150)
        ##self.txt_salery=Entry(self.root,textvariable=self.var_salery,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=270,width=200)
        self.txt_add=Entry(self.root,textvariable=self.var_add,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=910,y=150,width=150)
        #==buttons===
        btn_Add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=500,y=305,width=110,height=30)
        btn_Upadate=Button(self.root,text="Upadate",command=self.update,font=("times new roman",15,"italic"),bg="pink",cursor="hand2").place(x=650,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="Red",cursor="hand2").place(x=800,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"italic"),bg="Blue",cursor="hand2").place(x=950,y=305,width=110,height=30)
       
        cust_frame=Frame(self.root,bd=3,relief=RIDGE)
        cust_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(cust_frame,orient=VERTICAL)
        scrollx=Scrollbar(cust_frame,orient=HORIZONTAL)

        self.customerTable=ttk.Treeview(cust_frame,columns=("cust_id","name","mobile","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.customerTable.xview)
        scrolly.config(command=self.customerTable.yview)
        self.customerTable.heading("cust_id",text="Cust_id")
        self.customerTable.heading("name",text="Name")
        self.customerTable.heading("mobile",text="Mobile no.")
        self.customerTable.heading("address",text="Address")
        
        self.customerTable["show"]="headings"
        
        self.customerTable.column("cust_id",width=90)
        self.customerTable.column("name",width=100)
        self.customerTable.column("mobile",width=100)
        self.customerTable.column("address",width=100)
        
        self.customerTable.pack(fill=BOTH,expand=1)
        self.customerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================================================================================
    def add(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_cust_id.get()=="":
          messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
        else:

          cur.execute("Select * from customer where cust_id=?",(self.var_cust_id.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error","This  customer ID already assigned, try different",parent=self.root)
          else:
            cur.execute("Insert into customer(cust_id,name,mobile,address) values(?,?,?,?)",(
              self.var_cust_id.get(),
              self.var_name.get(),
              self.var_mob.get(),
              self.var_add.get(),
              
            ))
            con.commit()
            messagebox.showinfo('success','Customer Added Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from customer")
        rows=cur.fetchall()
        self.customerTable.delete(*self.customerTable.get_children())
        for row in rows:
          self.customerTable.insert('',END,values=row)

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
      f=self.customerTable.focus()
      content=(self.customerTable.item(f))
      row=content['values']
      # print(row)
      self.var_cust_id.set(row[0]),
      self.var_name.set(row[1]),
      self.var_mob.set(row[2]),
      self.var_add.set(row[3]),
      
    #==update===
    def update(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_cust_id.get()=="":
          messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
        else:

          cur.execute("Select * from customer where cust_id=?",(self.var_cust_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid customerr ID",parent=self.root)
          else:
            cur.execute("Update customer set name=?,mobile=?,address=?, where cust_id=?",(
             
              self.var_name.get(),
              self.var_mob.get(),
              self.var_add.get(),
            
              self.var_cust_id.get(),
            ))
            con.commit()
            messagebox.showinfo('success','Customer Updated Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
         if self.var_cust_id.get()=="":
          messagebox.showerror("Error","Customer ID Must be required",parent=self.root)
         else:

          cur.execute("Select * from customer where cust_id=?",(self.var_cust_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid customer ID",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
            if op==True:
              cur.execute("delete from customer where cust_id=?",(self.var_cust_id.get(),))
              con.commit()
              messagebox.showinfo("Delete","customer Deleted Successfully",parent=self.root)
              self.clear()

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_cust_id.set("")
        self.var_name.set("")
        self.var_mob.set("")
        
        self.var_add.set("")
        
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
          cur.execute("Select * from customer where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.customerTable.delete(*self.customerTable.get_children())
            for row in rows:
             self.customerTable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found!!!",parent=self.root)
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":

  root=Tk()
  obj=customerclass(root)
  root.mainloop()