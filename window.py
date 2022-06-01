from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk
import mysql.connector
from datetime import datetime, date, time, timedelta


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
Canvas1 = tk.Canvas(screen, background="#3385ff",relief=FLAT,bd=0,highlightthickness=0)
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
    
    label_1.destroy()
    label_0 = Label(Canvas1, text="Gate Way of Tally",borderwidth="0",width="40", background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_0.place(relx=0, rely=0)
    
    f1.destroy()
    global bk
    bk = Button(Canvas1, text="x", command=main, activeforeground="black", activebackground="#3385ff",
            fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)

    global movement_analysis_frame
    movement_analysis_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    movement_analysis_frame.place(x=0,y=21,width=1308,height=660)
    global f55
    global f66
    f55=Frame(movement_analysis_frame,bg="white",relief=RAISED,bd=1)
    f55.pack(pady=15)
    f66=Frame(movement_analysis_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f66.place(x=860,y=200,width=300,height=300)

    f0.destroy()
    # l11=Label(f55,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    # l11.pack(padx=10,pady=10)
    
    # options_list=["Period","Stock Category Analysis","Stock Item Analysis"]


    # cmb=ttk.Combobox(f55 ,values=options_list,font=("times new roman",10,"bold"))
    # cmb.pack(fill=X,pady=10,padx=10)

    itemsforlistbox=['Stock Group Analysis','Stock Category Analysis','Stock Item Analysis','Group Analysis','Exit']

    l5=Label(f66,text="Movement Analysis",font=hfont,bg="#0851a8",fg="white")
    l5.pack(fill=X)

    global lb
    lb=Listbox(f66,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)

   
    lb.bind('<<ListboxSelect>>',CurSelet)
    lb.pack(padx=10,pady=10)
    for items in itemsforlistbox:
        lb.insert(END,items)


def selected_groups(itm):
    

    


    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    
    label_1=Label(Canvas1, text="Stock group analysis",  borderwidth="0", width=40, background="#3385ff",
                                foreground="#00254a",   
                                font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    bk = Button(Canvas1, text="x", command=select_stl, activeforeground="black", activebackground="#3385ff",
            fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
    


    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    selected_groups_frame.place(x=0,y=21,width=1308,height=660)

    

    global tree0
    tree0=ttk.Treeview(selected_groups_frame, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)

    tree0.column("#1", anchor=tk.W,width=610)

    tree0.column("#2", anchor=tk.W,width=110)

    tree0.column("#3",anchor=tk.W,width=110)

    tree0.column("#4", anchor=tk.W,width=120)

    tree0.column("#5", anchor=tk.W,width=110)

    tree0.column("#6", anchor=tk.W,width=110)

    tree0.column("#7", anchor=tk.W,width=132)


    tree0.place(x=1,y=139)

    tree0.bind("<Double-1>", movement_val)

    conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
    mycursor=conn.cursor()
    mycursor.execute("select id from app_stock_groups where stock_group_name='"+itm+"'")
    gid=mycursor.fetchall()[0][0]
    mycursor.execute("select* from app_stock where stock_group_id_id='"+str(gid)+"'")
   
    stock_items=mycursor.fetchall()
    # print(stock_items)
    for i in stock_items:

        tree0.insert("",'end',values=(i[1],i[3],i[2],i[4]))

    mycursor.execute("select sum(stock_price) from app_stock where stock_group_id_id='"+str(gid)+"'")
    total=mycursor.fetchone()[0]
    conn.close()

    # dtsel=Button(Canvas3,text="date",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=date_select)
    # dtsel.pack(fill=X,pady=10,padx=10)

    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=0)
    f11.grid(row=1,column=0,columnspan=3,ipadx=200)
    l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
    l1f1.pack(fill=X)
    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=613,y=0,width=692,height=80)
    l1f2=Label(f12,text=itm,font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=305,y=10,anchor="center")
    l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=305,y=30,anchor="center")
    l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f4.place(x=305,y=50,anchor="center")



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
    l6f6=Label(f19,text=total,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l6f6.place(x=0,y=0,anchor="nw")

    f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f20.place(x=950,y=598,width=355,height=65)
    l7f6=Label(f20,text="000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l7f6.place(x=0,y=0,anchor="nw")
    
    def date_search():
        dasel.destroy()
        sdbtn.destroy()
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
        date_search_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
        date_search_frame.place(x=0,y=20,width=1308,height=680)
        dsf=Frame(date_search_frame,bg="white",relief=RAISED,bd=1)
        dsf.place(x=520,y=150,width=250,height=250)
        dsfl=Label(dsf,text="Change period",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        dsfl.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
        dsfl1=Label(dsf,text="From :",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        dsfl1.grid(row=1,column=0,columnspan=2,pady=10,padx=10)
        dsfl2=Label(dsf,text="To :",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        dsfl2.grid(row=2,column=0,columnspan=2,pady=10,padx=10)
        ent1=Entry(dsf,width=15,font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=1)
        ent1.grid(row=1,column=2,columnspan=2,pady=10,padx=10)
        ent2=Entry(dsf,width=15,font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=1)
        ent2.grid(row=2,column=2,columnspan=2,pady=10,padx=10)
        #get_date
        
        def dt_src(e):
            frm=ent1.get()
            to=ent2.get()
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
            mycursor=conn.cursor()
            mycursor.execute("select * from app_stock where date between '"+frm+"' and '"+to+"' and stock_group_id_id='"+str(gid)+"'")
            myresult=mycursor.fetchall()
            for i in myresult:
                tree0.insert("",END,values=i)
            

        ent1.bind("<KeyRelease>",dt_src)
        ent2.bind("<KeyRelease>",dt_src)




    global dasel
    dasel=Button(Canvas3,text="period",font=("times new roman",12,"bold"),bg="white",fg="black",command=date_search)
    dasel.place(x=3,y=18,width=218,height=30,anchor="w")
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",command=movement_analysis_back)
    sdbtn.place(x=3,y=50,width=218,height=30,anchor="w")
def statics():
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)
    ledger = Label(top, text="Statics", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    global selected_ledgers_frame
    selected_ledgers_frame=Frame(top,bg="white",relief=RAISED,bd=0)
    selected_ledgers_frame.place(x=1, y=73,width=1300, height=900)
    f16=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f16.place(x=500,y=90,width=120,height=900)
    f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,)
    f17.place(x=1180,y=90,width=120,height=900)
    b1s = Button(top,text = "   Contra", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b1s.place(x=0,y=165,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=0,anchor="nw") 
    
    b2s = Button(top,text = "   Credit Note", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b2s.place(x=0,y=190,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=25,anchor="nw")

    b3s = Button(top,text = "   Debit Note", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b3s.place(x=0,y=215,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=50,anchor="nw")
    
    b4s = Button(top,text = "   Job Work In Order", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b4s.place(x=0,y=240,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=75,anchor="nw")

    b5s = Button(top,text = "   Job Work Out Order", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b5s.place(x=0,y=265,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=100,anchor="nw")

    b6s = Button(top,text = "   Journel", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b6s.place(x=0,y=290,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=125,anchor="nw")

    b7s = Button(top,text = "   Meterial In", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b7s.place(x=0,y=315,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=150,anchor="nw")

    b8s = Button(top,text = "   Meterial Out", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b8s.place(x=0,y=340,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=175,anchor="nw")

    b9s = Button(top,text = "   Memorandum", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b9s.place(x=0,y=365,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=200,anchor="nw")

    b10s = Button(top,text = "   Payment", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b10s.place(x=0,y=390,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=225,anchor="nw")

    b11s = Button(top,text = "   Physical Stock", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b11s.place(x=0,y=415,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=250,anchor="nw") 
    
    b12s = Button(top,text = "   Purchase", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b12s.place(x=0,y=440,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=275,anchor="nw")

    b13s = Button(top,text = "   Purchase Order", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b13s.place(x=0,y=465,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=300,anchor="nw")
    
    b14s = Button(top,text = "   Reciept", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b14s.place(x=0,y=490,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=325,anchor="nw")

    b15s = Button(top,text = "   Reciept Note", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b15s.place(x=0,y=515,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=350,anchor="nw")

    b16s = Button(top,text = "   Rejections In", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b16s.place(x=0,y=540,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=375,anchor="nw")

    b17s = Button(top,text = "   Rejections Out", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b17s.place(x=0,y=565,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=400,anchor="nw")

    b18s = Button(top,text = "   Reversing Journel", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b18s.place(x=0,y=590,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=425,anchor="nw")

    b19s = Button(top,text = "   Sales", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b19s.place(x=0,y=615,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=450,anchor="nw")

    b20s = Button(top,text = "   Sales Order", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b20s.place(x=0,y=640,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=475,anchor="nw")

    b21s = Button(top,text = "   Stock Journel", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b21s.place(x=0,y=665,width=500,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=500,anchor="nw")

    b22s = Label(top,text = "   T o t a l", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b22s.place(x=20,y=745,height=18)
    l3f6=Label(f16,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=580,anchor="nw")

    b23s = Button(top,text = "   Groups", activeforeground = "black",command=list_of_groups, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b23s.place(x=650,y=165,width=500,height=18)
    l3f6=Label(f17,text="28",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=0,anchor="nw")

    b24s = Button(top,text = "   Ledgers", activeforeground = "black",command=list_of_ledgers, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b24s.place(x=650,y=190,width=500,height=18)
    l3f6=Label(f17,text="4",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=25,anchor="nw")

    b25s = Button(top,text = "   Stock Groups", activeforeground = "black",command=list_of_Stock_groups, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b25s.place(x=650,y=215,width=500,height=18)
    l3f6=Label(f17,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=50,anchor="nw")

    b26s = Button(top,text = "   Stock Items", activeforeground = "black",command=list_of_Stock_items, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b26s.place(x=650,y=240,width=500,height=18)
    l3f6=Label(f17,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=75,anchor="nw")

    b27s = Button(top,text = "   Voucher Types", activeforeground = "black",command=voucher_types, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b27s.place(x=650,y=265,width=500,height=18)
    l3f6=Label(f17,text="24",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=100,anchor="nw")

    b28s = Button(top,text = "   Units", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b28s.place(x=650,y=290,width=500,height=18)
    l3f6=Label(f17,text="0",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=125,anchor="nw")

    b29s = Button(top,text = "   Currencies", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b29s.place(x=650,y=315,width=500,height=18)
    l3f6=Label(f17,text="1",font=("Arial",10),bg="white",fg="black")
    l3f6.place(x=10,y=150,anchor="nw") 
    
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.10, relheight=0, relwidth=0.845)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.15, relheight=0, relwidth=0.845)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(x=480, y=735, relheight=0, width=135)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(x=480, y=765, relheight=0, width=135)
    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.10, relheight=1, relwidth=0)
    name = Label(top, bg='#ffffff',text="Type of vouchers", font=(
    'Arial 10'), anchor='w').place(x=20, y=93)
    name = Label(top, bg='#ffffff',text="infox\nfor 1-apr-2022 ", font=(
    'Arial 9'), anchor='w').place(x=480, y=90) 
    name = Label(top, bg='#ffffff',text="Type of Accounts", font=(
    'Arial 10'), anchor='w').place(x=650, y=93)
    name = Label(top, bg='#ffffff',text="infox\nfor 1-apr-2022 ", font=(
    'Arial 9'), anchor='w').place(x=1160, y=90)  

def list_of_groups():
    name = Label(top, text="Chart Of Accounts", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1600, height=13)

    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    name = Label(top, fg='#00c8ff', bg='#ffffff', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=0, y=73, width=1300, height=900)

    b4 = Button(top, text="x", command=statics, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    name = Label(top, bg='#ffffff',text="List Of Groups", font=(
    'Arial 12'), anchor='w').place(x=0, y=79)
    name = Label(top, bg='#ffffff',text="For April-1", font=(
    'Arial 12'), anchor='w').place(x=1200, y=79)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(x=0, y=110, relheight=0, relwidth=0.845) 
    b1s = Button(top,text = "Branch/Divisions", activeforeground = "black",command=branch_edit, activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b1s.place(x=0,y=125,width=1300,height=18)
    b2s = Button(top,text = "Capitals Account", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b2s.place(x=0,y=145,width=1300,height=18)
    b3s = Button(top,text = "Reserves & Surplus", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b3s.place(x=20,y=165,width=1280,height=18)
    b4s = Button(top,text = "Current Assets", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b4s.place(x=0,y=185,width=1300,height=18)
    b5s = Button(top,text = "Bank Accounts", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b5s.place(x=20,y=205,width=1280,height=18)
    b6s = Button(top,text = "Cash In Hand", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b6s.place(x=20,y=225,width=1280,height=18)
    b7s = Button(top,text = "Deposits(Assets)", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b7s.place(x=20,y=245,width=1280,height=18)
    b8s = Button(top,text = "Loans & Advances(Assets)", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b8s.place(x=20,y=265,width=1280,height=18)
    b9s = Button(top,text = "Stock In Hand", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b9s.place(x=20,y=285,width=1280,height=18)
    b10s = Button(top,text = "Sundry Debtors", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b10s.place(x=20,y=305,width=1280,height=18)
    b11s = Button(top,text = "Current Liabilities", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b11s.place(x=0,y=325,width=1300,height=18)
    b12s = Button(top,text = "Duties & Taxes", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b12s.place(x=20,y=345,width=1280,height=18)
    b13s = Button(top,text = "Provisions", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b13s.place(x=20,y=365,width=1280,height=18)
    b14s = Button(top,text = "Sundry Creditors", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b14s.place(x=20,y=385,width=1280,height=18)
    b15s = Button(top,text = "Direct Expences", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b15s.place(x=0,y=405,width=1300,height=18)
    b16s = Button(top,text = "Direct Incomes", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b16s.place(x=0,y=425,width=1300,height=18)
    b17s = Button(top,text = "Fixed Assets", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b17s.place(x=0,y=445,width=1300,height=18)
    b18s = Button(top,text = "Indirect Expences", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b18s.place(x=0,y=465,width=1300,height=18)
    b19s = Button(top,text = "Indirect Incomes", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b19s.place(x=0,y=485,width=1300,height=18)
    b20s = Button(top,text = "Investments", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b20s.place(x=0,y=505,width=1300,height=18)
    b21s = Button(top,text = "Loans(Liabilities)", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b21s.place(x=0,y=525,width=1300,height=18)
    b22s = Button(top,text = "Bank OD A/c", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b22s.place(x=20,y=545,width=1280,height=18)
    b23s = Button(top,text = "Secured Loans", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b23s.place(x=20,y=565,width=1280,height=18)
    b24s = Button(top,text = "Un Secured Loans", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b24s.place(x=20,y=585,width=1280,height=18)
    b25s = Button(top,text = "Misc.Expences(ASSSET)", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b25s.place(x=0,y=605,width=1300,height=18)
    b26s = Button(top,text = "Purchace Accounts", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b26s.place(x=0,y=625,width=1300,height=18)
    b27s = Button(top,text = "Sales Accounts", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b27s.place(x=0,y=645,width=1300,height=18)
    b28s = Button(top,text = "Suspence A/C", activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial  10 bold'),anchor="w")
    b28s.place(x=0,y=665,width=1300,height=18)
def selected_category():
    f1.destroy()
    f3.destroy()
    sgaf1.destroy()
    Canvas2.destroy()
    
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    label_1.destroy()
    global label_2
    label_2=Label(Canvas1, text="Stock Category Movement Analysis",borderwidth="0",width="40", background="#3385ff",
                                foreground="#00254a",   
                                font="-family {Segoe UI} -size 10 -weight bold ")
    label_2.place(relx=0, rely=0)


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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    
    sdbtn.destroy()
    label_1.destroy()
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
    label_1=Label(Canvas1, text="Group Analysis",borderwidth="0",width="40", background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
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
    sdbtn.destroy()
    # dtsel.destroy()
    curItem = tree0.focus()
    item_list=(tree0.item(curItem)['values'][0])
    
    movement_values(item_list)

def movement_values(item_list):
    
        # tree0.insert("",'end',values=(i,qty,rate,value,total))
        # supplier_name=i[1]
        # qty=i[2]
        # rate=i[3]
        # value=i[4]
        # total=i[5]
        # date=i[6]
        

   


    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=movement_analysis_back)
    sdbtn.pack(fill=X,pady=10,padx=10)
    
    label_1=Label(Canvas1, text="Item movement analysis",borderwidth="0",width="40", background="#3385ff",
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
    l1f2=Label(f12,text=item_list,font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
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
    global tree00
    tree00=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree00.column("#1", anchor=tk.W,width=686)
    
    tree00.column("#2", anchor=tk.CENTER,width=120)

    tree00.column("#3",anchor=tk.CENTER,width=140)

    tree00.column("#4", anchor=tk.CENTER,width=140)

    tree00.column("#5", anchor=tk.CENTER,width=212)

    tree00.place(x=0,y=60)
    qw=item_list
    tree00.bind("<Double-1>",supplier)

    conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
    mycursor=conn.cursor()
    mycursor.execute("select id from app_stock where stock_name='"+item_list+"'")
    gid=mycursor.fetchone()[0]
    mycursor.execute("select* from app_supplier where product_name_id='"+str(gid)+"'")
    items=mycursor.fetchall()
    for i in items:
        tree00.insert("",'end',values=(i[1],i[2],i[3],i[4],i[5],i[6]))
    mycursor.execute("select sum(product_quantity) from app_supplier where product_name_id='"+str(gid)+"'")
    tqty=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_eff_rate) from app_supplier where product_name_id='"+str(gid)+"'")
    trate=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_value) from app_supplier where product_name_id='"+str(gid)+"'")
    tvalue=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_price) from app_supplier where product_name_id='"+str(gid)+"'")
    tprice=mycursor.fetchone()[0]
    tree00.insert("",'end',values=("Total",tqty,tprice,trate,tvalue))



    conn.close()



    


    # l4f6=Label(f13,text=tqty,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f6.place(x=706,y=150,anchor="nw")
    # l4f8=Label(f13,text=rate,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f8.place(x=860,y=150,anchor="nw")
    # l4f7=Label(f13,text=value,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f7.place(x=990,y=150,anchor="nw")
    # l4f8=Label(f13,text=total,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f8.place(x=1100,y=150,anchor="nw")

    # horizontal =Frame(f13, bg='black', height=1,width=600)
    # horizontal.place(x=705, y=175)


    
    f13bt4=Label(f13,text="Movement outwards",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt4.place(x=0,y=170,anchor="nw")
    f13bt5=Label(f13,text="Buyers",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    f13bt5.place(x=10,y=200,anchor="nw")

    tree1=ttk.Treeview(f13, column=("c1", "c2","c3","c4","c5"), show='headings',height=3)

    tree1.column("#1", anchor=tk.W,width=686)

    
    tree1.column("#2", anchor=tk.CENTER,width=120)
    tree1.column("#3",anchor=tk.CENTER,width=140)

    tree1.column("#4", anchor=tk.CENTER,width=140)

    tree1.column("#5", anchor=tk.CENTER,width=212)

    tree1.place(x=0,y=230)
    tree1.bind("<Double-1>",buyer)
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
    mycursor=conn.cursor()
    mycursor.execute("select id from app_stock where stock_name='"+item_list+"'")
    gid=mycursor.fetchone()[0]
    mycursor.execute("select * from app_buyer where product_name_id='"+str(gid)+"'")
    items=mycursor.fetchall()
    for i in items:
        tree1.insert("",'end',values=(i[1],i[2],i[3],i[4],i[5],i[6]))
    mycursor.execute("select sum(product_quantity) from app_buyer where product_name_id='"+str(gid)+"'")
    tqty=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_eff_rate) from app_buyer where product_name_id='"+str(gid)+"'")
    trate=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_value) from app_buyer where product_name_id='"+str(gid)+"'")
    tvalue=mycursor.fetchone()[0]
    mycursor.execute("select sum(product_price) from app_buyer where product_name_id='"+str(gid)+"'")
    tprice=mycursor.fetchone()[0]
    tree1.insert("",'end',values=("Total",tqty,tprice,trate,tvalue))
    mycursor.close()



    # l46=Label(f13,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l46.place(x=706,y=330,anchor="nw")
    # l48=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l48.place(x=860,y=330,anchor="nw")
    # l47=Label(f13,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l47.place(x=990,y=330,anchor="nw")
    # l48=Label(f13,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l48.place(x=1100,y=330,anchor="nw")

    # horizontal =Frame(f13, bg='black', height=1,width=600)
    # horizontal.place(x=705, y=355)
    



    
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
    curItem = tree00.focus()
    item_list=(tree00.item(curItem)['values'][0])
    item_values(item_list)

def buyer(e):
   buyer_dtls()
    

def buyer_dtls():
    label_1=Label(Canvas1, text="Accounting voucher alteration secondry",width="40",borderwidth="0", background="#3385ff",
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
   
def item_values(item_list):
    label_1=Label(Canvas1, text="Item voucher analysis",borderwidth="0", width=40, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    
    global item_nm
    item_nm=Frame(Canvas1,height=200,width=1308,bg="white",relief=RAISED,bd=2)

    item_nm.place(x=0,y=21)
    lb1=Label(item_nm,text="Stock Item:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb1.place(x=0,y=0,anchor="nw")
    lb2=Label(item_nm,text="item_name",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb2.place(x=80,y=0,anchor="nw")
    lb3=Label(item_nm,text="Inwards under ledger:",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb3.place(x=0,y=20,anchor="nw")
    lb4=Label(item_nm,text=item_list,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb4.place(x=150,y=20,anchor="nw")
    lb5=Label(item_nm,text="for apr-10-22",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    lb5.place(x=1200,y=0,anchor="nw")
    



    global item_val
    item_val=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    item_val.place(x=0,y=70,width=1308,height=650)
    global tree
    tree = ttk.Treeview(item_val, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8"), show='headings', height=650)

    tree.column("#1", anchor=tk.CENTER,width=100)

    tree.heading("#1", text="Date")

    tree.column("#2", anchor=tk.W,width=600)

    tree.heading("#2", text="Perticulars")

    tree.column("#3", anchor=tk.CENTER,width=100)

    tree.heading("#3", text="Quantity")

    tree.column("#4", anchor=tk.CENTER,width=100)

    tree.heading("#4", text="Basic Rate")

    tree.column("#5", anchor=tk.CENTER,width=100)

    tree.heading("#5", text="Basic value")

    tree.column("#6", anchor=tk.CENTER,width=100)

    tree.heading("#6", text="Added cost")

    tree.column("#7", anchor=tk.CENTER,width=100)

    tree.heading("#7", text="Total value")

    tree.column("#8", anchor=tk.CENTER,width=100)

    tree.heading("#8", text="Eff.rate")
    tree.pack()
    tree.bind("<Double-1>",OnDoubleClick)
    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="db")
    c= conn.cursor()
   
    c.execute("SELECT * FROM app_supplier  where supplier_name='"+str(item_list)+"'")
    records = c.fetchall()

    for i in records:
        tree.insert("", "end", values=(i[6], i[1], i[2], i[3], i[4], i[5]))
    
    c.execute("select sum(product_quantity) from app_supplier  where supplier_name='"+str(item_list)+"'")
    tqt=c.fetchone()[0]
    c.execute("select sum(product_price) FROM app_supplier  where supplier_name='"+str(item_list)+"'")
    tqp=c.fetchone()[0]
    c.execute("select sum(product_eff_rate) FROM app_supplier  where supplier_name='"+str(item_list)+"'")
    teff=c.fetchone()[0]
    c.execute("select sum(product_value) FROM app_supplier  where supplier_name='"+str(item_list)+"'")
    tval=c.fetchone()[0]
    tree.insert("", 'end', values=("Total","",tqt, tqp,teff, tval))

        






    horizontal =Frame(item_val, bg='white', height=100,width=1308)
    horizontal.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=520)
    horizontal1 =Frame(item_val, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=545)
    l4f6=Label(horizontal,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    l4f6.place(x=0,y=5,anchor="nw")

    # l4f11=Label(horizontal,text=tqt,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f11.place(x=900,y=5,anchor="nw")
    # l4f10=Label(horizontal,text=tqp,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f10.place(x=1000,y=5,anchor="nw")
    # l4f9=Label(horizontal,text=teff,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f9.place(x=1060,y=5,anchor="nw")
    # l4f8=Label(horizontal,text=tval,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f8.place(x=1130,y=5,anchor="nw")
    # l4f7=Label(horizontal,text="1000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f7.place(x=1190,y=5,anchor="nw")
    # l4f8=Label(horizontal,text="10000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l4f8.place(x=1250,y=5,anchor="nw")

    

   
    
   

    
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
    
     



    
    # f16=Frame(movement_frame,bg="white",relief=RAISED,bd=2)
    # f16.place(x=610,y=145,width=340,height=450)
    # l3f6=Label(f16,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f6.place(x=0,y=0,anchor="nw")
    # l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f7.place(x=80,y=0,anchor="nw")
    # l3f8=Label(f16,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
    # l3f8.place(x=180,y=0,anchor="nw")
    
def OnDoubleClick(e):
    item_list=tree.item(tree.selection())['values'][1]
    supplier_bill(item_list)

def supplier_bill(item_list):





    label_1=Label(Canvas1, text="Accounting voucher alteration secondry",width="40",borderwidth="0", background="#3385ff",
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
   
    bill_tbl=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    bill_tbl.place(x=0,y=178,width=1308,height=400)

    global tree12
    tree12 = ttk.Treeview(bill_tbl, column=("c1", "c2", "c3","c4"), show='headings',height=350)

    tree12.column("#1", anchor=tk.W,width=830)

    tree12.heading("#1", text="Item Name",anchor=tk.W)

    tree12.column("#2", anchor=tk.CENTER,width=70)

    tree12.heading("#2", text="Quantity")

    tree12.column("#3", anchor=tk.CENTER,width=70)

    tree12.heading("#3", text="Rate")

    tree12.column("#4", anchor=tk.CENTER,width=70)

    tree12.heading("#4", text="Amount")

    tree12.pack(fill=BOTH)
        



    

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="db")
    c= conn.cursor()
    c.execute("select id from app_supplier where supplier_name='"+str(item_list)+"'")
    sid=c.fetchone()[0]
    c.execute("SELECT * FROM app_supplier_bill  where supplier_name_id='"+str(sid)+"'")
    records = c.fetchall()
    c.execute("select * from app_supplier_bill inner join app_supplier on app_supplier_bill.supplier_name_id=app_supplier.id where app_supplier_bill.supplier_name_id='"+str(sid)+"'")
    nw=c.fetchall()
    print(records)
    for i in records:
        pno=i[0]
        supinv=i[1]
        date=i[2]
        cbl=i[3]
        acc=i[4]
        cbl2=i[5]
        tree12.insert("", "end", values=(i[1],i[2],i[3],i[4]))


    bill_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    bill_frame.place(x=0,y=20,width=1308,height=160)
    l1f1=Label(bill_frame,text="Purchase No:",font=("times new roman",11,"bold"),bg="#00254a",fg="white",borderwidth=0)
    l1f1.place(x=0,y=0)
    l1f2=Label(bill_frame,text=pno,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f2.place(x=125,y=0)
    l1f3=Label(bill_frame,text="Supplier invoice no:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f3.place(x=0,y=20)

    l1f4=Label(bill_frame,text=supinv,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f4.place(x=135,y=20)
    
    l1f5=Label(bill_frame,text="Party A/c name:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f5.place(x=0,y=40)
    l1f6=Label(bill_frame,text="Apple",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f6.place(x=125,y=40)
    l1f7=Label(bill_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f7.place(x=0,y=60)
    l1f8=Label(bill_frame,text=cbl,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f8.place(x=125,y=60)
    l1f9=Label(bill_frame,text="Purchase ledger:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f9.place(x=0,y=80)
    l1f10=Label(bill_frame,text=acc,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f10.place(x=125,y=80)
    l1f11=Label(bill_frame,text="Current balance:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f11.place(x=0,y=100)
    l1f12=Label(bill_frame,text=cbl2,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f12.place(x=125,y=100)
    l1f13=Label(bill_frame,text="Date:",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f13.place(x=300,y=20)
    l1f14=Label(bill_frame,text=date,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f14.place(x=350,y=20)
    E1f15=Entry(bill_frame,width=20,font=("times new roman",11,"bold"),bg="yellow",fg="black",borderwidth=0)
    E1f15.place(x=1138,y=10)
    E1f15.insert(0,"01-10-21")
    l1f16=Label(bill_frame,text="Friday",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l1f16.place(x=1150,y=30)
    horizontal1 =Frame(bill_frame, bg='black', height=1,width=1308)
    horizontal1.place(x=0, y=175)


    f11=Frame(Canvas1,bg="white",relief=RAISED,bd=1)
    f11.place(x=0,y=578,width=1308,height=110)
    l11=Label(f11,text="Narration",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l11.place(x=0,y=0)

    # E11=Entry(f11,width=50,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=1)
    # E11.place(x=0,y=20,height=50)
    tex=Text(f11,width=50,height=5,font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=1)
    tex.place(x=0,y=20,height=50)
    
    l12=Label(f11,text="333322",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=0)
    l12.place(x=1200,y=0)
    
   













global f1
f1=Frame(Canvas2,bg="white",relief=FLAT,bd=0)
f1.pack()
   
def CurSelet(evt):
    value=lb.get(lb.curselection())
    # print (value)   
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
    itm=value[0]
    selected_groups(itm)

def stock_category_select(ent):
    value=lb.get(lb.curselection())
    if value=="primary":
        selected_category()


def stock_item_select(ent):
    # value=lb.get(lb.curselection())
    # if value=="soap":
    #     selected_item()
    value=lb.get(lb.curselection())
    item_list=value[0]
    movement_values(item_list)


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

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
    





    global label_1
    label_1 = Label(Canvas1, text="Select stock group",borderwidth="0", width=40, background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    bk = Button(Canvas1, text="x", command=movement_analysis, activeforeground="black", activebackground="#3385ff",
            fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
    
    
    movement_analysis_frame.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()
    global select_stl_frame
    select_stl_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    select_stl_frame.place(x=0,y=21,width=1308,height=660)
    f5=Frame(select_stl_frame,bg="white",relief=RAISED,bd=1)
    f5.pack()
    f6=Frame(select_stl_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
    f6.pack()
    f0.destroy()
    l11=Label(f5,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack()
    E1 = Entry(f5,width=30,borderwidth="1",bg="#f7d065")
    E1.pack(padx=10,pady=20)
   

    
    

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="db")
    c= conn.cursor()
    c.execute('SELECT stock_group_name  FROM app_stock_groups')
    dt=c.fetchall()
    
   





    options_list=["Period","Stock Category Analysis","Stock Item Analysis"]
    # cmb=ttk.Combobox(f5 ,values=options_list,font=("times new roman",10,"bold"),background="#f7d065")
    # cmb.pack(fill=X,pady=10,padx=10)

    l5=Label(f6,text="List of stock group",font=hfont,bg="#0851a8",fg="white")
    l5.pack(fill=X)
    global lb
    lb=Listbox(f6,height=15,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)  
    lb.bind('<<ListboxSelect>>',stock_group_select)

    lb.pack(padx=10,pady=10)
    for items in dt:
        lb.insert(END,items)
    c.close()
    def db_search(e):
        search=E1.get()
        lb.delete(0,END)
        conn = mysql.connector.connect(host ="localhost",
                                            user = "root",
                                            password ="",
                                            db ="db")
        c= conn.cursor()
        c.execute('SELECT stock_group_name  FROM app_stock_groups WHERE stock_group_name LIKE "%{}%"'.format(search))
        dt=c.fetchall()
        if dt:
            for items in dt:
                lb.insert(END,items)
            c.close()
        else:
            messagebox.showinfo("No data found","No data found")
    
    E1.bind("<KeyRelease>",db_search)

def  Stock_Cate_Analy():
    
    global label_1
    label_1 = Label(Canvas1, text="Select stock category",borderwidth="0",width="40", background="#3385ff", foreground="#00254a",  font="-family {Segoe UI} -size 10 -weight bold ")                                                   
    label_1.place(relx=0, rely=0)
    bk = Button(Canvas1, text="x", command=movement_analysis, activeforeground="black", activebackground="#3385ff",
            fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
    
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
    l11=Label(f5,text="Name of Group",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
    l11.pack()
    E1 = Entry(f5,width=30,borderwidth="1",bg="#f7d065")
    E1.pack(padx=10,pady=20)
   
    l5=Label(f6,text="List of stock Category",font=hfont,bg="#0851a8",fg="white")
    l5.pack(fill=X)
    global lb
    lb=Listbox(f6,height=6,background="#e6ffff",font="-family {Segoe UI} -size 12",justify="left",activestyle="none",bd=0,selectmode=BROWSE,width=25)
    lb.bind('<<ListboxSelect>>',stock_group_select)
    lb.pack(padx=10,pady=10)
    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="db")
    c= conn.cursor()
    c.execute('SELECT stock_group_name  FROM app_stock_groups')
    dt=c.fetchall()

    for items in dt:
        lb.insert(END,items)
    c.close()
    def db_search(e):
        search=E1.get()
        lb.delete(0,END)
        conn = mysql.connector.connect(host ="localhost",
                                            user = "root",
                                            password ="",
                                            db ="db")
        c= conn.cursor()
        c.execute('SELECT stock_group_name  FROM app_stock_groups WHERE stock_group_name LIKE "%{}%"'.format(search))
        dt=c.fetchall()
        if dt:
            for items in dt:
                lb.insert(END,items)
            c.close()
        else:
            messagebox.showinfo("No data found","No data found")
    
    E1.bind("<KeyRelease>",db_search)


def stock_item_analy():
    global label_1
    label_1 = Label(Canvas1, text="Select stock item",borderwidth="0", width=40, background="#3385ff",
                                    foreground="#00254a",   
                                    font="-family {Segoe UI} -size 10 -weight bold ")
    label_1.place(relx=0, rely=0)
    movement_analysis_frame.destroy()
    f1.destroy()
    f55.destroy()
    f66.destroy()
    global stock_item_analy_frame
    stock_item_analy_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
    stock_item_analy_frame.place(x=0,y=21,width=1308,height=660)
    f5=Frame(stock_item_analy_frame,bg="white",relief=RAISED,bd=1)
    f5.pack(pady=15)
    f6=Frame(stock_item_analy_frame,bg="white",relief=RAISED,bd=1,background="#e6ffff",width=100)
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

    conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password ="",
                                     db ="db")
    c= conn.cursor()
    c.execute('SELECT stock_name  FROM app_stock')
    dt=c.fetchall()

    for items in dt:
        lb.insert(END,items)


def group_analysis():
    global label_1
    label_1 = Label(Canvas1, text="Select Group",borderwidth="0", width=40, background="#3385ff",
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
    f0=Frame(Canvas2,bg="#a9ceeb",relief=GROOVE,bd=1)
    f0.place(x=860,y=200,width=300,height=300)
    # l5=Label(f0,text="statement of inv",font=hfont,bg="#3385ff",fg="black",)
    # l5.pack(fill="x")
    # bt1=Button(f0,text="Movement Analysis",font=hfont,bg="white",fg="black",command=movement_analysis)
    # bt1.pack(fill="x",padx=10,pady=10)
    menuname = Label(f0,text="Statements Of inv", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='w').pack(fill=X)

    b10 = Button(f0,text = "Movement Analysis",anchor="w",command=movement_analysis,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).pack(fill=X,padx=10,pady=10)




main()
screen.mainloop()