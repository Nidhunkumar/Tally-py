from tkinter import *
from tkinter import ttk

import os

root=Tk()
root.title("Window")
root.geometry("1200x600")
root.resizable(0,0)
root.configure(background="white")

f0=Frame(root,height=100,width=1200,bg="white",relief=RIDGE,bd=1)
f0.place(x=500,y=25,width=200,height=100)

# l1=Label(root,text="Select stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white")
# l1.pack(fill=X)

# l2=Label(root,text="c-name",font=("times new roman",13,"bold"),bg="blue",fg="white")
# l2.pack(fill=X)


f0_l0=Label(f0,text="Name of group",font=("times new roman",15,"bold"),bg="blue",fg="white")
f0_l0.pack(fill=X,side=LEFT) 

cmb=ttk.Combobox(f0,values=("Select","Group 1","Group 2","Group 3","Group 4","Group 5",),font=("times new roman",15,"bold"),state="readonly")
cmb.pack(fill=X,side=LEFT)

f1=Frame(root,height=100,width=1200,bg="white",relief=RIDGE,bd=5)
f1.place(x=400,y=150,width=350,height=400)

f1_l0=Label(f1,text="Movement Analysis",font=("times new roman",25,"bold"),bg="blue",fg="white")






root.mainloop()


