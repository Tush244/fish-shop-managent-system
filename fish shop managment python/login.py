from msvcrt import LK_NBLCK
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\USER\tushar244\GettyImages-931270318-43ab672111.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,width=1550,height=800) 

if __name__ =="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
