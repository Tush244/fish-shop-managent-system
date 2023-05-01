from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from employee import employeeclass
from supplier import supplierclass
from f_category import f_categoryclass
from f_product import f_productclass
from stock import stockclass 
from customer import customerclass
from bills import billsclass



class FMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("FISH SHOP MANAGEMENT SYSTEM  ||DEVELOPED BY UNKNOWN")
        #self.root.config(bg="white")
        
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\USER\tushar244\2776662 (2).jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1700,height=850)
        #===TITLE===
        title=Label(self.root,text="FISH SHOP MANAGEMENT",font=("italic",40,"italic","bold"),bg="blue",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #==btn logout===
        #btn_logout=Button(self.root,text="Logout",font=("italic",15,"bold"),bg="white",cursor="hand2").place(x=1155,y=10,height=50,width=150)

        #===left menu==
        self.MenuLogo=Image.open("fish-sticker-transparent-background-gold-fish-png.png")
        self.MenuLogo=self.MenuLogo.resize((140,140,),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="black")
        LeftMenu.place(x=0,y=70,width=200,height=700)

        #==btn==
        
        
        lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

          
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("italic",20),bg="green").pack(side=TOP,fill=X)
        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_Customer=Button(LeftMenu,text="Customer",command=self.customer,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_Stock=Button(LeftMenu,text="Stock",command=self.stock,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_f_category=Button(LeftMenu,text="F_Category",command=self.f_category,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_f_product=Button(LeftMenu,text="F_Product",command=self.f_product,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_Supplier=Button(LeftMenu,text="Supplier",command=self.suppleir,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_bill=Button(LeftMenu,text="Bill",command=self.bills,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Logout",command=self.logout,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_logout=Button(LeftMenu,text="Exit",command=self.exit,font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
       # btn_f_product=Button(LeftMenu,text="F_Product",font=("times new roman",21,"italic","bold"),bg="black",fg="white",bd=1,cursor="hand2").pack(side=TOP,fill=X)
      #==footer==
      
      #==footer==
      
        lbl_footer=Label(self.root,text="Fish Shop Management System || Developed by unknown\n for any technical issue Contact:7719903821",font=("times new roman",12,"italic"),bg="blue",fg="white").pack(side=BOTTOM,fill=X)  




       ##############################
    def employee(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=employeeclass(self.new_win)


     #========
    def suppleir(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=supplierclass(self.new_win)    

    def f_category(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=f_categoryclass(self.new_win)  




    def f_product(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=f_productclass(self.new_win)  
   
    def stock(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=stockclass(self.new_win)  

    def customer(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=customerclass(self.new_win)  
    
    
    def bills(self):
         self.new_win=Toplevel(self.root)
         self.new_obj.billsclass(self.new_win) 

    
    
    def logout(self):
          self.root.destroy()

    def exit(self):
         self.root.destroy()


if __name__=="__main__":

  root=Tk()
  obj=FMS(root)
  root.mainloop()