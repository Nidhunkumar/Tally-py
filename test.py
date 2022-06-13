from doctest import master
from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.init_ui()
        
    def init_ui(self):
        self.master.title("Tkinter")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.master.configure(background='#F0F0F0')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.label = ttk.Label(self.master, text="Hello World!")
        self.label.grid(column=0, row=0, sticky=NSEW)
        self.button = ttk.Button(self.master, text="Click Me", command=self.page1)
        self.button.grid(column=0, row=1, sticky=NSEW)
    def page1(self):
        self.label.configure(text="Page 1")
        self.button.configure(text="Page 1")
        self.button.configure(command=self.page2)
        self.button.grid(column=0, row=1, sticky=NSEW)
    def page2(self):
        self.label.configure(text="Page 2")
        self.button.configure(text="Page 2")
        self.button.configure(command=self.page3)
        self.button.grid(column=0, row=1, sticky=NSEW)
    def page3(self):
        self.label.configure(text="Page 3")
        self.button.configure(text="Page 3")
        self.button.configure(command=home)
        self.button.grid(column=0, row=1, sticky=NSEW)




def home():
   
    f1=Frame(master,bg='#F0F0F0',width=400,height=400)
    f1.grid()
    l1=Label(f1,text='Home',bg='#F0F0F0',font=('Arial',20,'bold'))
    l1.pack()
    b1=Button(f1,text='Click Me',command=c.init_ui)
    b1.pack()

    

c=App(Tk())
    
c.master.mainloop()
