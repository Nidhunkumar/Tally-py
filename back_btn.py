from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x400")
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()

        self.listbx = Listbox(self.frame1, width=30, height=10)
        self.listbx.insert(1, "item1")
        self.listbx.insert(2, "item2")
        self.listbx.insert(3, "item3")
        self.listbx.insert(4, "item4")
        self.listbx.insert(5, "item5")

        self.listbx.pack()
        self.listbx.bind("<<ListboxSelect>>", self.list_itm)

  

    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()
    
    def list_itm(self, event):
        itm=self.listbx.get(self.listbx.curselection())
        self.nextpg(itm)

    
    

      


    
    def nextpg(self, itm):
        for i in self.master.winfo_children():
            i.destroy()
        self.label = ttk.Label(self.master, text="page1")
        self.label.pack()

        self.frame3 = Frame(self.master, width=300, height=300)
        self.frame3.pack()
        self.entry_txt = ttk.Label(self.frame3, text=itm)
        self.entry_txt.pack()

        self.list_i = Listbox(self.frame3, width=30, height=10)
        self.list_i.insert(1, "item1")
        self.list_i.insert(2, "item2")
        self.list_i.insert(3, "item3")
        self.list_i.pack()
        self.list_i.bind("<<ListboxSelect>>", self.list_itms)

    def list_itms(self, event):
      itmll=self.list_i.get(self.list_i.curselection())
      self.nextpg2(itmll)
    
    def nextpg2(self, itmll):
        for i in self.master.winfo_children():
            i.destroy()
        self.label = ttk.Label(self.master, text="page2")
        self.label.pack() 

        self.frame4 = Frame(self.master, width=300, height=300)
        self.frame4.pack()
        self.entry_txt2 = ttk.Label(self.frame4, text=itmll)
        self.entry_txt2.pack()
        # self.back_btn = ttk.Button(self.frame4, text="Go to Back", command=self.nextpg)
        # self.back_btn.pack()
    

        



       
root = Tk()
app(root)
root.mainloop()