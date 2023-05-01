from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class employeeclass:
    def __init__(self,root):
      
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()
        # all variable

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()  
       
       
        self.var_emp_id=StringVar() 
        self.var_gender=StringVar()  
        self.var_contact=StringVar() 
        self.var_name=StringVar()
        self.var_dob=StringVar() 
        self.var_doj=StringVar() 
        self.var_email=StringVar()
        self.var_pass=StringVar() 
        self.var_utype=StringVar()  
        self.var_address=StringVar()
        self.var_salery=StringVar()  



        ################search frame##########
        searchFrame=LabelFrame(self.root,text="Search Employee",font=("times new roman",15,"italic","bold"),bd=2,bg="white")
        searchFrame.place(x=300,y=20,width=600,height=70)
       



       ###############options#################
      
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','Name','contact',"Email"),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_search.place(x=12,y=10,width=180)
        cmb_search.current(0)



        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"italic"),bg="lightyellow").place(x=220,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=440,y=10,width=150,height=26)



        #=====title======
        title=Label(self.root,text="Employee Details",font=("times new roman",20,"italic","bold"),bg="black",fg="white").place(x=60,y=100,width=1000)



        #===content====
        # row1

        lbl_empid=Label(self.root,text="Emp ID",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=150)
      
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=150)
      
      

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=150,y=150,width=200)
       # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=150,width=200)
       
        
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female','other'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=900,y=150,width=200)
       # ==row 2==
        lbl_Name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=190)
        lbl_dob=Label(self.root,text="DOB",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=190)
        lbl_doj=Label(self.root,text="DOJ",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=190)
      
      

        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=150,y=190,width=200)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=190,width=200)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=900,y=190,width=200)
      
       #==row3==
        lbl_email=Label(self.root,text="Email",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=230)
        lbl_pass=Label(self.root,text="Password",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=230)
             
      

        txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=150,y=230,width=200)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=230,width=200)
       # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=930,y=230,width=200)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=('Admin','Employee'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_utype.place(x=930,y=230,width=200)
        cmb_utype.current(0)

       #===row4==
        lbl_address=Label(self.root,text="Address",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=270)
        lbl_salery=Label(self.root,text="Salery",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=270)
        self.txt_address=Entry(self.root,textvariable=self.var_address,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=150,y=270,width=200)
        self.txt_salery=Entry(self.root,textvariable=self.var_salery,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=270,width=200)
      
        #==buttons===
        btn_Add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=500,y=305,width=110,height=30)
        btn_Upadate=Button(self.root,text="Upadate",command=self.update,font=("times new roman",15,"italic"),bg="pink",cursor="hand2").place(x=650,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="Red",cursor="hand2").place(x=800,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"italic"),bg="Blue",cursor="hand2").place(x=950,y=305,width=110,height=30)
       
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("emp_id","name","email","gender","contact","DOB","DOJ","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("emp_id",text="Emp_id")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contactc")
        self.EmployeeTable.heading("DOB",text="DOB")
        self.EmployeeTable.heading("DOJ",text="DOJ")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="Utype")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("emp_id",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("DOB",width=100)
        self.EmployeeTable.column("DOJ",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================================================================================
    def add(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_emp_id.get()=="":
          messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
        else:

          cur.execute("Select * from employee where emp_id=?",(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error","This  Employee ID already assigned, try different",parent=self.root)
          else:
            cur.execute("Insert into employee(emp_id,name,email,gender,contact,DOB,DOJ,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
              self.var_emp_id.get(),
              self.var_name.get(),
              self.var_email.get(),
              self.var_gender.get(),
              self.var_contact.get(),
              self.var_dob.get(),
              self.var_doj.get(),
              self.var_pass.get(),
              self.var_utype.get(),
              self.var_address.get(),
              self.var_salery.get(),
             
            ))
            con.commit()
            messagebox.showinfo('success','Employee Added Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from employee")
        rows=cur.fetchall()
        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
        for row in rows:
          self.EmployeeTable.insert('',END,values=row)

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
      f=self.EmployeeTable.focus()
      content=(self.EmployeeTable.item(f))
      row=content['values']
      # print(row)
      self.var_emp_id.set(row[0]),
      self.var_name.set(row[1]),
      self.var_email.set(row[2]),
      self.var_gender.set(row[3]),
      self.var_contact.set(row[4]),
      self.var_dob.set(row[5]),
      self.var_doj.set(row[6]),
      self.var_pass.set(row[7]),
      self.var_utype.set(row[8]),
      self.var_address.set(row[9]),
      self.var_salery.set(row[10]),
      
    #==update===
    def update(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_emp_id.get()=="":
          messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
        else:

          cur.execute("Select * from employee where emp_id=?",(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
          else:
            cur.execute("Update employee set name=?,email=?,gender=?,contact=?,DOB=?,DOJ=?,pass=?,utype=?,address=?,salary=? where emp_id=?",(
             
              self.var_name.get(),
              self.var_email.get(),
              self.var_gender.get(),
              self.var_contact.get(),
              self.var_dob.get(),
              self.var_doj.get(),
              self.var_pass.get(),
              self.var_utype.get(),
              self.var_address.get(),
              self.var_salery.get(),
              self.var_emp_id.get(),
            ))
            con.commit()
            messagebox.showinfo('success','Employee Updated Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
         if self.var_emp_id.get()=="":
          messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
         else:

          cur.execute("Select * from employee where emp_id=?",(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
            if op==True:
              cur.execute("delete from employee where emp_id=?",(self.var_emp_id.get(),))
              con.commit()
              messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
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
          cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
             self.EmployeeTable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found!!!",parent=self.root)
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":

  root=Tk()
  obj=employeeclass(root)
  root.mainloop()