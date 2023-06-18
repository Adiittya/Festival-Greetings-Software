
import tkinter
import customtkinter as ct
from tkinter import ttk   
from PIL import ImageTk, Image
import database as db
import mail
import notification
from CTkMessagebox import CTkMessagebox 
from tkinter import StringVar
from datetime import *
import upcoming
import time
import netcheck
import pygame


class exception:
        
      def error(self,error):
        print(error)
        self.msg=ctkmessagebox = CTkMessagebox( title='Error', message=f'Something went Wrong ! \\nError:{error}', fade_in_duration=100, option_1="Cancel", option_2="Retry")
        ctkmessagebox.after(10000, ctkmessagebox.button_event)

        if self.msg.get()=='Retry':
            ctkmessagebox.destroy()

        elif self.msg.get()=='Cancel':
            return False
        
#-----------------------------------------------------Register class ----------------------------------------------------------------------------
        
class Register(exception):
    global reg_img
    def change_mode(self,mode):
        ct.set_appearance_mode(mode)
        print("gdrgd")
        if mode=='dark':
            self.reg_l3.configure(text_color='white')
        elif mode=='light':
            self.reg_l3.configure(text_color='black')

    def __init__(self):
        print(ct.AppearanceModeTracker)
        reg_switch_var = True
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("green")  # theme
        self.reg_app = ct.CTk()  # obejct
        self.reg_app.geometry("660x440")  # defing default window size
        self.reg_app.title("Register")  # title of the reg_frame
        self.reg_img = ImageTk.PhotoImage(Image.open("fest_photos\\bg.jpg"))
        self.reg_l1 = ct.CTkLabel(master=self.reg_app, image=self.reg_img)
        self.reg_l1.pack()

        self.reg_frame = ct.CTkFrame(master=self.reg_l1, width=320, height=360)
        self.reg_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.reg_l2 = ct.CTkLabel(master=self.reg_frame, text="Resgister", font=('Segoe UI', 20))
        self.reg_l2.place(x=50, y=35)

        self.reg_entry1 = ct.CTkEntry(master=self.reg_frame, width=220, placeholder_text="Name")
        self.reg_entry1.place(x=50, y=90)

        self.reg_entry2 = ct.CTkEntry(master=self.reg_frame, width=220, placeholder_text="Email")
        self.reg_entry2.place(x=50, y=135)

        self.reg_entry3 = ct.CTkEntry(master=self.reg_frame, width=220,
                                placeholder_text="Password", show="*")
        self.reg_entry3.place(x=50, y=180)

        self.reg_l3 = ct.CTkButton(master=self.reg_frame, text="Already registered ?", font=('Segoe UI', 12),fg_color="transparent",hover=False,command=self.Call_login)
        self.reg_l3.place(x=165, y=280)

        reg_button1 = ct.CTkButton(master=self.reg_frame, width=220, text='Register', corner_radius=10, command=self.reg)
        reg_button1.place(x=50, y=240)

        reg_switch_var = ct.StringVar(value="off")
        reg_switch_1 = ct.CTkSwitch(master=self.reg_frame, variable=reg_switch_var, text="", width=10, onvalue="light",offvalue="dark", bg_color="transparent", command=lambda:self.change_mode(reg_switch_var.get()))
        reg_switch_1.place(x=230, y=310)

        self.reg_app.mainloop()



    def reg(self):  # login validation with database
            # if self.reg_entry1.get()
        name = self.reg_entry1.get()
        mail = self.reg_entry2.get()
        password = self.reg_entry3.get()
        try:
            if name != "" and password != "" and mail != "":

                self.reg_entry1.delete(0, "end")
                self.reg_entry2.delete(0, "end")
                self.reg_entry3.delete(0, "end")
                db.connection("insert into authentication(user_name, user_pass, email) values (%s, %s, %s)", (name, password, mail))
                self.reg_app.destroy()
                self.Call_login()
                        
            else:
                self.reg_l4 = ct.CTkLabel(master=self.reg_frame, text="All fields are compulsory !", font=('Segoe UI', 12), text_color="red")
                self.reg_l4.place(x=10, y=280)
                self.reg_l4.after(2000, self.reg_l4.destroy)

        except Exception as a:
            print(a)
            self.c=self.error(a)
            if self.c==False:
                self.reg_app.destroy()
                exit()

    def Call_login(self):
        self.log=Loginapp()

        # opening image and storing it to varibale
        
#-----------------------------------------------------Login class ---------------------------------------------------------------------------

class Loginapp(exception):
    def change_mode(self,mode):
        ct.set_appearance_mode(mode)
        print("gdrgd")

    def __init__(self):

        self.log_switch_var=True
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("green") #theme 
        self.log_app=ct.CTk() #obejct
        self.log_app.geometry("660x440") #defing default window size
        self.log_app.title("login")  #title of the frame
        self.log_img=ImageTk.PhotoImage(Image.open("fest_photos\\bg.jpg")) #opening image and storing it to varibale 
        self.log_l1=ct.CTkLabel(master=self.log_app,image=self.log_img)
        self.log_l1.pack()

        self.log_frame=ct.CTkFrame(master=self.log_l1, width=320, height=360)
        self.log_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.log_l2=ct.CTkLabel(master=self.log_frame,text="Log into your Account",font=('Century Gothic',20))
        self.log_l2.place(x=50,y=45)

        self.log_entry1=ct.CTkEntry(master=self.log_frame,width=220,placeholder_text="Username")
        self.log_entry1.place(x=50,y=110)

        self.log_entry2=ct.CTkEntry(master=self.log_frame,width=220,placeholder_text="Password",show="*")
        self.log_entry2.place(x=50,y=165)

        self.log_l2=ct.CTkLabel(master=self.log_frame,text="Forget password?",font=('Century Gothic',12))
        self.log_l2.place(x=165,y=195)

        self.log_button1=ct.CTkButton(master=self.log_frame,width=220,text='login',corner_radius=10,command=self.login)
        self.log_button1.place(x=50,y=240)

        log_switch_var = ct.StringVar(value="off")
        log_switch_1 = ct.CTkSwitch(master=self.log_frame,variable=log_switch_var,text="",width=10, onvalue="light", offvalue="dark",bg_color="transparent",command=lambda:self.change_mode(log_switch_var.get()))
        log_switch_1.place(x=200,y=300)
        
        self.log_app.mainloop()


    def login(self): #login validation with database
        self.user=self.log_entry1.get()
        self.passw=self.log_entry2.get()
        self.log_entry1.delete(0,"end")
        self.log_entry2.delete(0,"end")

        try:
            row=db.connection("select * from authentication where user_name=%s and user_pass=%s",(self.user, self.passw))
            if row!=[]:
                print("login succsesful aditya")
                print(row)
                self.log_1=ct.CTkLabel(master=self.log_frame,text="Login succsesfully",font=("Segoe UI",12),text_color="green")
                self.log_1.place(x=50,y=300)
                self.button_func()
                #register()
            else:
                print(row)
                print("Acsses denied")
                self.log_1=ct.CTkLabel(master=self.log_frame,text="Access denied",font=("Segoe UI",12),text_color="red")
                self.log_1.place(x=50,y=300)
        except Exception as a:
            print(a)
            self.c=self.error(a)
            if self.c==False:
               exit()

    
            

    def button_func(self): #creat new window
        self.log_app.destroy()
        dashboard(self.user)


#----------------------------------------------------------------dashboard ----------------------------------------------------------------
class dashboard(Loginapp):
     
     def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"Time:{self.time}\nDate:{self.date}"
        self.t1.configure(text=set_text, font=("", 13, "bold"))
        self.t1.after(100, self.show_time)


     def net(self):
            if netcheck.internet():
                self.net_status.configure(text="Online", text_color="green")

            else:
                self.net_status.configure(text="Offline", text_color="red")
            self.net_status.after(2000, self.net)
        
            

     def logout(self):
         self.w.destroy()
         Loginapp()
        
     def changetheme(self,mode):
         self.mode=mode
         ct.set_appearance_mode(self.mode)

     def __init__(self,user):
        ct.set_appearance_mode("dark")
        self.user=user
        print(self.user)
        self.w=ct.CTk() #obejct
        self.w.geometry("1280x720") #defing default window size
        self.d_frame=ct.CTkFrame(master=self.w,height=800,width=250)
        self.d_frame.place(x=8,y=8)
        user="Aditya"

        try :
            self.name= db.connection("select user_name from authentication where id=%s",(self.user,))

        except Exception as a:
            print("Exception ",a)
            self.error(a)
        finally:
            self.image1 =ImageTk.PhotoImage(Image.open("fest_photos\profile-removebg-preview.png").resize((185,185))) 

            self.profile=ct.CTkLabel(master=self.d_frame, height=100, width=100, image=self.image1, text="")
            self.profile.place(x=48,y=88)
        
            self.d_l1=ct.CTkLabel( master=self.d_frame, text=self.user, font=('Century Gothic',20))
            self.d_l1.place(x=90,y=235,)
        
            self.t1=ct.CTkLabel(master=self.d_frame)
            self.t1.place(x=75,y=50)

            self.m_frame=ct.CTkFrame(master=self.w,height=800,width=1002)
            self.m_frame.place(x=268,y=8)

            self.customer_button=ct.CTkButton(master=self.d_frame,text='Customer',font=('Aerial',15),height=28, width=120,command=self.customer) 
            self.customer_button.place(x=65,y=300)

            self.fest_button=ct.CTkButton(master=self.d_frame,text='Festival',font=('Aerial',15),height=28, width=120,command=self.festival) 
            self.fest_button.place(x=65,y=350)


            self.image2=ImageTk.PhotoImage(Image.open("fest_photos\\logout.png").resize((21,21))) 
            self.logout=ct.CTkButton(master=self.d_frame,text='Logout',font=('Aerial',15),height=28, width=120, command=self.logout)
            self.logout.place(x=65,y=400)

            self.logimg=ct.CTkLabel(master=self.d_frame,text='',font=('Aerial',15),height=20, width=20, image=self.image2)
            self.logimg.place(x=195,y=450)

            log_switch_var = ct.StringVar(value="off")
            log_switch_1 = ct.CTkSwitch(master=self.d_frame,variable=log_switch_var,text="",width=10, onvalue="light", offvalue="dark",bg_color="transparent",command=lambda:self.changetheme(log_switch_var.get()))
            log_switch_1.place(x=160,y=500)

            self.net_status=ct.CTkLabel( master=self.d_frame, font=('Aerial',15,'bold'))
            self.net_status.place(x=100,y=0)

            self.net()
            self.show_time()
            self.default_win()
            self.w.mainloop()

#------------------Customer update function --------------------------
    #  def changetheme(self,mode):
    #      self.mode=mode
    #      ct.set_appearance_mode(self.mode)
    #      if self.mode=="light":
    #         print("light")
    #         self.c_l1.configure(fg_color='#ffffff')
    #      elif self.mode=="dark":
    #          print(self.color)
    #          self.c_l1.configure(fg_color='#2d2d2d')
        #  if ct.get_appearance_mode=='dark':
        #     self.color='#2d2d2d'
        #  elif ct.get_appearance_mode=='light':
        #     self.color='#ffffff's
     def default_win(self):
        self.msg,self.emails=mail.dec_fest(self.user)
        self.def_l3=ct.CTkLabel(master=self.m_frame,text=f"Festivlas :" ,font=("",18))
        self.def_l3.place(w=300,y=30)
        if self.msg:
            self.def_l1=ct.CTkLabel(master=self.m_frame,text=f"Emails sent to {len(self.emails)} customers\non occation of {self.msg} ",font=("",18))
            self.def_l1.place(w=300,y=80)
        else:
            self.def_l1=ct.CTkLabel(master=self.m_frame,text=f"Emails were not sent beacuse \nthere isn't any occation",font=("",18))
            self.def_l1.place(w=300,y=80)

        self.bmsg=mail.dec_bday(self.user)
        self.def_l4=ct.CTkLabel(master=self.m_frame,text="Birthday:" ,font=("",20))
        self.def_l4.place(w=300,y=150)
        if self.bmsg:
            self.def_l2=ct.CTkLabel(master=self.m_frame,text=f"Birthday greeting sent to {self.bmsg}",font=("",18))
            self.def_l2.place(w=350,y=200)
        else:
            self.def_l2=ct.CTkLabel(master=self.m_frame,text=f"No birthday of customer were found",font=("",18))
            self.def_l2.place(w=350,y=200)
    

        self.def_l4=ct.CTkLabel(master=self.m_frame,text="Upcoming Events",font=("",18))
        self.def_l4.place(w=350,y=250)

        self.def_l5=ct.CTkLabel(master=self.m_frame,text=upcoming.get_upcoming_events(),font=("",18))
        self.def_l5.place(w=350,y=290)
        
     def customer(self):
        self.m_frame.destroy()
        self.changetheme(ct.get_appearance_mode())
        print(ct.get_appearance_mode())


        self.cus_result=db.connection("select * from customers")
        self.table_view=ct.CTkFrame(master=self.w, height=450,width=1002 )#frame for table view
        self.table_view.place(x=275, y=20)
        self.columns = ('Id', 'Name', 'Email', 'State','birthdate','points')
#----------------------------------------------------------------TABLEVIEW START----------------------------------------------------------------
        self.tree = ttk.Treeview(self.table_view, columns=self.columns, show='headings',height=17)
        # define heading
    
        self.tree.heading('Id', text='Id')
        self.tree.column('Id',width=160)
        self.tree.heading('Name', text='Name')
        self.tree.column('Name',width=160)
        self.tree.heading('Email', text='Email')
        self.tree.column('Email',width=260)
        self.tree.heading('State', text='State')
        self.tree.column('State',width=210)
        self.tree.heading('birthdate', text='Birthdate')
        self.tree.column('birthdate',width=210)
        self.tree.heading('points', text='Points')
        self.tree.column('points',width=210)
        self.style=ttk.Style()
        self.style.configure("Treeview",
                             background="silver",
                             foreground="black",
                             rowheight=30,
                             fieldbackground="silver",
                             font=('Arial',13))
        # add data to the treeview
        for i in self.cus_result:
            self.tree.insert('', tkinter.END, values=i)


        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']

        self.tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.table_view, orient=tkinter.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

#----------------------------------------------------------------EMDOF TABLE VIEW:----------------------------------------------------------------

        #--------------------------------------labels and entry of customers:----------------------------------------------------------------
        self.cus_frame=ct.CTkFrame(master=self.w ,height=300, width=1000 , bg_color="transparent" ,fg_color="transparent")
        self.cus_frame.place(x=268, y=468)
        
        self.c1=ct.CTkLabel( master=self.cus_frame, text="Enter id of customer you want to update", font=('Aerial',15))
        self.c1.place(x=10,y=10)

        self.c_entry1=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="Id")
        self.c_entry1.place(x=10,y=40)    #end of Id label and entry

        self.c2=ct.CTkLabel( master=self.cus_frame, text="Name", font=('Aerial',15))
        self.c2.place(x=10,y=80)

        self.c_entry2=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="Name")
        self.c_entry2.place(x=10,y=110)# end of Name label and entry 
        
        self.c3=ct.CTkLabel( master=self.cus_frame, text="Email", font=('Aerial',15))
        self.c3.place(x=10,y=150) 

        self.c_entry3=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="Email")
        self.c_entry3.place(x=10,y=180) #end of Email label and entry 

        self.c4=ct.CTkLabel( master=self.cus_frame, text="State", font=('Aerial',15))
        self.c4.place(x=330,y=10)

        self.c_entry4=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="Location")
        self.c_entry4.place(x=330,y=40)  #end of locationlabel and entry 

        self.c5=ct.CTkLabel( master=self.cus_frame, text="Birthday", font=('Aerial',15))
        self.c5.place(x=330,y=80)
 
        self.c_entry5=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="YYYY-MM-dd")
        self.c_entry5.place(x=330,y=110)  #end of date label and entry 

        self.c4=ct.CTkLabel( master=self.cus_frame, text="Points", font=('Aerial',15))
        self.c4.place(x=330,y=150)

        self.c_entry6=ct.CTkEntry(master=self.cus_frame,width=200,placeholder_text="points")
        self.c_entry6.place(x=330,y=180)
#-------------------------------------------------Customers Buttons------------------------------------------------

        self.b1=ct.CTkButton(master=self.cus_frame, text="Update",command=self.custom_update)
        self.b1.place(x=730,y=40)  #update button

        self.b2=ct.CTkButton(master=self.cus_frame, text="refresh",command=self.customer)
        self.b2.place(x=730,y=110) #Refresh button 

        self.b3=ct.CTkButton(master=self.cus_frame, text="Add",command=self.custom_add)
        self.b3.place(x=730,y=180)  #Add button

        self.tree.bind('<<TreeviewSelect>>', self.cust_get_entry) #calls the function whenever the record is selecteed

     def cust_get_entry(self, e): #retriving data from rows
         
         self.c_entry1.delete(0, "end")
         self.c_entry2.delete(0, "end")
         self.c_entry3.delete(0, "end") 
         self.c_entry4.delete(0, "end")
         self.c_entry5.delete(0, "end")
         self.c_entry6.delete(0, "end")

         self.selected=self.tree.focus()
         self.values=self.tree.item(self.selected, 'values')
         self.c_entry1.insert(0, self.values[0])
         self.c_entry2.insert(0, self.values[1])
         self.c_entry3.insert(0, self.values[2])        
         self.c_entry4.insert(0, self.values[3])
         self.c_entry5.insert(0, self.values[4])
         self.c_entry6.insert(0, self.values[5])
        
     def custom_update(self):  #  customer update function
         id=self.c_entry1.get()
         name=self.c_entry2.get().capitalize()
         mail=self.c_entry3.get()
         location=self.c_entry4.get().capitalize()
         birthday=self.c_entry5.get()
         points=self.c_entry6.get()
        
         if id!="" and name!="" and mail!="" and location!="" and birthday!="" and points!="":
    
            self.c_entry1.delete(0,"end")
            self.c_entry2.delete(0,"end")
            self.c_entry3.delete(0,"end")
            self.c_entry4.delete(0,"end")
            self.c_entry5.delete(0,"end")
            self.c_entry6.delete(0,"end")
            print(self.b1.cget('text'))

            db.connection("UPDATE customers SET name=%s, email_id=%s, cust_state=%s, birthday=%s, points=%s WHERE id=%s", (name, mail, location, birthday, points, id))
            print("updated")

            pygame.mixer.init()
            pygame.mixer.music.load("audio_files\\success-1.mp3")
            pygame.mixer.music.play()

            self.error1 =ct.CTkLabel( master=self.cus_frame, text="Record updated", font=('Aerial',15),text_color="green")
            self.error1.place(x=735,y=215)
            self.error1.after(2000,self.error1.destroy)


         else:
             self.error1=ct.CTkLabel( master=self.cus_frame, text="All fields are compulsory !", font=('Aerial',15),text_color="red")
             self.error1.place(x=735,y=215)
             self.error1.after(2000,self.error1.destroy)


     def custom_add(self):  #customer add function
            id=self.c_entry1.get()
            name=self.c_entry2.get().capitalize()
            mail=self.c_entry3.get()
            state=self.c_entry4.get().capitalize()
            birthday=self.c_entry5.get()
            points=self.c_entry6.get()
            
            if name!="" and mail!="" and state!="" and birthday!="" and points!="":
        
                self.c_entry1.delete(0,"end")
                self.c_entry2.delete(0,"end")
                self.c_entry3.delete(0,"end")
                self.c_entry4.delete(0,"end")
                self.c_entry5.delete(0,"end")
                self.c_entry6.delete(0,"end")

                db.connection("INSERT INTO customers (id ,name , email_id, cust_state, birthday, points) values (%s, %s, %s, %s, %s, %s)", (id, name, mail, state, birthday, points))

                self.error1 =ct.CTkLabel( master=self.fest_frame, text="Record Added", font=('Aerial',15),text_color="green")
                self.error1.place(x=735,y=215)
                self.error1.after(2000,self.error1.destroy)

            else:
                self.error1=ct.CTkLabel( master=self.cus_frame, text="All fields are compulsory", font=('Aerial',15),text_color="red")
                self.error1.place(x=700,y=215)
                self.error1.after(2000,self.error1.destroy)

     #----------------------------------------------------------enf of customers gui-----------------------------------------

     def festival(self): # festival tab
        self.changetheme(ct.get_appearance_mode())
        print(ct.get_appearance_mode())
        self.m_frame.destroy()


        self.cus_result=db.connection("select * from fest_india")
        self.table_view_fest=ct.CTkFrame(master=self.w, height=450,width=1002 )#frame for table view
        self.table_view_fest.place(x=275, y=20)
        self.columns = ('Id', 'Festival Name', 'Date', 'Locality')
#----------------------------------------------------------------TABLEVIEW START----------------------------------------------------------------
        self.tree = ttk.Treeview(self.table_view_fest, columns=self.columns, show='headings',height=17)
        # define heading
    
        self.tree.heading('Id', text='Id')
        self.tree.column('Id',width=260)
        self.tree.heading('Festival Name', text='Festival Name')
        self.tree.column('Festival Name',width=350)
        self.tree.heading('Date', text='Date')
        self.tree.column('Date',width=300)
        self.tree.heading('Locality', text='Locality')
        self.tree.column('Locality',width=300)
        self.fest_style=ttk.Style()
        self.fest_style.configure("Treeview",
                             background="silver",
                             foreground="black",
                             rowheight=30,
                             fieldbackground="silver",
                             font=('Arial',13))
        # add data to the treeview
        for i in self.cus_result:
            self.tree.insert('', tkinter.END, values=i)


        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']

        self.tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        fest_scrollbar = ttk.Scrollbar(self.table_view_fest, orient=tkinter.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=fest_scrollbar.set)
        fest_scrollbar.grid(row=0, column=1, sticky='ns')

    #--------------------------festival labels and entry------------------------------------------------
        self.fest_frame=ct.CTkFrame(master=self.w ,height=300, width=1000 , bg_color="transparent" ,fg_color="transparent")
        self.fest_frame.place(x=268, y=468)
        
        self.c1=ct.CTkLabel( master=self.fest_frame, text="Enter id of festival you want to update", font=('Aerial',15))
        self.c1.place(x=10,y=10)

        self.c_entry1=ct.CTkEntry(master=self.fest_frame,width=200,placeholder_text="Id")
        self.c_entry1.place(x=10,y=40)

        self.c2=ct.CTkLabel( master=self.fest_frame, text=" Festival Name", font=('Aerial',15))
        self.c2.place(x=10,y=80)

        self.c_entry2=ct.CTkEntry(master=self.fest_frame,width=200,placeholder_text="Name")
        self.c_entry2.place(x=10,y=110)
        
        self.c3=ct.CTkLabel( master=self.fest_frame, text="Date", font=('Aerial',15))
        self.c3.place(x=10,y=150)

        self.c_entry3=ct.CTkEntry(master=self.fest_frame, width=200, placeholder_text="YYYY-MM-DD", font=('Aerial',15))
        self.c_entry3.place(x=10, y=180)

        self.c4=ct.CTkLabel( master=self.fest_frame, text="Locality", font=('Aerial',15))
        self.c4.place(x=330,y=10)

        self.c_entry4=ct.CTkEntry(master=self.fest_frame,width=200, placeholder_text="locality")
        self.c_entry4.place(x=330,y=40)

 #-------------------------------------festival buttons --------------------------------
        self.b1=ct.CTkButton(master=self.fest_frame, text="Update",command=self.fest_update)
        self.b1.place(x=730,y=40)

        self.b2=ct.CTkButton(master=self.fest_frame, text="refresh",command=self.festival)
        self.b2.place(x=730,y=110)

        self.b3=ct.CTkButton(master=self.fest_frame, text="Add",command=self.fest_add)
        self.b3.place(x=730,y=180)

        self.tree.bind('<<TreeviewSelect>>', self.fest_get_entry)

     def fest_get_entry(self, e):
         
         self.c_entry1.delete(0,"end")
         self.c_entry2.delete(0,"end")
         self.c_entry3.delete(0,"end") 
         self.c_entry4.delete(0,"end")
         self.selected=self.tree.focus()
         self.values=self.tree.item(self.selected, 'values')
         self.c_entry1.insert(0,self.values[0])
         self.c_entry2.insert(0,self.values[1])
         self.c_entry3. insert(0,self.values[2])        
         self.c_entry4.insert(0,self.values[3])
        
     def fest_update(self): #festival update function
         id=self.c_entry1.get()
         fest_name=self.c_entry2.get().capitalize()
         fest_date=self.c_entry3.get()

         locality=self.c_entry4.get().capitalize()
        
         if id!="" and fest_name!="" and fest_date!="" and fest_name!="" and locality!="":
    
            self.c_entry1.delete(0,"end")
            self.c_entry2.delete(0,"end")
            self.c_entry3.delete(0,"end") 
            self.c_entry4.delete(0,"end")

            try:
                db.connection("UPDATE fest_india SET fest_name=%s, fest_date=%s, locality=%s WHERE id=%s", (fest_name, fest_date, locality, id))
                print("updated")

                self.error1 =ct.CTkLabel( master=self.fest_frame, text="Record Updated", font=('Aerial',15),text_color="green")
                self.error1.place(x=735,y=215)
                self.error1.after(2000,self.error1.destroy)

                pygame.mixer.init()
                pygame.mixer.music.load("audio_files\\success-1.mp3")
                pygame.mixer.music.play()

            except Exception as e:
                self.e=e
                self.error(e)


         else:
             self.error1=ct.CTkLabel( master=self.fest_frame, text="All fields are compulsory !", font=('Aerial',15),text_color="red")
             self.error1.place(x=734,y=215)
             self.error1.after(2000,self.error1.destroy)


     def fest_add(self): # festival add function
            id=self.c_entry1.get()
            fest_name=self.c_entry2.get().capitalize()
            fest_date=self.c_entry3.get().capitalize()
            locality=self.c_entry4.get().capitalize()

            if id!=""and fest_name!="" and fest_date!="" :
        
                self.c_entry1.delete(0,"end")
                self.c_entry2.delete(0,"end")
                self.c_entry3.delete(0,"end")
                self.c_entry4.delete(0,"end")

                db.connection("INSERT INTO fest_india (id ,fest_name , fest_date, locality) values (%s, %s, %s, %s)", (id, fest_name, fest_date, locality))
                print("added")
                self.error1 =ct.CTkLabel( master=self.fest_frame, text="Record Added", font=('Aerial',15),text_color="green")
                self.error1.place(x=735,y=215)
                self.error1.after(2000,self.error1.destroy)

            else:
                self.error1 =ct.CTkLabel( master=self.fest_frame, text="All fields are compulsory !", font=('Aerial',15),text_color="red")
                self.error1.place(x=735,y=215)
                self.error1.after(2000,self.error1.destroy)

#----------------------------------------------------------------Main----------------------------------------------------------------

if __name__== '__main__':
    Res=Loginapp
