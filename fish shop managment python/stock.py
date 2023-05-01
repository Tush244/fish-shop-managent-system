from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class stockclass:
    def __init__(self,root):
      
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()
        # all variable

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()  
       
       
        self.var_f_cat=StringVar() 
        self.var_f_name=StringVar()  
        self.var_f_weight=StringVar() 
        self.var_st_date=StringVar()
        self.var_st_price=StringVar()




        ################search frame##########
        searchFrame=LabelFrame(self.root,text="Search stock",font=("times new roman",15,"italic","bold"),bd=2,bg="white")
        searchFrame.place(x=300,y=20,width=600,height=70)
       



       ###############options#################
      
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','f_cat','f_Name','st_date'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        cmb_search.place(x=12,y=10,width=180)
        cmb_search.current(0)



        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("times new roman",15,"italic"),bg="lightyellow").place(x=220,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=440,y=10,width=150,height=26)



        #=====title======
        title=Label(self.root,text="Stock Details",font=("times new roman",20,"italic","bold"),bg="black",fg="white").place(x=60,y=100,width=1000)



        #===content====
        # row1

        lbl_f_cat=Label(self.root,text="Category",font=("times new roman",15,"italic","bold"),bg="white").place(x=10,y=150)
        lbl_name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=250,y=150)
      
        lbl_weight=Label(self.root,text="weight",font=("times new roman",15,"italic","bold"),bg="white").place(x=480,y=150)
        lbl_date=Label(self.root,text="Date",font=("times new roman",15,"italic","bold"),bg="white").place(x=710,y=150)
        lbl_price=Label(self.root,text="price",font=("times new roman",15,"italic","bold"),bg="white").place(x=940,y=150)
        

        txt_category=Entry(self.root,textvariable=self.var_f_cat,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=95,y=150,width=150)
       # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=150,width=200       
        
        ##cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female','other'),state='readonly',justify=CENTER,font=('times new roman',15,'italic'))
        ##cmb_gender.place(x=500,y=150,width=180)
        ##cmb_gender.current(0)
        
        
        ##txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=900,y=150,width=200)
       # ==row 2==
       ## lbl_Name=Label(self.root,text="Name",font=("times new roman",15,"italic","bold"),bg="white").place(x=60,y=190)
       ## lbl_dob=Label(self.root,text="DOB",font=("times new roman",15,"italic","bold"),bg="white").place(x=410,y=190)
        ##lbl_doj=Label(self.root,text="DOJ",font=("times new roman",15,"italic","bold"),bg="white").place(x=820,y=190)
      
      

        txt_name=Entry(self.root,textvariable=self.var_f_name,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=320,y=150,width=150)
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
        self.txt_weight=Entry(self.root,textvariable=self.var_f_weight,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=550,y=150,width=150)
        ##self.txt_salery=Entry(self.root,textvariable=self.var_salery,font=("times new roman",15,"italic","bold"),bg="white").place(x=500,y=270,width=200)
        self.txt_date=Entry(self.root,textvariable=self.var_st_date,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=760,y=150,width=150)
        self.txt_price=Entry(self.root,textvariable=self.var_st_price,font=("times new roman",15,"italic","bold"),bg="lightyellow").place(x=1000,y=150,width=150)
        
       
        #==buttons===
        btn_Add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="yellow",cursor="hand2").place(x=500,y=305,width=110,height=30)
        btn_Upadate=Button(self.root,text="Upadate",command=self.update,font=("times new roman",15,"italic"),bg="pink",cursor="hand2").place(x=650,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="Red",cursor="hand2").place(x=800,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"italic"),bg="Blue",cursor="hand2").place(x=950,y=305,width=110,height=30)
       
        stock_frame=Frame(self.root,bd=3,relief=RIDGE)
        stock_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(stock_frame,orient=VERTICAL)
        scrollx=Scrollbar(stock_frame,orient=HORIZONTAL)

        self.stockTable=ttk.Treeview(stock_frame,columns=("f_cat","name","weight","date",'price'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.stockTable.xview)
        scrolly.config(command=self.stockTable.yview)
        self.stockTable.heading("f_cat",text="f_cat")
        self.stockTable.heading("name",text="Name")
        self.stockTable.heading("weight",text="f_weight")
        self.stockTable.heading("date",text="date")
        self.stockTable.heading("price",text="price")
        self.stockTable["show"]="headings"
        
        self.stockTable.column("f_cat",width=90)
        self.stockTable.column("name",width=100)
        self.stockTable.column("weight",width=100)
        self.stockTable.column("date",width=100)
        self.stockTable.column("price",width=100)
        
        self.stockTable.pack(fill=BOTH,expand=1)
        self.stockTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================================================================================
    def add(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_f_cat.get()=="":
          messagebox.showerror("Error","f_category Must be required",parent=self.root)
        else:

          cur.execute("Select * from stock where f_cat=?",(self.var_f_cat.get(),))
          row=cur.fetchone()
          if row==():
              messagebox.showerror("Error","This ID already assigned, try different",parent=self.root)
          else:
            cur.execute("Insert into stock(f_cat,f_name,f_weight,st_date,st_price) values(?,?,?,?,?)",(
              self.var_f_cat.get(),
              self.var_f_name.get(),
              self.var_f_weight.get(),
              self.var_st_date.get(),
              self.var_st_price.get(),
            ))
            con.commit()
            messagebox.showinfo('success','stock Added Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from stock")
        rows=cur.fetchall()
        self.stockTable.delete(*self.stockTable.get_children())
        for row in rows:
          self.stockTable.insert('',END,values=row)

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
      f=self.stockTable.focus()
      content=(self.stockTable.item(f))
      row=content['values']
      # print(row)
      self.var_f_cat.set(row[0]),
      self.var_f_name.set(row[1]),
      self.var_f_weight.set(row[2]),
      self.var_st_date.set(row[3]),
      self.var_st_price.set(row[4]),
    #==update===
    def update(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_f_cat.get()=="":
          messagebox.showerror("Error","Category Must be required",parent=self.root)
        else:

          cur.execute("Select * from stock where f_cat=?",(self.var_f_cat.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid category",parent=self.root)
          else:
            cur.execute("Update stock set f_name=?,f_weight=?,st_date=?,st_price=?, where f_cat=?",(
             
              self.var_f_name.get(),
              self.var_f_weight.get(),
              self.var_st_date.get(),
              self.var_st_price.get(),
              self.var_f_cat.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Stock Updated Successfully',parent=self.root)
            self.show()
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
         if self.var_f_cat.get()=="":
          messagebox.showerror("Error","Category Must be required",parent=self.root)
         else:

          cur.execute("Select * from stock where f_cat=?",(self.var_f_cat.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid category",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
            if op==True:
              cur.execute("delete from stock where f_cat=?",(self.var_f_cat.get(),))
              con.commit()
              messagebox.showinfo("Delete","stock Deleted Successfully",parent=self.root)
              self.clear()

      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_f_cat.set("")
        self.var_f_name.set("")
        self.var_f_weight.set("")
        self.var_st_date.set(" ")
        self.var_st_price.set("")
        
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
          cur.execute("Select * from stock where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.stockTable.delete(*self.stockTable.get_children())
            for row in rows:
             self.stockTable.insert('',END,values=row)
          else:
            messagebox.showerror("Error","No record found!!!",parent=self.root)
      except Exception as ex:

       messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":

  root=Tk()
  obj=stockclass(root)
  root.mainloop()