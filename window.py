from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk

hfont="-family {Segoe UI} -size 12 -weight bold "


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          
sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=account).place(x=20,y=10)
sbmibtn=Button(screen,text='Y:Data',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=180,y=10)
sbmibtn=Button(screen,text='Z:Exchange',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=340,y=10)
sbmibtn=Button(screen,text='G:Go To',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=600,y=10)
sbmibtn=Button(screen,text='O:Import',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
sbmibtn=Button(screen,text='E;Export',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
sbmibtn=Button(screen,text='M:E-mail',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
sbmibtn=Button(screen,text='F1:Help',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)
#main-canvas
global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850)
Label5 = Label(Canvas1,text="mov",borderwidth="0", width=5, background="#3385ff",
                                    foreground="#00254a",
                                    font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


#entry_box
def cavas4():
    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.330, rely=0.0300, relheight=0.100, relwidth=0.350)
    Label6 = Label(Canvas4,text='Select Company',borderwidth="0", width=12, background="white",
                                        foreground="#00254a",
                                        font="-family {Segoe UI} -size 12 -weight bold ")
    Label6.place(relx=0.35, rely=0.20, relheight=0.30, relwidth=0.300)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.35, rely=0.50, relheight=0.30, relwidth=0.300)

#center-canvas
global Canvas2
Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas2.place(relx=0.11, rely=0.1, relheight=0.800, relwidth=0.800)


#side-canvas
global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
global f3
f3=Frame(Canvas2,bg="white",relief=RIDGE,bd=1)
f3.place(x=410,y=10 ,anchor="center")

global sgaf1
sgaf1=Frame(Canvas2,bg="white",relief=RIDGE,bd=5)
sgaf1.place(x=330,y=110,anchor="center")

def Stock_group_analysis():

        f1.destroy()
        f0_l0=Label(f3,text="Name of group",font=("times new roman",15,"bold"),bg="blue",fg="white")
        f0_l0.pack(fill=X,pady=2) 
        options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
        value_inside = StringVar(Canvas2)
        value_inside.set("Select an Option")
        cmb=ttk.Combobox(f3,values=options_list,font=("times new roman",10,"bold"))
        cmb.pack(fill=X,pady=2,padx=2)

        

        f1_l0=Label(sgaf1,text="List of Stock groups",font=("times new roman",12,"bold"),bg="blue",fg="white")
        f1_l0.pack(fill=X,pady=2,padx=2)
        bt0=Button(sgaf1,text="group1",font=("times new roman",12,"bold"),bg="white",fg="red",command=selected_groups)
        bt0.pack(fill=X,pady=2,padx=2)
        bt1=Button(sgaf1,text="  group2",font=("times new roman",12,"bold"),bg="white",fg="red")
        bt1.pack(fill=X,pady=2,padx=2)
        bt2=Button(sgaf1,text="group3",font=("times new roman",12,"bold"),bg="white",fg="red")
        bt2.pack(fill=X,pady=2,padx=2)
        bt3=Button(sgaf1,text="group4",font=("times new roman",12,"bold"),bg="white",fg="red")
        bt3.pack(fill=X,pady=2,padx=2)



def selected_groups():
        f1.destroy()
        f3.destroy()
        sgaf1.destroy()
        l1=Label(Canvas1,text="Stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
        l1.grid(row=0,column=0,ipadx=35,)

        options_list=["Period","Stock Category Analysis","Stock Item Analysis"]
        cm=ttk.Combobox(f0 ,values=options_list,font=("times new roman",10,"bold"))
        cm.pack(fill=X,pady=2,padx=2)
        cm.current(0)
        selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_groups_frame.place(x=10,y=35,width=1300,height=650)

        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=3,ipadx=200)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="blue",fg="white",borderwidth=5,relief=GROOVE,width=20,height=6)
        l1f1.pack(fill=X,pady=2,padx=2)
        f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=610,y=0,width=680,height=80)
        l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=305,y=10,anchor="center")
        l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=305,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=305,y=50,anchor="center")

        f13=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f13.place(x=0,y=145,width=607,height=450)
        f13bt1=Button(f13,text="PRODUCT-1",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt1.place(x=0,y=0,anchor="nw")
        f13bt2=Button(f13,text="PRODUCT-2",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt2.place(x=0,y=30,anchor="nw")
        f13bt3=Button(f13,text="PRODUCT-3",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt3.place(x=0,y=60,anchor="nw")
        f13bt4=Button(f13,text="PRODUCT-4",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt4.place(x=0,y=90,anchor="nw")

        f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=610,y=83,width=340,height=58)
        l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=0,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=80,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=180,y=30,anchor="nw")



        f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=950,y=83,width=340,height=58)
        l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=0,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=80,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=180,y=30,anchor="nw")

        f16=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f16.place(x=610,y=145,width=340,height=450)
        l3f6=Label(f16,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f6.place(x=0,y=0,anchor="nw")
        l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f7.place(x=80,y=0,anchor="nw")
        l3f8=Label(f16,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f8.place(x=180,y=0,anchor="nw")
        

        f17=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f17.place(x=950,y=145,width=340,height=450)
        l4f6=Label(f17,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f6.place(x=0,y=0,anchor="nw")
        l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f7.place(x=80,y=0,anchor="nw")
        l4f8=Label(f17,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f8.place(x=180,y=0,anchor="nw")


       
        f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=598,width=607,height=48)
        l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=0,y=0,anchor="nw")

        f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f19.place(x=610,y=598,width=340,height=48)
        l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f20.place(x=950,y=598,width=340,height=48)
        l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")


            

global f1
f1=Frame(Canvas2,bg="white",relief=RAISED,bd=1)
f1.place(x=380,y=0)
def movement_analysis():
    f0.destroy()
    l5=Label(f1,text="Movement Analysis",font=hfont,bg="blue",fg="white",)
    l5.pack(fill="x")
    bt1=Button(f1,text="Stock Group Analysis",font=hfont,bg="white",fg="black",command=Stock_group_analysis)
    bt1.pack(fill="x",padx=10,pady=10)
    bt2=Button(f1,text="Stock Category Analysis",font=hfont,bg="white",fg="black",command=screen.destroy)
    bt2.pack(fill="x",padx=10,pady=10)
    bt3=Button(f1,text="Stock Item Analysis",font=hfont,bg="white",fg="black",command=screen.destroy)
    bt3.pack(fill="x",padx=10,pady=10)
    bt4=Button(f1,text="Group Analysis",font=hfont,bg="white",fg="black",command=screen.destroy)
    bt4.pack(fill="x",padx=10,pady=10)
    bt5=Button(f1,text="Exit",font=hfont,bg="white",fg="black",command=screen.destroy)
    bt5.pack(fill="x",padx=10,pady=10)

global f0
f0=Frame(Canvas2,bg="white",relief=RAISED,bd=1)
f0.place(x=380,y=0)
l5=Label(f0,text="statement of inv",font=hfont,bg="blue",fg="white",)
l5.pack(fill="x")
bt1=Button(f0,text="Movement Analysis",font=hfont,bg="white",fg="black",command=movement_analysis)
bt1.pack(fill="x",padx=10,pady=10)



























screen.mainloop()