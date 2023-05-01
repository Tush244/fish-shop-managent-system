from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Fish Billing")




if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop

