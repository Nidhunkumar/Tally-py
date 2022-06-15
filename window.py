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
    def dt_src():
        selected_groups_frame.destroy()
        frm=ent1.get()
        to=ent2.get()
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
        mycursor=conn.cursor()
        mycursor.execute("select * from app_stock where date between '"+frm+"' and '"+to+"' and stock_group_id_id='"+str(gid)+"'")
        myresult=mycursor.fetchall()

        if len(myresult)>0:
            label_1=Label(Canvas1, text="Stock group analysis",  borderwidth="0", width=40, background="#3385ff",
                                        foreground="#00254a",   
                                        font="-family {Segoe UI} -size 10 -weight bold ")
            label_1.place(relx=0, rely=0)
            bk = Button(Canvas1, text="x", command=select_stl, activeforeground="black", activebackground="#3385ff",
                    fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
            
            global selected_groups_frame_srch
            selected_groups_frame_srch=Frame(Canvas1,bg="white",relief=RAISED,bd=0)
            selected_groups_frame_srch.place(x=0,y=21,width=1308,height=660)

            global tree05
            tree05=ttk.Treeview(selected_groups_frame_srch, column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',height=22)

            tree05.column("#1", anchor=tk.W,width=610)

            tree05.column("#2", anchor=tk.W,width=110)

            tree05.column("#3",anchor=tk.W,width=110)

            tree05.column("#4", anchor=tk.W,width=120)

            tree05.column("#5", anchor=tk.W,width=110)

            tree05.column("#6", anchor=tk.W,width=110)

            tree05.column("#7", anchor=tk.W,width=132)

            tree05.place(x=1,y=139)

            tree05.bind("<Double-1>", movement_val)
            
            for i in myresult:
                
                tree05.insert("",'end',values=(i[1],i[3],i[2],i[4]))

            f11=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=0)
            f11.grid(row=1,column=0,columnspan=3,ipadx=200)
            l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,width=23,height=7)
            l1f1.pack(fill=X)
            f12=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f12.place(x=613,y=0,width=692,height=80)
            l1f2=Label(f12,text=itm,font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
            l1f2.place(x=305,y=10,anchor="center")
            l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
            l1f3.place(x=305,y=30,anchor="center")
            l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
            l1f4.place(x=305,y=50,anchor="center")



            f14=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f14.place(x=614,y=81,width=340,height=58)
            l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
            l1f5.place(x=0,y=0,anchor="nw")
            l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l1f6.place(x=0,y=30,anchor="nw")
            l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l1f7.place(x=110,y=30,anchor="nw")
            l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l1f8.place(x=225,y=30,anchor="nw")


            f15=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f15.place(x=955,y=81,width=350,height=58)
            l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
            l2f5.place(x=0,y=0,anchor="nw")
            l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l2f6.place(x=0,y=30,anchor="nw")
            l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l2f7.place(x=110,y=30,anchor="nw")
            l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
            l2f8.place(x=225,y=30,anchor="nw")



            
            f18=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f18.place(x=0,y=598,width=607,height=65)
            l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
            l5f6.place(x=1,y=0,anchor="nw")

            f19=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f19.place(x=610,y=598,width=340,height=65)
            l6f6=Label(f19,text=total,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
            l6f6.place(x=0,y=0,anchor="nw")

            f20=Frame(selected_groups_frame_srch,bg="white",relief=RAISED,bd=1)
            f20.place(x=950,y=598,width=355,height=65)
            l7f6=Label(f20,text="000",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
            l7f6.place(x=0,y=0,anchor="nw") 

        else:
            messagebox.showinfo("Error","No data found / Invalid date please try again in YYYY-MM-DD format")
            date_search()  

        # conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
        # mycursor=conn.cursor()
        # mycursor.execute("select id from app_stock_groups where stock_group_name='"+itm+"'")
        # gid=mycursor.fetchall()[0][0]
        # mycursor.execute("select* from app_stock where stock_group_id_id='"+str(gid)+"'")
    
        # stock_items=mycursor.fetchall()
        # # print(stock_items)
        # for i in stock_items:

        #     tree0.insert("",'end',values=(i[1],i[3],i[2],i[4]))

        # mycursor.execute("select sum(stock_price) from app_stock where stock_group_id_id='"+str(gid)+"'")
        # total=mycursor.fetchone()[0]
        # conn.close()

        # dtsel=Button(Canvas3,text="date",font=("times new roman",12,"bold"),bg="white",fg="black",relief=RAISED,bd=1,command=date_select)
        # dtsel.pack(fill=X,pady=10,padx=10)

        
    def date_search():
        dasel.destroy()
        sdbtn.destroy()
        global Canvas3
        bk = Button(Canvas1, text="x", command=select_stl, activeforeground="black", activebackground="#3385ff",
        fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)

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
        global ent1
        global ent2
        ent1=Entry(dsf,width=15,font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=1)
        ent1.grid(row=1,column=2,columnspan=2,pady=10,padx=10)
        ent2=Entry(dsf,width=15,font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=1)
        ent2.grid(row=2,column=2,columnspan=2,pady=10,padx=10)
        btn=Button(dsf,text="Search",width=10,font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=1,command=dt_src)
        btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10)
        
    global dasel
    dasel=Button(Canvas3,text="period",font=("times new roman",12,"bold"),bg="white",fg="black",command=date_search)
    dasel.place(x=3,y=18,width=218,height=30,anchor="w")
    global sdbtn
    sdbtn=Button(Canvas3,text="Back",font=("times new roman",12,"bold"),bg="white",fg="black",command=movement_analysis_back)
    sdbtn.place(x=3,y=50,width=218,height=30,anchor="w")
  
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
def OnDoubleClick(e):
    item_list=tree.item(tree.selection())['values'][1]
    supplier_bill(item_list)
class Item:
    def __init__(self, name, price, qty):
        self.product_name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.price * i.qty
        return total

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
    def allCart(self):
        for i in self.items:
            if (i.product_name in self.dictionary):
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name:i.qty})
    

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=biller)
    if sure == True:
        biller.destroy()
        root.destroy()


class bill_window:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Billing System")

        self.label = Label(biller)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/bill_window.png")
        self.label.configure(image=self.img)

        self.message = Label(biller)
        self.message.place(relx=0.038, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")

        self.clock = Label(biller)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(biller)
        self.entry1.place(relx=0.509, rely=0.23, width=240, height=24)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=cust_name)

        self.entry2 = Entry(biller)
        self.entry2.place(relx=0.791, rely=0.23, width=240, height=24)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=cust_num)

        self.entry3 = Entry(biller)
        self.entry3.place(relx=0.102, rely=0.23, width=240, height=24)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(textvariable=cust_search_bill)

        self.button1 = Button(biller)
        self.button1.place(relx=0.031, rely=0.104, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=logout)

        self.button2 = Button(biller)
        self.button2.place(relx=0.315, rely=0.234, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Search""")
        self.button2.configure(command=self.search_bill)

        self.button3 = Button(biller)
        self.button3.place(relx=0.048, rely=0.885, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Total""")
        self.button3.configure(command=self.total_bill)

        self.button4 = Button(biller)
        self.button4.place(relx=0.141, rely=0.885, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Generate""")
        self.button4.configure(command=self.gen_bill)

        self.button5 = Button(biller)
        self.button5.place(relx=0.230, rely=0.885, width=86, height=25)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 10")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Clear""")
        self.button5.configure(command=self.clear_bill)

        self.button6 = Button(biller)
        self.button6.place(relx=0.322, rely=0.885, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(command=exitt)

        self.button7 = Button(biller)
        self.button7.place(relx=0.098, rely=0.734, width=86, height=26)
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#CF1E14")
        self.button7.configure(cursor="hand2")
        self.button7.configure(foreground="#ffffff")
        self.button7.configure(background="#CF1E14")
        self.button7.configure(font="-family {Poppins SemiBold} -size 10")
        self.button7.configure(borderwidth="0")
        self.button7.configure(text="""Add To Cart""")
        self.button7.configure(command=self.add_to_cart)

        self.button8 = Button(biller)
        self.button8.place(relx=0.274, rely=0.734, width=84, height=26)
        self.button8.configure(relief="flat")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#CF1E14")
        self.button8.configure(cursor="hand2")
        self.button8.configure(foreground="#ffffff")
        self.button8.configure(background="#CF1E14")
        self.button8.configure(font="-family {Poppins SemiBold} -size 10")
        self.button8.configure(borderwidth="0")
        self.button8.configure(text="""Clear""")
        self.button8.configure(command=self.clear_selection)

        self.button9 = Button(biller)
        self.button9.place(relx=0.194, rely=0.734, width=68, height=26)
        self.button9.configure(relief="flat")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#CF1E14")
        self.button9.configure(cursor="hand2")
        self.button9.configure(foreground="#ffffff")
        self.button9.configure(background="#CF1E14")
        self.button9.configure(font="-family {Poppins SemiBold} -size 10")
        self.button9.configure(borderwidth="0")
        self.button9.configure(text="""Remove""")
        self.button9.configure(command=self.remove_product)

        text_font = ("Poppins", "8")
        self.combo1 = ttk.Combobox(biller)
        self.combo1.place(relx=0.035, rely=0.408, width=477, height=26)

        find_category = "SELECT product_cat FROM raw_inventory"
        cur.execute(find_category)
        result1 = cur.fetchall()
        cat = []
        for i in range(len(result1)):
            if(result1[i][0] not in cat):
                cat.append(result1[i][0])


        self.combo1.configure(values=cat)
        self.combo1.configure(state="readonly")
        self.combo1.configure(font="-family {Poppins} -size 8")
        self.combo1.option_add("*TCombobox*Listbox.font", text_font)
        self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")


        self.combo2 = ttk.Combobox(biller)
        self.combo2.place(relx=0.035, rely=0.479, width=477, height=26)
        self.combo2.configure(font="-family {Poppins} -size 8")
        self.combo2.option_add("*TCombobox*Listbox.font", text_font) 
        self.combo2.configure(state="disabled")


        self.combo3 = ttk.Combobox(biller)
        self.combo3.place(relx=0.035, rely=0.551, width=477, height=26)
        self.combo3.configure(state="disabled")
        self.combo3.configure(font="-family {Poppins} -size 8")
        self.combo3.option_add("*TCombobox*Listbox.font", text_font)

        self.entry4 = ttk.Entry(biller)
        self.entry4.place(relx=0.035, rely=0.629, width=477, height=26)
        self.entry4.configure(font="-family {Poppins} -size 8")
        self.entry4.configure(foreground="#000000")
        self.entry4.configure(state="disabled")

        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.439, rely=0.586, width=695, height=275)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        self.combo1.bind("<<ComboboxSelected>>", self.get_category)
        
    def get_category(self, Event):
        self.combo2.configure(state="readonly")
        self.combo2.set('')
        self.combo3.set('')
        find_subcat = "SELECT product_subcat FROM raw_inventory WHERE product_cat = ?"
        cur.execute(find_subcat, [self.combo1.get()])
        result2 = cur.fetchall()
        subcat = []
        for j in range(len(result2)):
            if(result2[j][0] not in subcat):
                subcat.append(result2[j][0])
        
        self.combo2.configure(values=subcat)
        self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
        self.combo3.configure(state="disabled")

    def get_subcat(self, Event):
        self.combo3.configure(state="readonly")
        self.combo3.set('')
        find_product = "SELECT product_name FROM raw_inventory WHERE product_cat = ? and product_subcat = ?"
        cur.execute(find_product, [self.combo1.get(), self.combo2.get()])
        result3 = cur.fetchall()
        pro = []
        for k in range(len(result3)):
            pro.append(result3[k][0])

        self.combo3.configure(values=pro)
        self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
        self.entry4.configure(state="disabled")

    def show_qty(self, Event):
        self.entry4.configure(state="normal")
        self.qty_label = Label(biller)
        self.qty_label.place(relx=0.033, rely=0.664, width=82, height=26)
        self.qty_label.configure(font="-family {Poppins} -size 8")
        self.qty_label.configure(anchor="w")

        product_name = self.combo3.get()
        find_qty = "SELECT stock FROM raw_inventory WHERE product_name = ?"
        cur.execute(find_qty, [product_name])
        results = cur.fetchone()
        self.qty_label.configure(text="In Stock: {}".format(results[0]))
        self.qty_label.configure(background="#ffffff")
        self.qty_label.configure(foreground="#333333")
    
    cart = Cart()
    def add_to_cart(self):
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total')==-1:
            product_name = self.combo3.get()
            if(product_name!=""):
                product_qty = self.entry4.get()
                find_mrp = "SELECT mrp, stock FROM raw_inventory WHERE product_name = ?"
                cur.execute(find_mrp, [product_name])
                results = cur.fetchall()
                stock = results[0][1]
                mrp = results[0][0]
                if product_qty.isdigit()==True:
                    if (stock-int(product_qty))>=0:
                        sp = mrp*int(product_qty)
                        item = Item(product_name, mrp, int(product_qty))
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=biller)
        else:
            self.Scrolledtext1.delete('1.0', END)
            new_li = []
            li = strr.split("\n")
            for i in range(len(li)):
                if len(li[i])!=0:
                    if li[i].find('Total')==-1:
                        new_li.append(li[i])
                    else:
                        break
            for j in range(len(new_li)-1):
                self.Scrolledtext1.insert('insert', new_li[j])
                self.Scrolledtext1.insert('insert','\n')
            product_name = self.combo3.get()
            if(product_name!=""):
                product_qty = self.entry4.get()
                find_mrp = "SELECT mrp, stock, product_id FROM raw_inventory WHERE product_name = ?"
                cur.execute(find_mrp, [product_name])
                results = cur.fetchall()
                stock = results[0][1]
                mrp = results[0][0]
                if product_qty.isdigit()==True:
                    if (stock-int(product_qty))>=0:
                        sp = results[0][0]*int(product_qty)
                        item = Item(product_name, mrp, int(product_qty))
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=biller)

    def remove_product(self):
        if(self.cart.isEmpty()!=True):
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                    new_string = get_all_bill[:len(get_all_bill)-3]
                    self.Scrolledtext1.delete('1.0', END)
                    for i in range(len(new_string)):
                        self.Scrolledtext1.insert('insert', new_string[i])
                        self.Scrolledtext1.insert('insert','\n')
                    
                    self.Scrolledtext1.configure(state="disabled")
            else:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split("\n")
                    for i in range(len(li)):
                        if len(li[i])!=0:
                            if li[i].find('Total')==-1:
                                new_li.append(li[i])
                            else:
                                break
                    new_li.pop()
                    for j in range(len(new_li)-1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert','\n')
                    self.Scrolledtext1.configure(state="disabled")

        else:
            messagebox.showerror("Oops!", "Add a product.", parent=biller)

    def wel_bill(self):
        self.name_message = Text(biller)
        self.name_message.place(relx=0.514, rely=0.452, width=176, height=30)
        self.name_message.configure(font="-family {Podkova} -size 10")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(biller)
        self.num_message.place(relx=0.894, rely=0.452, width=90, height=30)
        self.num_message.configure(font="-family {Podkova} -size 10")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(biller)
        self.bill_message.place(relx=0.499, rely=0.477, width=176, height=26)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(biller)
        self.bill_date_message.place(relx=0.852, rely=0.477, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")
    
    def total_bill(self):
        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Add a product.", parent=biller)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n"+("─"*61)
                self.Scrolledtext1.insert('insert', divider)
                total = "\nTotal\t\t\t\t\t\t\t\t\t\t\tRs. {}".format(self.cart.total())
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n"+("─"*61)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
            else:
                return

    state = 1
    def gen_bill(self):

        if self.state == 1:
            strr = self.Scrolledtext1.get('1.0', END)
            self.wel_bill()
            if(cust_name.get()==""):
                messagebox.showerror("Oops!", "Please enter a name.", parent=biller)
            elif(cust_num.get()==""):
                messagebox.showerror("Oops!", "Please enter a number.", parent=biller)
            elif valid_phone(cust_num.get())==False:
                messagebox.showerror("Oops!", "Please enter a valid number.", parent=biller)
            elif(self.cart.isEmpty()):
                messagebox.showerror("Oops!", "Cart is empty.", parent=biller)
            else: 
                if strr.find('Total')==-1:
                    self.total_bill()
                    self.gen_bill()
                else:
                    self.name_message.insert(END, cust_name.get())
                    self.name_message.configure(state="disabled")
            
                    self.num_message.insert(END, cust_num.get())
                    self.num_message.configure(state="disabled")
            
                    cust_new_bill.set(random_bill_number(8))

                    self.bill_message.insert(END, cust_new_bill.get())
                    self.bill_message.configure(state="disabled")
                
                    bill_date.set(str(date.today()))

                    self.bill_date_message.insert(END, bill_date.get())
                    self.bill_date_message.configure(state="disabled")

                    

                    with sqlite3.connect("./Database/store.db") as db:
                        cur = db.cursor()
                    insert = (
                        "INSERT INTO bill(bill_no, date, customer_name, customer_no, bill_details) VALUES(?,?,?,?,?)"
                    )
                    cur.execute(insert, [cust_new_bill.get(), bill_date.get(), cust_name.get(), cust_num.get(), self.Scrolledtext1.get('1.0', END)])
                    db.commit()
                    #print(self.cart.items)
                    print(self.cart.allCart())
                    for name, qty in self.cart.dictionary.items():
                        update_qty = "UPDATE raw_inventory SET stock = stock - ? WHERE product_name = ?"
                        cur.execute(update_qty, [qty, name])
                        db.commit()
                    messagebox.showinfo("Success!!", "Bill Generated", parent=biller)
                    self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.state = 0
        else:
            return
                    
    def clear_bill(self):
        self.wel_bill()
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.name_message.configure(state="normal")
        self.num_message.configure(state="normal")
        self.bill_message.configure(state="normal")
        self.bill_date_message.configure(state="normal")
        self.Scrolledtext1.configure(state="normal")
        self.name_message.delete(1.0, END)
        self.num_message.delete(1.0, END)
        self.bill_message.delete(1.0, END)
        self.bill_date_message.delete(1.0, END)
        self.Scrolledtext1.delete(1.0, END)
        self.name_message.configure(state="disabled")
        self.num_message.configure(state="disabled")
        self.bill_message.configure(state="disabled")
        self.bill_date_message.configure(state="disabled")
        self.Scrolledtext1.configure(state="disabled")
        self.cart.remove_items()
        self.state = 1

    def clear_selection(self):
        self.entry4.delete(0, END)
        self.combo1.configure(state="normal")
        self.combo2.configure(state="normal")
        self.combo3.configure(state="normal")
        self.combo1.delete(0, END)
        self.combo2.delete(0, END)
        self.combo3.delete(0, END)
        self.combo2.configure(state="disabled")
        self.combo3.configure(state="disabled")
        self.entry4.configure(state="disabled")
        try:
            self.qty_label.configure(foreground="#ffffff")
        except AttributeError:
            pass
             
    def search_bill(self):
        find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute(find_bill, [cust_search_bill.get().rstrip()])
        results = cur.fetchall()
        if results:
            self.clear_bill()
            self.wel_bill()
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")

            self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
            self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")

            self.state = 0

        else:
            messagebox.showerror("Error!!", "Bill not found.", parent=biller)
            self.entry3.delete(0, END)

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
    bk = Button(Canvas1, text="x", command=movement_analysis, activeforeground="black", activebackground="#3385ff",
            fg='black', bg='#3385ff', borderwidth=0, font=('Arial 16 bold'),).place(x=1280, y=0,height=18)
    
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
    
    E1 = Entry(f5,width=30,borderwidth="1",bg="#f7d065")
    E1.pack(padx=10,pady=20)



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



    def db_search(e):
        search=E1.get()
        lb.delete(0,END)
        conn = mysql.connector.connect(host ="localhost",
                                            user = "root",
                                            password ="",
                                            db ="db")
        c= conn.cursor()
        c.execute('SELECT stock_name  FROM app_stock WHERE stock_name LIKE "%{}%"'.format(search))
        dt=c.fetchall()
        if dt:
            for items in dt:
                lb.insert(END,items)
            c.close()
        else:
            messagebox.showinfo("No data found","No data found")
    
    E1.bind("<KeyRelease>",db_search)




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