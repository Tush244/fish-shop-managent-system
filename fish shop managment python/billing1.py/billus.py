from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x900+0+0")
        self.root.title("Billing software Created By Gayatri, Amol & Umesh.......i.e. G.A.U.")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software For Milk Dairy Shop",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack()

       #========================variables============================
        #=============================Milk product==================
        self.Milk=IntVar()
        self.Dahi=IntVar()
        self.Paneer=IntVar()
        self.Lassi=IntVar()
        self.ShreeKhand=IntVar()
        self.Cheese=IntVar()
        self.AamrKhand=IntVar()
        self.Ghee=IntVar()
        self.Khava=IntVar()
        self.Malai=IntVar()
        self.Butter=IntVar()
        self.Tak=IntVar()

        #========================Cold Drinks==========================


        self.Maza = IntVar()
        self.Fruity = IntVar()
        self.Thumbs_up = IntVar()
        self.Limca = IntVar()
        self.Sprite = IntVar()
        self.Bislery = IntVar()

        #=============================Total Product Price & Tax Variable======================


        self.Milk_Product_Price = StringVar()
        self.Cold_Drinks_Price= StringVar()


        self.Milk_Product_tax = StringVar()
        self.Cold_Drinks_tax = StringVar()

        #===================================Customer======================

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.Bill_Number=StringVar()
        x=random.randint(1000,9999)
        self.Bill_Number.set(str(x))

        self.Search_bill=StringVar()






       #============Customer Details frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name", bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label = Label(F1, text="Phone Number", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphone_text = Entry(F1, width=15,textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_label = Label(F1, text="Bill Number", bg=bg_color, fg="white",font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_text = Entry(F1, width=15,textvariable=self.Search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_button=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #========================Milk Product=====================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Milk Product", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=700,height=380)

        Milk_label=Label(F2,text="Milk(ml)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        Milk_text=Entry(F2,width=10,textvariable=self.Milk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=0,column=1,padx=10,pady=10)

        Dahi_label=Label(F2,text="Dahi(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        Dahi_text=Entry(F2,width=10,textvariable=self.Dahi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=1,column=1,padx=10,pady=10)

        Paneer_label=Label(F2,text="Paneer(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        Paneer_text=Entry(F2,width=10,textvariable=self.Paneer,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=2,column=1,padx=10,pady=10)

        Lassi_label=Label(F2,text="Lassi(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="W")
        Lassi_text=Entry(F2,width=10,textvariable=self.Lassi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=3,column=1,padx=10,pady=10)

        ShreeKhand_label=Label(F2,text="ShreeKhand(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="W")
        ShreeKhand_text=Entry(F2,width=10,textvariable=self.ShreeKhand,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=4,column=1,padx=10,pady=10)

        Cheese=Label(F2,text="Cheese(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="W")
        Cheese_text=Entry(F2,width=10,textvariable=self.Cheese,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=5,column=1,padx=10,pady=10)

        AamrKhand_label=Label(F2,text="AamrKhand(gm)",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=10,pady=10,sticky="W")
        AamrKhand_text=Entry(F2,width=10,textvariable=self.AamrKhand,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=0,column=3,padx=10,pady=10)

        Ghee_label = Label(F2, text="Ghee(gm)", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=2, padx=10, pady=10, sticky="W")
        Ghee_text = Entry(F2, width=10,textvariable=self.Ghee, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        Khava_label = Label(F2, text="Khava(gm)", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=2, padx=10, pady=10, sticky="W")
        Khava_text = Entry(F2, width=10,textvariable=self.Khava, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)

        Malai = Label(F2, text="Malai(gm)", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=2, padx=10, pady=10, sticky="W")
        Malai_text = Entry(F2, width=10,textvariable=self.Malai, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)

        Butter_label = Label(F2, text="Butter(gm)", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=2, padx=10, pady=10, sticky="W")
        Butter_text = Entry(F2, width=10,textvariable=self.Butter, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=3,padx=10,pady=10)

        Tak_label = Label(F2, text="Tak(gm)", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=2, padx=10, pady=10, sticky="W")
        Tak_text = Entry(F2, width=10,textvariable=self.Tak, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=3,padx=10,pady=10)


       #========================Cold Drinks=================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=710, y=180, width=350, height=380)



        Maza_label=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=6,padx=10,pady=10,sticky="W")
        Maza_text=Entry(F4,width=10,textvariable=self.Maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=0,column=7,padx=10,pady=10)

        Fruity_label=Label(F4,text="Fruity",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=6,padx=10,pady=10,sticky="W")
        Fruity_text=Entry(F4,width=10,textvariable=self.Fruity,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=1,column=7,padx=10,pady=10)

        Thumbs_up_label=Label(F4,text="Thumbs up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=6,padx=10,pady=10,sticky="W")
        Paneer_text=Entry(F4,width=10,textvariable=self.Thumbs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=2,column=7,padx=10,pady=10)

        Limca_label=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=6,padx=10,pady=10,sticky="W")
        Limka_text=Entry(F4,width=10,textvariable=self.Limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=3,column=7,padx=10,pady=10)

        Sprite_label=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=6,padx=10,pady=10,sticky="W")
        Sprite_text=Entry(F4,width=10,textvariable=self.Sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=4,column=7,padx=10,pady=10)

        Bislery_label=Label(F4,text="Bislery",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=6,padx=10,pady=10,sticky="W")
        Bislery_text=Entry(F4,width=10,textvariable=self.Bislery,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN) .grid(row=5,column=7,padx=10,pady=10)


        #============Billing area==========

        F5 =Frame(self.root, bd=10, relief=GROOVE, )
        F5.place(x=1070, y=180, width=427, height=380)

        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=================Button Frame======================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_label=Label(F6,text="Total Milk Product Price",bg=bg_color,fg="white",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text=Entry(F6,width=18,font="arial 10 bold",textvariable=self.Milk_Product_Price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        m2_label = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_text = Entry(F6, width=18, font="arial 10 bold",textvariable=self.Cold_Drinks_Price, bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        T1_label = Label(F6, text="Milk Product Tax", bg=bg_color, fg="white",font=("times new roman", 16, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        T1_text = Entry(F6, width=18, font="arial 10 bold",textvariable=self.Milk_Product_tax, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        T2_label = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white",font=("times new roman", 16, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        T2_text = Entry(F6, width=18, font="arial 10 bold",textvariable=self.Cold_Drinks_tax, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        Button_F=Frame(F6,bd=7,relief=GROOVE)
        Button_F.place(x=790,width=680,height=100)


        total_button=Button(Button_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GenrateBill_button = Button(Button_F, text="Genrate Bill",command=self.bill_area, bg="cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_button = Button(Button_F,text="Clear",command=self.clear_data, bg="cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_button = Button(Button_F,text="Exit",command=self.Exit_app, bg="cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.M_M_P=self.Milk.get()*0.035
        self.M_D_P=self.Dahi.get()*0.040
        self.M_P_P=self.Paneer.get()*0.05
        self.M_L_P=self.Lassi.get()*0.03
        self.M_S_P=self.ShreeKhand.get()*0.02
        self.M_C_P=self.Cheese.get()*0.05
        self.M_A_P=self.AamrKhand.get()*0.02
        self.M_G_P=self.Ghee.get()*0.05
        self.M_K_P=self.Khava.get()*0.05
        self.M_ML_P=self.Malai.get()*0.03
        self.M_B_P=self.Butter.get()*0.04
        self.M_T_P=self.Tak.get()*0.04
        self.total_Milk_Product_Price=float(
            self.M_M_P+
            self.M_D_P +
            self.M_P_P +
            self.M_L_P+
            self.M_S_P +
            self.M_C_P +
            self.M_A_P +
            self.M_G_P +
            self.M_K_P +
            self.M_ML_P +
            self.M_B_P +
            self.M_T_P
            )
        self.Milk_Product_Price.set("Rs. "+str(self.total_Milk_Product_Price))
        self.M_tax=round((self.total_Milk_Product_Price*0.05),2)
        self.Milk_Product_tax.set("Rs. "+str(self.M_tax))
        #round((number),how many decimal point you want)

        self.C_M_P=self.Maza.get()*50
        self.C_F_P=self.Fruity.get()*30
        self.C_T_P=self.Thumbs_up.get()*20
        self.C_L_P=self.Limca.get()*50
        self.C_S_P=self.Sprite.get()*20
        self.C_B_P=self.Bislery.get()*20
        self.total_Cold_Drinks_Price=float(
            self.C_M_P+
            self.C_F_P+
            self.C_T_P+
            self.C_L_P +
            self.C_S_P +
            self.C_B_P
            )
        self.Cold_Drinks_Price.set("Rs. "+str(self.total_Cold_Drinks_Price))
        self.C_tax=round((self.total_Cold_Drinks_Price*0.05),2)
        self.Cold_Drinks_tax.set("Rs. "+str(self.C_tax))

        self.Total_bill=float(self.total_Milk_Product_Price +
                             self.total_Cold_Drinks_Price+
                             self.M_tax+
                             self.C_tax)


    def welcome_bill(self):
            self.textarea.delete('1.0',END)
            self.textarea.insert(END,"\t Welcome to Dairy Powar")
            self.textarea.insert(END,f"\n Bill Number :{self.Bill_Number.get()}")
            self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
            self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
            self.textarea.insert(END,f"\n ==============Milk Product====================")
            self.textarea.insert(END,f"\n Product Name\t\tQTY\t\tPrice")
            self.textarea.insert(END,f"\n ==============================================")




    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome_bill()
            #========condition for milk product
            if self.Milk.get()!=0:
                self.textarea.insert(END, f"\n Milk(ml)\t\t{self.Milk.get()}\t\t{self.M_M_P}")
            if self.Dahi.get()!=0:
                self.textarea.insert(END, f"\n Dahi(gm)\t\t{self.Dahi.get()}\t\t{self.M_D_P}")
            if self.Paneer.get()!=0:
                self.textarea.insert(END, f"\n Paneer(gm)\t\t{self.Paneer.get()}\t\t{self.M_P_P}")
            if self.Lassi.get()!=0:
                self.textarea.insert(END, f"\n Lassi(gm)\t\t{self.Lassi.get()}\t\t{self.M_L_P}")
            if self.ShreeKhand.get()!=0:
                self.textarea.insert(END, f"\n ShreeKhand(gm)\t\t{self.ShreeKhand.get()}\t\t{self.M_S_P}")
            if self.Cheese.get()!=0:
                self.textarea.insert(END, f"\n Cheese(gm)\t\t{self.Cheese.get()}\t\t{self.M_C_P}")
            if self.AamrKhand.get()!=0:
                self.textarea.insert(END, f"\n AamrKhand(gm)\t\t{self.AamrKhand.get()}\t\t{self.M_A_P}")
            if self.Ghee.get()!=0:
                self.textarea.insert(END, f"\n Ghee(gm)\t\t{self.Ghee.get()}\t\t{self.M_G_P}")
            if self.Khava.get()!=0:
                self.textarea.insert(END, f"\n Khava(gm)\t\t{self.Khava.get()}\t\t{self.M_K_P}")
            if self.Malai.get()!=0:
                self.textarea.insert(END, f"\n Malai(gm)\t\t{self.Malai.get()}\t\t{self.M_ML_P}")
            if self.Butter.get()!=0:
                self.textarea.insert(END, f"\n Butter(gm)\t\t{self.Butter.get()}\t\t{self.M_B_P}")
            if self.Tak.get()!=0:
                self.textarea.insert(END, f"\n Tak(gm)\t\t{self.Tak.get()}\t\t{self.M_T_P}")



            self.textarea.insert(END, f"\n\n ")
            self.textarea.insert(END, f"\n =================Cold Drinks==================")
            self.textarea.insert(END, f"\n Product Name\t\tQTY\t\tPrice")
            self.textarea.insert(END, f"\n ==============================================")

            if self.Maza.get() != 0:
                self.textarea.insert(END, f"\n Maza\t\t{self.Maza.get()}\t\t{self.C_M_P}")
            if self.Fruity.get() != 0:
                self.textarea.insert(END, f"\n Fruity\t\t{self.Fruity.get()}\t\t{self.C_F_P}")
            if self.Thumbs_up.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t{self.Thumbs_up.get()}\t\t{self.C_T_P}")
            if self.Limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t{self.Limca.get()}\t\t{self.C_L_P}")
            if self.Sprite.get() != 0:
                self.textarea.insert(END, f"\n ShreeKhand\t\t{self.Sprite.get()}\t\t{self.C_S_P}")
            if self.Bislery.get() != 0:
                self.textarea.insert(END, f"\n Bislery\t\t{self.Bislery.get()}\t\t{self.C_B_P}")


            self.textarea.insert(END, f"\n\n ")

            self.textarea.insert(END, f"\n ----------------------------------------------")
            if self.Milk_Product_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Milk Product Tax\t\t\t\t{self.Milk_Product_tax.get()}")
            if self.Cold_Drinks_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cold Drinks Tax\t\t\t\t{self.Cold_Drinks_tax.get()}")

            self.textarea.insert(END, f"\n Total Bill : \t\t\t\t Rs. {self.Total_bill}")
            self.textarea.insert(END, f"\n ----------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
        if op>0:
           self.bill_data=self.textarea.get('1.0',END)
           f1=open("Bills/"+str(self.Bill_Number.get())+".txt","w")
           f1.write(self.bill_data)
           f1.close()
           messagebox.showinfo("Saved",f"Bill no. : {self.Bill_Number.get} Saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"

        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.Search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:

         self.Milk.set(0)
        self.Dahi.set(0)
        self.Paneer.set(0)
        self.Lassi.set(0)
        self.ShreeKhand.set(0)
        self.Cheese.set(0)
        self.AamrKhand.set(0)
        self.Ghee.set(0)
        self.Khava.set(0)
        self.Malai.set(0)
        self.Butter.set(0)
        self.Tak.set(0)

        # ========================Cold Drinks==========================

        self.Maza.set(0)
        self.Fruity.set(0)
        self.Thumbs_up.set(0)
        self.Limca.set(0)
        self.Sprite.set(0)
        self.Bislery.set(0)

        # =============================Total Product Price & Tax Variable======================

        self.Milk_Product_Price.set("")
        self.Cold_Drinks_Price.set("")

        self.Milk_Product_tax.set("")
        self.Cold_Drinks_tax.set("")

        # ===================================Customer======================

        self.c_name.set("")
        self.c_phon.set("")
        self.Bill_Number.set("")
        x = random.randint(1000, 9999)
        self.Bill_Number.set(str(x))

        self.Search_bill.set("")
        self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()
