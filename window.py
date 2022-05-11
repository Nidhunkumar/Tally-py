from tkinter import *
import os
from tkinter import ttk


root=Tk()
root.title("Window")
root.geometry("1520x720+0+0")
root.resizable(0,0)
root.configure(background="white")


l1=Label(root,text="Select stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
l1.grid(row=0,column=0,ipadx=100,sticky=W)

l2=Label(root,text="c-name",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
l2.grid(row=0,column=1,ipadx=400,sticky=W)
bt1=Button(root,text="print",font=("times new roman",11,"bold"),bg="blue",fg="white",command=root.destroy,relief=GROOVE,bd=2)
bt1.grid(row=0,column=2,ipadx=100,sticky=W)



f0=Frame(root,height=650,width=180,bg="white",relief=RAISED,bd=5)

options_list=["Period","Stock Category Analysis","Stock Item Analysis"]


cmb=ttk.Combobox(f0 ,values=options_list,font=("times new roman",10,"bold"))
cmb.pack(fill=X,pady=2,padx=2)
cmb.current(0)

f0.place(x=1322,y=35,width=195,height=650)


f1=Frame(root,height=650,width=1200,bg="white",relief=RAISED,bd=5)
f11=Frame(f1,bg="white",relief=FLAT,bd=5)
f11.grid(row=1,column=0,columnspan=3,ipadx=200)
l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="blue",fg="white",borderwidth=5,relief=GROOVE,width=20,height=2)
l1f1.pack(fill=X,pady=2,padx=2)
l2f1=Label(f11,text="Quantity",font=("times new roman",12,"bold"),bg="blue",fg="white",borderwidth=5,relief=GROOVE,width=20,height=2)
l2f1.pack(fill=X,pady=2,padx=2)
l3f1=Label(f11,text="Rate",font=("times new roman",12,"bold"),bg="blue",fg="white",borderwidth=5,relief=GROOVE,width=20,height=2)
l3f1.pack(fill=X,pady=2,padx=2)


f1.place(x=10,y=35,width=1300,height=650)






root.mainloop()


