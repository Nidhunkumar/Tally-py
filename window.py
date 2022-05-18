from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk
import mysql.connector


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
Canvas1 = tk.Canvas( background="#3385ff",relief=FLAT,bd=0,highlightthickness=0)
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850)
Label5 = Label(Canvas1,text="C-Name",borderwidth="0", background="#3385ff",
                                    foreground="#00254a",
                                    font="-family {Segoe UI} -size 10 -weight bold ")
Label5.pack(anchor=CENTER)
label_1=Label(Canvas1, text="",borderwidth="0", width=20, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
label_1.pack(anchor=W)


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
Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="flat",selectbackground="blue", selectforeground="white")
Canvas2.place(x=0,y=20, relheight=1, relwidth=1)


#side-canvas
global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
global f3
f3=Frame(Canvas2,bg="white",relief=RIDGE,bd=1)
f3.pack()

global sgaf1
sgaf1=Frame(Canvas2,bg="white",relief=RIDGE,bd=1)
sgaf1.pack(pady=10)

def movement_analysis():
    global label_1
    label_1 = Label(Canvas1, text="Gate Way of Tally",borderwidth="0", background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    
    f1.destroy()
    global movement_analysis_frame
    movement_analysis_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    movement_analysis_frame.place(x=0,y=21,width=1308,height=660)
    global f55
    global f66
    f55=Frame(movement_analysis_frame,bg="white",relief=RAISED,bd=1)
    f55.pack(pady=15)
    f66=Frame(movement_analysis_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f66.pack()

    f0.destroy()
    l11=Label(f55,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack(padx=10,pady=10)
    
    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]


    cmb=ttk.Combobox(f55 ,values=options_list,font=("times new roman",10,"bold"))
    cmb.pack(fill=X,pady=10,padx=10)

    itemsforlistbox=['Stock Group Analysis','Stock Category Analysis','Stock Item Analysis','Group Analysis','Exit']

    l5=Label(f66,text="Movement Analysis",font=hfont,bg="blue",fg="black")
    l5.pack(fill=X)

    global lb
    lb=Listbox(f66,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)

   
    lb.bind('<<ListboxSelect>>',CurSelet)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)



def selected_groups():
        f1.destroy()
        f3.destroy()
        sgaf1.destroy()
        Canvas2.destroy()
        global sdbtn
        sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
        sdbtn.pack(fill=X,pady=10,padx=10)
        label_1=Label(Canvas1, text="Stock group analysis",borderwidth="0", width=20, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
        label_1.place(relx=0, rely=0)


        global selected_groups_frame
        selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
        selected_groups_frame.place(x=0,y=21,width=1308,height=660)

        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
        f11.grid(row=1,column=0,columnspan=3,ipadx=200)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
        l1f1.pack(fill=X)
        f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f12.place(x=613,y=0,width=692,height=80)
        l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=305,y=10,anchor="center")
        l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=305,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=305,y=50,anchor="center")

        tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)

        tree0.column("#1", anchor=tk.W,width=610)

        tree0.column("#2", anchor=tk.W,width=110)

        tree0.column("#3",anchor=tk.W,width=110)

        tree0.column("#4", anchor=tk.W,width=120)

        tree0.column("#5", anchor=tk.W,width=110)

        tree0.column("#6", anchor=tk.W,width=110)

        tree0.column("#7", anchor=tk.W,width=132)


        tree0.place(x=1,y=139)

        tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
        tree0.bind("<Double-1>", movement_val)



        f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=614,y=81,width=340,height=58)
        l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=0,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=110,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=225,y=30,anchor="nw")



        f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=955,y=81,width=350,height=58)
        l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=0,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=110,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=225,y=30,anchor="nw")



       
        f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f18.place(x=0,y=598,width=607,height=65)
        l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=1,y=0,anchor="nw")

        f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f19.place(x=610,y=598,width=340,height=65)
        l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f20.place(x=950,y=598,width=355,height=65)
        l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")

def selected_category():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Stock Category Movement Analysis",borderwidth="0", background="#3385ff",
                                foreground="#00254a",   
                                font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)


    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)

    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")

    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)

    tree0.column("#1", anchor=tk.W,width=610)

    tree0.column("#2", anchor=tk.W,width=110)

    tree0.column("#3",anchor=tk.W,width=110)

    tree0.column("#4", anchor=tk.W,width=120)

    tree0.column("#5", anchor=tk.W,width=110)

    tree0.column("#6", anchor=tk.W,width=110)

    tree0.column("#7", anchor=tk.W,width=132)


    tree0.place(x=1,y=139)

    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)



    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")



    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")




    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")

    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")

    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def selected_item():
    movement_values()

def Bank_account_group():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Bank Accounts",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")
def Bank_OCC_group():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Bank OCC A/c ",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def Bank_OD_group():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Bank OD A/c ",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def Branch_Division_group():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Branch/Devision ",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def Cash_in_Hand_group():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Cash-in-Hand ",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def Sundry_Creditors_group():
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Sundry Creditors ",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")

def movement_analysis_back():
    global selected_groups_frame
    sdbtn.destroy()
    movement_analysis()

def Sundry_Debtors_group():
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    f55.destroy()
    f66.destroy()
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text="Sundry Debtors",font=hfont,bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")    
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)
    tree0.column("#1", anchor=tk.W,width=610)
    tree0.column("#2", anchor=tk.W,width=110)
    tree0.column("#3",anchor=tk.W,width=110)
    tree0.column("#4", anchor=tk.W,width=120)
    tree0.column("#5", anchor=tk.W,width=110)
    tree0.column("#6", anchor=tk.W,width=110)
    tree0.column("#7", anchor=tk.W,width=132)
    tree0.place(x=1,y=139)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15","16","17"))
    tree0.bind("<Double-1>", movement_val)
    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=614,y=81,width=340,height=58)
    l1f5=Label(f14,text="Purchases",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=0,y=30,anchor="nw")
    l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=110,y=30,anchor="nw")
    l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=225,y=30,anchor="nw")
    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=955,y=81,width=350,height=58)
    l2f5=Label(f15,text="Sales",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l2f5.place(x=0,y=0,anchor="nw")
    l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f6.place(x=0,y=30,anchor="nw")
    l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f7.place(x=110,y=30,anchor="nw")
    l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l2f8.place(x=225,y=30,anchor="nw")
    f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f18.place(x=0,y=598,width=607,height=65)
    l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l5f6.place(x=1,y=0,anchor="nw")
    f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f19.place(x=610,y=598,width=340,height=65)
    l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")
    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")
def movement_val(e):
    movement_values()

def movement_values():
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    
    label_1=Label(Canvas1, text="Item movement analysis",borderwidth="0", background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global movement_frame
    movement_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    movement_frame.place(x=0,y=21,width=1308,height=680)

    f11=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",width=33,height=7)
    l1f1.pack(fill=X)
    f12=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=705,y=0,width=600,height=83)
    l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")

    f13=Frame(movement_frame,bg="white",relief=RAISED,bd=2)
    f13.place(x=0,y=142,width=1305,height=515)
    f13bt1=Label(f13,text="Movement inward",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt1.place(x=0,y=0,anchor="nw")
    f13bt2=Label(f13,text="Suppliers",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt2.place(x=10,y=30,anchor="nw")

    f14=Frame(movement_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=705,y=83,width=600,height=58)
    l1f5=Label(f14,text="Movement values",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f5.place(x=0,y=0,anchor="nw")
    l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=10,y=30,anchor="nw")
    l1f7=Label(f14,text="Basic Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=160,y=30,anchor="nw")
    l1f8=Label(f14,text="Effective rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=270,y=30,anchor="nw")
    l1f9=Label(f14,text="Values",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
    l1f9.place(x=400,y=30,anchor="nw")

    tree0=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree0.column("#1", anchor=tk.CENTER,width=686)
    
    tree0.column("#2", anchor=tk.CENTER,width=120)

    tree0.column("#3",anchor=tk.CENTER,width=140)

    tree0.column("#4", anchor=tk.CENTER,width=140)

    tree0.column("#5", anchor=tk.CENTER,width=212)

    tree0.place(x=0,y=60)
    tree0.insert("",'end',values=("C-Name","12 BTL","13","14","15"))


    l4f6=Label(f13,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f6.place(x=706,y=150,anchor="nw")
    l4f8=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=860,y=150,anchor="nw")
    l4f7=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f7.place(x=990,y=150,anchor="nw")
    l4f8=Label(f13,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1100,y=150,anchor="nw")

    horizontal =Frame(f13, bg='black', height=1,width=600)
    horizontal.place(x=705, y=175)
    tree0.bind("<Double-1>",supplier)




    f13bt4=Label(f13,text="Movement outwards",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt4.place(x=0,y=170,anchor="nw")
    f13bt5=Label(f13,text="Buyers",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt5.place(x=10,y=200,anchor="nw")
    tree1=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree1.column("#1", anchor=tk.CENTER,width=686)

    
    tree1.column("#2", anchor=tk.CENTER,width=120)
    tree1.column("#3",anchor=tk.CENTER,width=140)

    tree1.column("#4", anchor=tk.CENTER,width=140)

    tree1.column("#5", anchor=tk.CENTER,width=212)

    tree1.place(x=0,y=230)
    tree1.insert("",'end',values=("C-Name","12 BTL","13","14","15"))

    l46=Label(f13,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l46.place(x=706,y=330,anchor="nw")
    l48=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l48.place(x=860,y=330,anchor="nw")
    l47=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l47.place(x=990,y=330,anchor="nw")
    l48=Label(f13,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l48.place(x=1100,y=330,anchor="nw")

    horizontal =Frame(f13, bg='black', height=1,width=600)
    horizontal.place(x=705, y=355)
    tree1.bind("<Double-1>",buyer)


    
# data = [
# 	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
# 	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
	
# ]
def supplier(e):
   item_values()

def buyer(e):
   buyer_dtls()
    

def buyer_dtls():
    label_1=Label(Canvas1, text="Accounting voucher alteration secondry",borderwidth="0", background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    global buyer_dtls_frame
    buyer_dtls_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    buyer_dtls_frame.place(x=0,y=20,width=1308,height=200)
    l1f1=Label(buyer_dtls_frame,text="Sales No:",font=("times new roman",11,"bold"),bg="#00254a",fg="white",borderwidth=0)
    l1f1.place(x=0,y=0)
    l1f2=Label(buyer_dtls_frame,text="1",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f2.place(x=125,y=0)
   
    l1f5=Label(buyer_dtls_frame,text="Party A/c name:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f5.place(x=0,y=30)
    l1f6=Label(buyer_dtls_frame,text="abc",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=125,y=30)
    l1f7=Label(buyer_dtls_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=0,y=60)
    l1f8=Label(buyer_dtls_frame,text="10000cr",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=125,y=60)
    l1f9=Label(buyer_dtls_frame,text="Sales ledger:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f9.place(x=0,y=90)
    l1f10=Label(buyer_dtls_frame,text="sale",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f10.place(x=125,y=90)
    l1f11=Label(buyer_dtls_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f11.place(x=0,y=120)
    l1f12=Label(buyer_dtls_frame,text="10000cr",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f12.place(x=125,y=120)
    
    E1f15=Entry(buyer_dtls_frame,width=20,font=("times new roman",11,"bold"),bg="yellow",fg="black",borderwidth=0)
    E1f15.place(x=1138,y=10)
    E1f15.insert(0,"01-10-21")
    l1f16=Label(buyer_dtls_frame,text="Friday",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f16.place(x=1150,y=30)
    horizontal1 =Frame(buyer_dtls_frame, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=175)

    bill_tbl=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    bill_tbl.place(x=0,y=178,width=1308,height=400)


    global tree
    tree = ttk.Treeview(bill_tbl, column=("c1", "c2", "c3","c4"), show='headings',height=350)

    tree.column("#1", anchor=tk.W,width=830)

    tree.heading("#1", text="Item Name",anchor=tk.W)

    tree.column("#2", anchor=tk.CENTER,width=70)

    tree.heading("#2", text="Quantity")

    tree.column("#3", anchor=tk.CENTER,width=70)

    tree.heading("#3", text="Rate")

    tree.column("#4", anchor=tk.CENTER,width=70)

    tree.heading("#4", text="Amount")

    tree.pack(fill=tk.BOTH)

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="tally")
    c= conn.cursor()

    
   

    
    # c.execute("""CREATE TABLE if not exists stock (
    #     first_name text,
    #     last_name text,
    #     id integer,
    #     address text,
    #     city text,
    #     state text,
    #     zipcode text)
    #     """)
   
    
    # for record in data:
    #     c.execute("INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s)", record)
    # conn.commit()
    c.execute("SELECT * FROM stock")
    records = c.fetchall()

    for record in records:
        tree.insert("", "end", values=record)
    f11=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    f11.place(x=0,y=578,width=1308,height=110)
    l11=Label(f11,text="Narration",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l11.place(x=0,y=0)
    E11=Entry(f11,width=50,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=1)
    E11.place(x=0,y=20,height=50)
    
    l12=Label(f11,text="333322",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l12.place(x=1200,y=0)
   
def item_values():
    group_analysis_frame.destroy()
    label_1=Label(Canvas1, text="Item voucher analysis",borderwidth="0", width=20, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    
    global item_nm
    item_nm=Frame(Canvas1,height=200,width=1308,bg="white",relief=RAISED,bd=2)

    item_nm.place(x=0,y=21)
    lb1=Label(item_nm,text="Stock Item:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb1.place(x=0,y=0,anchor="nw")
    lb2=Label(item_nm,text="Item Name",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb2.place(x=80,y=0,anchor="nw")
    lb3=Label(item_nm,text="Inwards under ledger:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb3.place(x=0,y=20,anchor="nw")
    lb4=Label(item_nm,text="Item Name",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb4.place(x=150,y=20,anchor="nw")
    lb5=Label(item_nm,text="for apr-10-22",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb5.place(x=1200,y=0,anchor="nw")
    



    global item_val
    item_val=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    item_val.place(x=0,y=70,width=1308,height=650)
    global tree
    tree = ttk.Treeview(item_val, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8"), show='headings', height=650)

    tree.column("#1", anchor=tk.CENTER,width=50)

    tree.heading("#1", text="Date")

    tree.column("#2", anchor=tk.CENTER,width=830)

    tree.heading("#2", text="Perticulars")

    tree.column("#3", anchor=tk.CENTER,width=70)

    tree.heading("#3", text="Quantity")

    tree.column("#4", anchor=tk.CENTER,width=70)

    tree.heading("#4", text="Basic Rate")

    tree.column("#5", anchor=tk.CENTER,width=70)

    tree.heading("#5", text="Basic value")

    tree.column("#6", anchor=tk.CENTER,width=70)

    tree.heading("#6", text="Added cost")

    tree.column("#7", anchor=tk.CENTER,width=70)

    tree.heading("#7", text="Total value")

    tree.column("#8", anchor=tk.CENTER,width=70)

    tree.heading("#8", text="Eff.rate")
    tree.pack()
    tree.bind("<Double-1>",OnDoubleClick)
    




    horizontal =Frame(item_val, bg='white', height=100,width=1308)
    horizontal.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=545)
    l4f6=Label(horizontal,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f6.place(x=0,y=5,anchor="nw")

    l4f11=Label(horizontal,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f11.place(x=900,y=5,anchor="nw")
    l4f10=Label(horizontal,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f10.place(x=1000,y=5,anchor="nw")
    l4f9=Label(horizontal,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f9.place(x=1060,y=5,anchor="nw")
    l4f8=Label(horizontal,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1130,y=5,anchor="nw")
    l4f7=Label(horizontal,text="1000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f7.place(x=1190,y=5,anchor="nw")
    l4f8=Label(horizontal,text="10000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f8.place(x=1250,y=5,anchor="nw")

    

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="tally")
    c= conn.cursor()

    
   

    
    c.execute("""CREATE TABLE if not exists stock (
        first_name text,
        last_name text,
        id integer,
        address text,
        city text,
        state text,
        zipcode text)
        """)
   
    
    # for record in data:
    #     c.execute("INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s)", record)
    # conn.commit()
    c.execute("SELECT * FROM stock")
    records = c.fetchall()

    for record in records:
        tree.insert("", "end", values=record)
    
        

     



    
    # f16=Frame(movement_frame,bg="white",relief=RAISED,bd=2)
    # f16.place(x=610,y=145,width=340,height=450)
    # l3f6=Label(f16,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f6.place(x=0,y=0,anchor="nw")
    # l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f7.place(x=80,y=0,anchor="nw")
    # l3f8=Label(f16,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f8.place(x=180,y=0,anchor="nw")
    
def OnDoubleClick(e):
    label_1=Label(Canvas1, text="Accounting voucher alteration secondry",borderwidth="0", background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    item_nm.destroy()
    item_val.destroy()
    global bill_frame
    bill_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    bill_frame.place(x=0,y=20,width=1308,height=200)
    l1f1=Label(bill_frame,text="Purchase No:",font=("times new roman",11,"bold"),bg="#00254a",fg="white",borderwidth=0)
    l1f1.place(x=0,y=0)
    l1f2=Label(bill_frame,text="1",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f2.place(x=125,y=0)
    l1f3=Label(bill_frame,text="Supplier invoice no:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f3.place(x=0,y=20)

    l1f4=Label(bill_frame,text="1",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f4.place(x=135,y=20)
    
    l1f5=Label(bill_frame,text="Party A/c name:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f5.place(x=0,y=40)
    l1f6=Label(bill_frame,text="abc",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=125,y=40)
    l1f7=Label(bill_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=0,y=60)
    l1f8=Label(bill_frame,text="10000cr",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=125,y=60)
    l1f9=Label(bill_frame,text="Purchase ledger:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f9.place(x=0,y=80)
    l1f10=Label(bill_frame,text="Purchase acc",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f10.place(x=125,y=80)
    l1f11=Label(bill_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f11.place(x=0,y=100)
    l1f12=Label(bill_frame,text="10000cr",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f12.place(x=125,y=100)
    l1f13=Label(bill_frame,text="Date:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f13.place(x=300,y=20)
    l1f14=Label(bill_frame,text="01/01/2020",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f14.place(x=350,y=20)
    E1f15=Entry(bill_frame,width=20,font=("times new roman",11,"bold"),bg="yellow",fg="black",borderwidth=0)
    E1f15.place(x=1138,y=10)
    E1f15.insert(0,"01-10-21")
    l1f16=Label(bill_frame,text="Friday",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f16.place(x=1150,y=30)
    horizontal1 =Frame(bill_frame, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=175)

    bill_tbl=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    bill_tbl.place(x=0,y=178,width=1308,height=400)


    global tree
    tree = ttk.Treeview(bill_tbl, column=("c1", "c2", "c3","c4"), show='headings',height=350)

    tree.column("#1", anchor=tk.W,width=830)

    tree.heading("#1", text="Item Name",anchor=tk.W)

    tree.column("#2", anchor=tk.CENTER,width=70)

    tree.heading("#2", text="Quantity")

    tree.column("#3", anchor=tk.CENTER,width=70)

    tree.heading("#3", text="Rate")

    tree.column("#4", anchor=tk.CENTER,width=70)

    tree.heading("#4", text="Amount")

    tree.pack(fill=tk.BOTH)

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="tally")
    c= conn.cursor()

    
   

    
    # c.execute("""CREATE TABLE if not exists stock (
    #     first_name text,
    #     last_name text,
    #     id integer,
    #     address text,
    #     city text,
    #     state text,
    #     zipcode text)
    #     """)
   
    
    # for record in data:
    #     c.execute("INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s)", record)
    # conn.commit()
    c.execute("SELECT * FROM stock")
    records = c.fetchall()

    for record in records:
        tree.insert("", "end", values=record)
    f11=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    f11.place(x=0,y=578,width=1308,height=110)
    l11=Label(f11,text="Narration",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l11.place(x=0,y=0)
    E11=Entry(f11,width=50,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=1)
    E11.place(x=0,y=20,height=50)
    
    l12=Label(f11,text="333322",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l12.place(x=1200,y=0)
    
    
        















global f1
f1=Frame(Canvas2,bg="white",relief=FLAT,bd=0)
f1.pack()
   
def CurSelet(evt):
    value=lb.get(lb.curselection())
    print (value)   
    if value=="Stock Group Analysis":
        select_stl()

    elif value=="Stock Category Analysis":
        Stock_Cate_Analy()
    
    elif value=="Stock Item Analysis":

        stock_item_analy()

    elif value=="Group Analysis":

        group_analysis()
        

def stock_group_select(ent):
    value=lb.get(lb.curselection())
    if value=="Abc-ltd":
        selected_groups()

def stock_category_select(ent):
    value=lb.get(lb.curselection())
    if value=="primary":
        selected_category()


def stock_item_select(ent):
    value=lb.get(lb.curselection())
    if value=="soap":
        selected_item()


def group_item_select(ent):
    global grp_sel
    grp_sel=lb.get(lb.curselection())
    if grp_sel=="Bank account":
        Bank_account_group()
    elif grp_sel=="Bank OCC A/c":
        Bank_OCC_group()
    elif grp_sel=="Bank OD A/c":
        Bank_OD_group()
    elif grp_sel=="Branch/Division":
        Branch_Division_group()
    elif grp_sel=="Cash-in-hand":
        Cash_in_Hand_group()
    elif grp_sel=="Sundry Creditors":
        Sundry_Creditors_group()
    elif grp_sel=="Sundry Debtors":
        Sundry_Debtors_group()

def select_stl():
    global label_1
    label_1 = Label(Canvas1, text="Select stock group",borderwidth="0", width=20, background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    movement_analysis_frame.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()
    f5=Frame(Canvas2,bg="white",relief=RAISED,bd=1)
    f5.pack(pady=15)
    f6=Frame(Canvas2,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f6.pack()
    f0.destroy()
    l11=Label(f5,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack(padx=10,pady=10)
    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]
    cmb=ttk.Combobox(f5 ,values=options_list,font=("times new roman",10,"bold"))
    cmb.pack(fill=X,pady=10,padx=10)
    itemsforlistbox=['Abc-ltd','csd-ltd','vdf-ltd','daf-ltd']
    l5=Label(f6,text="List of stock group",font=hfont,bg="blue",fg="black")
    l5.pack(fill=X)
    global lb
    lb=Listbox(f6,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)  
    lb.bind('<<ListboxSelect>>',stock_group_select)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)
   
def  Stock_Cate_Analy():
    
    global label_1
    label_1 = Label(Canvas1, text="Select stock category",borderwidth="0", background="#3385ff", foreground="#00254a",  font="-family {Segoe UI} -size 10 -weight bold ")                                                   
    label_1.place(relx=0, rely=0)
    movement_analysis_frame.destroy()
    f0.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()
    global stock_category_frame
    stock_category_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    stock_category_frame.place(x=0,y=21,width=1308,height=660)
    f5=Frame(stock_category_frame,bg="white",relief=RAISED,bd=1)
    f5.pack(pady=15)
    f6=Frame(stock_category_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f6.pack()
    l11=Label(f5,text="Name of Category",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack(padx=10,pady=10)
    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]
    cmb=ttk.Combobox(f5 ,values=options_list,font=("times new roman",10,"bold"))
    cmb.pack(fill=X,pady=10,padx=10)
    itemsforlistbox=['primary','secondary']
    l5=Label(f6,text="List of stock Category",font=hfont,bg="blue",fg="black")
    l5.pack(fill=X)
    global lb
    lb=Listbox(f6,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)
    lb.bind('<<ListboxSelect>>',stock_category_select)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)


def stock_item_analy():
    global label_1
    label_1 = Label(Canvas1, text="Select stock item",borderwidth="0", width=20, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    movement_analysis_frame.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()

    f5=Frame(Canvas2,bg="white",relief=RAISED,bd=1)
    f5.pack(pady=15)
    f6=Frame(Canvas2,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f6.pack()

    f0.destroy()
    l11=Label(f5,text="Name of Item",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack(padx=10,pady=10)
    
    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]


    cmb=ttk.Combobox(f5 ,values=options_list,font=("times new roman",10,"bold"))
    cmb.pack(fill=X,pady=10,padx=10)

    itemsforlistbox=['soap','pen','book']

    l5=Label(f6,text="List of stock Item",font=hfont,bg="blue",fg="black")
    l5.pack(fill=X)

    global lb
    lb=Listbox(f6,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)

   
    lb.bind('<<ListboxSelect>>',stock_item_select)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)


def group_analysis():
    global label_1
    label_1 = Label(Canvas1, text="Select Group",borderwidth="0", width=20, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    movement_analysis_frame.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()
    movement_analysis_frame.destroy()
    global group_analysis_frame
    group_analysis_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    group_analysis_frame.place(x=0,y=21,width=1308,height=660)

    f5=Frame( group_analysis_frame,bg="white",relief=RAISED,bd=1)
    f5.pack(pady=15)
    f6=Frame( group_analysis_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f6.pack()

    f0.destroy()
    l11=Label(f5,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack(padx=10,pady=10)
    
    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]


    cmb=ttk.Combobox(f5 ,values=options_list,font=("times new roman",10,"bold"))
    cmb.pack(fill=X,pady=10,padx=10)

    itemsforlistbox=['Bank account','Bank OCC A/c','Bank OD A/c','Branch/Division','Cash-in-hand','Sundry Creditors','Sundry Debtors']

    l5=Label(f6,text="List of Group",font=hfont,bg="blue",fg="black")
    l5.pack(fill=X)

    global lb
    lb=Listbox(f6,height=10,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)

   
    lb.bind('<<ListboxSelect>>',group_item_select)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)

def main():
    global f0
    f0=Frame(Canvas2,bg="white",relief=RAISED,bd=5)
    f0.pack(pady=10)
    l5=Label(f0,text="statement of inv",font=hfont,bg="#3385ff",fg="black",)
    l5.pack(fill="x")
    bt1=Button(f0,text="Movement Analysis",font=hfont,bg="white",fg="black",command=movement_analysis)
    bt1.pack(fill="x",padx=10,pady=10)



main()
screen.mainloop()