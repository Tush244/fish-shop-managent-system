from tkinter import*
from tkinter import font
#from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class f_categoryclass:
  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x500+250+130")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        self.root.config(bg="white")
        self.root.focus_force()


        #====variables==
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #====title===
        lbl_title=Label(self.root,text="Product Category",font=("times new roman",20,"italic"),bg="black",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text="Enter Category Name",font=("times new roman",20,"italic"),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"italic"),bg="lightyellow").place(x=50,y=170,width=300)
        
        btn_add=Button(self.root,text="Add",command=self.add,font=("times new roman",15,"italic"),bg="green",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15,"italic"),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        
        #==== category details===
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=400,height=100)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cat_id","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("cat_id",text="Cat_id")
        self.category_table.heading("name",text="Name")
        
        self.category_table["show"]="headings"
        
        self.category_table.column("cat_id",width=90)
        self.category_table.column("name",width=100)
          
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        #==images==
        self.img1=Image.open("fishmarket.jpg")
        self.img1=self.img1.resize((500,250),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(self.img1)

        self.lbl_img1=Label(self.root,image=self.img1,bd=2,relief=RAISED) 
        self.lbl_img1.place(x=50,y=240)   


        self.img2=Image.open("Fishmarket1.jpg")
        self.img2=self.img2.resize((500,250),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(self.img2)

        self.lbl_img2=Label(self.root,image=self.img2,bd=2,relief=RAISED) 
        self.lbl_img2.place(x=580,y=240) 
        self.show()
        #======functions===
    def add(self):
        con=sqlite3.connect(database=r'TUSHARG244.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
             messagebox.showerror("Error","Category name Must be required",parent=self.root)
            else:
              cur.execute("Select * from f_category where name=?",(self.var_name.get(),))
              row=cur.fetchone()
              if row!=None:
                messagebox.showerror("Error","This f_category  already present, try different",parent=self.root)
              else:
                cur.execute("Insert into f_category(name) values(?)",(
                self.var_name.get(),
                
                ))
                con.commit()
                messagebox.showinfo('Success','f_category Added Successfully',parent=self.root)
                self.show()
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        cur.execute("Select * from f_category")
        rows=cur.fetchall()
        self.category_table.delete(*self.category_table.get_children())
        for row in rows:
          self.category_table.insert('',END,values=row)

      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

   
    def get_data(self,ev):
      f=self.category_table.focus()
      content=(self.category_table.item(f))
      row=content['values']
      # print(row)
      self.var_cat_id.set(row[0]),
      self.var_name.set(row[1]),



    def delete(self):
      con=sqlite3.connect(database=r'TUSHARG244.db')
      cur=con.cursor()
      try:
        if self.var_cat_id.get()=="":
          messagebox.showerror("Error","please select category from the list",parent=self.root)
        else:
          cur.execute("Select * from f_category where cat_id=?",(self.var_cat_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Try again",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete=?",parent=self.root)
          if op==True:
            cur.execute("delete from f_category where cat_id=?",(self.var_cat_id.get(),))
            con.commit()
            messagebox.showinfo("Delete","f_category Deleted Successfully",parent=self.root)
            self.show()
            self.var_cat_id.set("")
            self.var_name.set("")
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
  root=Tk()
  obj=f_categoryclass(root)
  root.mainloop()



