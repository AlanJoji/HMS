#Imported modules and files
from tkinter import *
import mysql.connector
import appointment_load as appload
import patient_load as patload
import doctor_load as docload

#Sql connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=#"<password>",
  database='test'
)

mycursor = mydb.cursor()
#reg_no is global
#did is global
#status is global for patient to differentiate quit between appointment and signin/up

#Function definitons

#Inserts default values to patient table 
def patient_create():
  
  #mycursor.execute("create table Patient1(reg_no int PRIMARY KEY, name varchar(100), age int(3), gender char(1), bloodgroup varchar(3), email_address varchar(100), ph_no double )")
  
  patload.create_patient_load()


#Inserting values into doctor table  
def doc_create():
  
  #mycursor.execute("create table Doctor1(doc_id char(4) PRIMARY KEY, name varchar(100), ph_no double, speciality varchar(100), e_mail varchar(100))")
  
  docload.create_doctor_load()


#Inserting values into appointment table 
def appoint_create():
  
  #mycursor.execute("CREATE TABLE Appointment1(D_Id char(4),9to9_30am varchar(4),9_30to10am varchar(4),10to10_30am varchar(4),10_30to11am varchar(4),11to11_30am varchar(4),11_30to12am varchar(4),foreign key (D_Id) references Doctor1 (doc_id))")
  mycursor.execute("select doc_id from doctor1")
  myresult=mycursor.fetchall()
  for x in myresult:
    appload.create_entry(x[0], 10)


#Doctor home page 
def doc_home():

    try:
        window16.destroy()
    except:
        #print ("W16 kill failed")
        print()
    try:
        window19.destroy()
    except:
        #print ("W19 kill failed")
        print()

    global window18
    window18 = Tk()
    window18.title("Doctor Homepage")
    #window18.geometry("400x400")
    window18.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

    button2 = Button(window18, text = "View Appointments", command = doc_apt).pack()
    button3 = Button(window18, text = "Click to exit", command = window18.quit).pack(side=BOTTOM)
    window18.mainloop()
    return()


#Patient home page 
def pat_home():
    #window2 and window3 are from appointment
    try:
        window12.destroy()
    except:
        #print("Window12 kill failed")
        print()
    try:
        window13.destroy()
    except:
        #print("Window13 kill failed")
        print()
    try:
        window14.destroy()
    except:
        #print("Window14 kill failed")
        print()
    try:
        window3.destroy()
    except:
        #print("Window3 kill failed")
        print()
    try:
        window7.destroy()
    except:
        #print("Unexpected error:", sys.exc_info()[0])
        #print("Window7 kill failed")
        print()
    try:
        window21.destroy()
    except:
        #print("Window21 kill failed")
        print()

    global window5
    window5=Tk()
    window5.title("Patient Homepage")
    #window5.geometry("400x400")
    window5.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

    label1=Label(window5,text="Do you want to:", fg= "green").pack()
    button1=Button(window5,text="Update Patient Details",command=update).pack()
   
    button2=Button(window5,text="Schedule Appointment",command=_speciality).pack()

    button3=Button(window5,text="Exit application",command=window5.quit).pack(side=BOTTOM)
    
    window5.mainloop()
    return()
    
#Appointment Scheduling 
#Chosing doctor's speciality window 
def _speciality():
    #print("In side function speciality")
    try:
        window5.destroy()
    except:
        #print("window4 could not be destroyed")
        print()
    try:
        window14.destroy()
    except:
        #print("Window14 kill failed")
        print()
    try:
        window12.destroy()
    except:
        #print("Window12 kill failed")
        print()

    global window9 
    window9 = Tk()
    window9.title("Appointments: Chose Doctor Specialising-in")
    #window9.geometry("400x400")
    window9.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
    
    mycursor.execute("select distinct speciality from Doctor1") 
    myresult = mycursor.fetchall()

    spec = []

    for x in myresult :
        spec.append(x[0])
    
    label = Label(window9, text = "Choose Doctor's Specialisation:", fg = "green").pack()
    global clicked1
    clicked1 = StringVar()
    clicked1.set(spec[0])

    dropdown = OptionMenu(window9, clicked1, *spec)
    dropdown.config(width = 20)
    dropdown.pack()

    button = Button(window9, text = "Click to Finalize", command = doctor).pack()


    window9.mainloop()    
    return()

#Chosing doctor for appointment
def doctor():
    global speciality
    speciality = clicked1.get()
    try:
        window9.destroy()
    except:
        #print("Window 9 kill failed")
        print()

    global window10
    window10 = Tk()
    window10.title("Appointments: Choose Doctor")
    #window10.geometry("400x400")
    window10.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
    
    label = Label(window10, text = "Choose your doctor:", fg="green").pack()
        
    mycursor.execute("select name from Doctor1 where speciality= '" +str(speciality)+"'") 
    myresult = mycursor.fetchall()

    doc = []

    for x in myresult :
        doc.append(x[0])
        
    label = Label(window10, text = "Choose Doctor's Name:",fg = "green").pack()
    
    global clicked2
    clicked2 = StringVar()
    clicked2.set(doc[0])

    dropdown = OptionMenu(window10, clicked2, *doc)
    dropdown.config(width = 20)
    dropdown.pack()

    button = Button(window10, text = "Click to Finalize", command = time).pack()
    
    window10.mainloop()
    return()

#Chosing time slot for appointment
def time():
    global name 
    name = clicked2.get()

    try:
        window10.destroy()
    except:
        #print("Window 10 destroy failed")
        print()

    global window11
    window11 = Tk()
    window11.title("Appointments: Choose Time")
    #window11.geometry("400x400")
    window11.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

    
    mycursor.execute("select doc_id from Doctor1 where name ='" + name + "'")
    myresult = mycursor.fetchall()

    #var4 is doctor id 
    for x in myresult:
        global did
        did = x[0]    

    mycursor.execute("select T_Start,T_End,DTTM from appointment1 where D_Id ='" + did + "' and P_ID is null")
    myresult = mycursor.fetchall()
    
    global appoint
    appoint = []

    for x in myresult:
        appoint.append(x)

    label = Label(window11, text="Select a suitable appointment")
    
    global listbox
    listbox = Listbox(window11,width = 45)

    counter = 1

    label = Label(window11, text = "Select the Time Slot for the Appointment",fg = "green").pack()
            
    listbox.insert(0,"From\t\t\t\tTo\t\t\t\tDate")

    for x in appoint:
        listbox.insert(counter,x[0]+":00\t\t\t\t"+x[1]+":00\t\t\t"+x[2].strftime("%d-%b-%Y"))
        counter = counter + 1 
            
        listbox.pack()

    button = Button(window11, text = "Finalize Time Slot", command = appointment_set).pack()

    window11.mainloop()

#Appointment final window (set/not set) 
def appointment_set():
    #print(listbox.curselection()[0])
    curr_selection = listbox.curselection()[0]
    try:
        window11.destroy()
    except:
        #print("Window 11 kill failed")
        print()
    
    try:
        if (curr_selection == 0):
            global window12
            window12 = Tk()
            window12.title("Appointment Not Set")
            #window12.geometry("400x400")
            window12.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

            label = Label(window12, text = "Incorrect Appointment Time Slot Selected ", fg="green").pack()
                        
            button1 = Button(window12, text = "Try again", command = _speciality).pack()
            button2 = Button(window12, text = "Return to Home Page", command = pat_home).pack()

            window12.mainloop()

        else:
            #print ("About to update")
            selection = appoint[curr_selection - 1]
            #print(selection)                      
            sql = "update appointment1 set P_ID= %s where D_ID= %s and DTTM= %s and T_Start= %s"
            val = (reg_no,did,selection[2],selection[0])
            mycursor.execute(sql,val)
            mydb.commit()   
                        
            mycursor.execute("select (name) from doctor1 where doc_id='" + did +"' ") 
            name=mycursor.fetchall()[0][0]
            
            #global window3
            global window13
            window13 = Tk()
            window13.title("Appointment Set Successful")
            #window13.geometry("400x400")
            window13.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

            status = False 

            label = Label(window13, text = "Appointment booked with " + str(name), fg="green" ).pack()
                        
            button = Button(window13, text = "Return to Home Page", command = pat_home).pack()

            window13.mainloop()
    except:
        #print("Unexpected error:", sys.exc_info()[0])
        global window14
        window14 = Tk()
        window14.title("Appointment Not Set")
        window14.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

        label = Label(window14, text = "Incorrect Appointment Time Slot Selected ", fg="green").pack()
                        
        button1 = Button(window14, text = "Try again", command = _speciality).pack()
        button2 = Button(window14, text = "Return to Home Page", command = pat_home).pack()

        window14.mainloop()

    return()
    
#Updating patient details 
#Values are changed by changing value in entry box
def update():
    try:
        window5.destroy()
    except:
        #print ("Window5 could not be killed")
        print()
    try:
        window8.destroy()
    except:
        #print ("Window8 could not be killed")
        print()
    try:
        window14.destroy()
    except:
        #print("Window14 kill failed")
        print()

    global window6
    window6 = Tk()
    window6.title("Update patient details:")
    #window6.geometry("400x400")
    window6.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
    
    label1 = Label(window6,text = "Current Patient details:",fg = "green")
    label1.grid(row=1,column=0)
    
    a = reg_no
   
    mycursor.execute("select * from patient1 where reg_no="+str(a))
    x = mycursor.fetchall()
    
    g = x[0][0]
    s = x[0][1]
    b = x[0][2]
    c = x[0][3]
    d = x[0][4]
    e = x[0][5]
    f = x[0][6]
        
    label2 = Label(window6,text="Name:")
    label2.grid(row=2,column=0)
    
    global entry2
    entry2 = Entry(window6,borderwidth=5)
    entry2.insert(0,s)
    entry2.grid(row=2,column=1)
    
    label3 = Label(window6,text="Age:")
    label3.grid(row=3,column=0)
    
    global entry3
    entry3 = Entry(window6,borderwidth=5)
    entry3.insert(0,b)
    entry3.grid(row=3,column=1)
    
    label4 = Label(window6,text="Gender:")
    label4.grid(row=4,column=0)
    
    global entry4
    entry4 = Entry(window6,borderwidth=5)
    entry4.insert(0,c)
    entry4.grid(row=4,column=1)
    
    label5 = Label(window6,text="Blood Group:")
    label5.grid(row=5,column=0)
    
    global entry5
    entry5 = Entry(window6,borderwidth=5)
    entry5.insert(0,d)
    entry5.grid(row=5,column=1)
    
    label6 = Label(window6,text="Email:")
    label6.grid(row=6,column=0)
    
    global entry6
    entry6 = Entry(window6,borderwidth=5)
    entry6.insert(0,e)
    entry6.grid(row=6,column=1)
    
    label7 = Label(window6,text="Phone Number:")
    label7.grid(row=7,column=0)
    
    global entry7
    entry7 = Entry(window6,borderwidth=5)
    entry7.insert(0,f)
    entry7.grid(row=7,column=1)
    
    button11 = Button(window6, text = "Update", command = up)
    button11.grid(row=8, column = 0)
    
    window6.mainloop()

    return()

#Updating the values from entry boxes
def up():
    h = entry2.get()
    i = entry3.get()
    j = entry4.get()
    k = entry5.get()
    l = entry6.get()
    m = entry7.get()
         
    if(0<len(h)<100  and 0<len(j)<4  and 0<len(l)<100 and len(str(m))==12):
        mycursor.execute("update patient1 set name='"+h+"',age='"+str(i)+"', gender='"+j+"', bloodgroup='"+k+"', email_address='"+l+"', ph_no='"+str(m)+"'where reg_no='"+str(reg_no)+"'")
        mydb.commit()
        
        i = True
    else:
        i = False

    if(i == True):
        window6.destroy()

        global window7
        window7 = Tk()
        window7.title("Patient Updation Successful")
        #window7.geometry("400x400")
        window7.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
        
        global status 
        status = True 
        label1=Label(window7,text="Your details have been updated",fg = "green").pack(side=TOP)
        button1=Button(window7,text="Click to Home Page",command=pat_home).pack()
        
        window7.mainloop()
    
    else:
        window8=Tk()
        window8.title("Patient Updation Not Successful")
        #window8.geometry("400x400")
        window8.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
        
        button1 = Button(window8,text="Click to try again",command=update).pack(side=TOP)
        button2 = Button(window8,text="Click to exit",command=window8.quit).pack(side=BOTTOM)
        
        window8.mainloop()
        return()
    
#Doctor appointment view
def doc_apt():
    try:
        window18.destroy()
    except:
        #print ("W18 kill failed")
        print()
    global window19
    window19 = Tk()
    window19.title("Doctor Appointment List")
    #window19.geometry("1000x650")
    window19.geometry('%dx%d+%d+%d' % (1000, 700, 100, 100))
    
    mycursor.execute("select a.P_ID, a.T_Start, a.T_End, a.DTTM, p.name from appointment1 a, patient1 p where a.D_ID='" + did + "' and a.P_ID = p.reg_no")
    myresult=mycursor.fetchall()
    
    l1 = []
    
    for x in myresult:
        l1.append(x)
    
    if len(l1) == 0:
        label1 = Label(window19, text = "No scheduled appointments").pack()
        button1 = Button(window19, text = "Go to Home page", command = doc_home).pack()
    
    else:
        label2 = Label(window19, borderwidth = 3, relief = "ridge", text = "Start Time", width = 20)
        label3 = Label(window19, borderwidth = 3, relief = "ridge", text = "End Time", width = 20)
        label4 = Label(window19, borderwidth = 3, relief = "ridge", text = "Date", width = 20)
        label5 = Label(window19, borderwidth = 3, relief = "ridge", text = "Patient Name", width = 20)
        
        label2.grid(row = 0, column = 0)
        label3.grid(row = 0, column = 1)
        label4.grid(row = 0, column = 2)
        label5.grid(row = 0, column = 3)
        
        for x in range(len(l1)):             
            label2 = Label(window19, borderwidth = 3, relief = "ridge", text = str(l1[x][1]), width = 20)
            label3 = Label(window19, borderwidth = 3, relief = "ridge", text = str(l1[x][2]), width = 20)
            label4 = Label(window19, borderwidth = 3, relief = "ridge", text = str(l1[x][3]), width = 20)
            label5 = Label(window19, borderwidth = 3, relief = "ridge", text = str(l1[x][4]), width = 20)
            label2.grid(row = x + 1, column = 0)
            label3.grid(row = x + 1, column = 1)
            label4.grid(row = x + 1, column = 2)
            label5.grid(row = x + 1, column = 3)
        
        global status 
        status = False 
        
        button = Button(window19, text = "Go to Home page", command = doc_home)
        button.grid(row = 100, column = 0)
        window19.mainloop()
    return()

#Patient
#Sign in/Sign up page    
def patient_click():
    w0.destroy()
    
    global window1
    
    window1 = Tk()
    window1.title("Account Creation and Sign in")
    #window1.geometry("400x400")
    window1.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))
    
    label1 = Label(window1,text="Select an option",fg="green")
    label1.pack()

    label2 = Label(window1,text="If you have an account",fg="black").pack()
    button2 = Button(window1,text="Sign in ",command=sign_in_click).pack()

    label3 = Label(window1,text="To Register",fg="black").pack()
    button3 = Button(window1,text="Sign up ",command=sign_up_click).pack()
    
    button4 = Button(window1,text="Exit",command=window1.quit,bg="grey").pack(side=BOTTOM)

    window1.mainloop()
    return ()

#Doctor 
#Doctor sign in 
def doc_click():
    try:        
        w0.destroy()
    except:
        #print("W0 kill failed")
        print()
    try:
        window17.destroy()
    except:
        #print("Window17 kill failed")
        print()

    global window15
    
    window15 = Tk()
    window15.title("Doctor Log in")
    #window15.geometry("400x400")
    window15.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

    label1 = Label(window15, text = "Doctor Log-in", fg = "green")
    label2 = Label(window15, text = "Enter your Doctor ID:")
    label3 = Label(window15, text = "Enter your Name:")
    
    global entry1
    entry1 = Entry(window15, borderwidth = 5, width = 20, bg = "grey")
    
    global entry2
    entry2 = Entry(window15, borderwidth = 5, width = 20, bg = "grey")
    
    button1 = Button(window15, text = "Log In", command = search_doctor)
    
    label1.grid(row = 0, column = 0)
    label2.grid(row = 2, column = 0)
    label3.grid(row = 4, column = 0)
    entry1.grid(row = 2, column = 1)
    entry2.grid(row = 4, column = 1)
    button1.grid(row = 5, column = 1)       
    
    window15.mainloop()
    
    return()

#Doctor search in table doctor1    
def search_doctor():

    try:    
        global name 
        name = entry2.get()
        global did
        did = entry1.get()

        sql = "select * from doctor1 where doc_id = %s and name = %s"
        val = (did, name)
            
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        
        i = None
            
        if len(myresult) == 0 :
           #print("Entered patient not found")
            i = False
            
        else:
            #print(myresult[0])
            #print("Entered patient found")
            i = True
    except:
        #print("An error occured")
        i = False
    try:
        window15.destroy()
    except:
        #print ("Window 15 kill failed")
        print()

    if(i==True):

        global window16
        window16 = Tk()
        window16.title("Doctor Login Successful")
        #window16.geometry("400x200")
        window16.geometry('%dx%d+%d+%d' % (400, 200, 100, 100))

        global status 
        status = True 
            
        #name = entry2.get()
        label1 = Label(window16, text = "Welcome to Newlife Hospital " + str(name), fg = "green").pack()
        button1 = Button(window16, text = "Click to go to Home Page", command = doc_home).pack()
        window16.mainloop()
    else:
        global window17
        window17 = Tk()
        window17.title("Doctor Login Not Successful")
        #window17.geometry("400x400")
        window17.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

        #name = entry2.get()
        button1 = Button(window17, text = "Click to try again", command = doc_click).pack(side = TOP)
        button2 = Button(window17, text = "Click to exit", command = window17.quit).pack(side = BOTTOM)
        window17.mainloop()

#Window opens sign-in if sign in fails
def sign_in_repeat():
    try:
        window4.destroy()
    except:
        #print ("W14 kill failed")
        print()

    sign_in_click()

#Patient sign-in
def sign_in_click():
    try:
        window1.destroy()
    except:
        #print("W1 destroy was failed")
        print()

    global window2 
    window2 = Tk()
    window2.title("Patient Sign in")
    #window2.geometry("350x400")
    window2.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

    label1 = Label(window2,text="Patient Sign-in",fg="green")

    label2 = Label(window2,text="Enter your Patient ID:")
    label3 = Label(window2,text="Enter your Name:")
    
    global entry1
    global entry2

    entry1 = Entry(window2,borderwidth=5,width=20, bg="grey")
    #entry1.insert(0,"ID")
    entry2 = Entry(window2,borderwidth=5,width=20, bg="grey")
    #entry2.insert(0,"Name")

    button1 = Button(window2,text="Sign In",command=search_patient)
    
    label1.grid(row=0,column=0)
    label2.grid(row=2,column=0)
    label3.grid(row=4,column=0)

    entry1.grid(row=2,column=1)
    entry2.grid(row=4,column=1)

    button1.grid(row=5,column=1)

    window2.mainloop()
    return()

#Patient search in patient1 
def search_patient():
    try:
        global reg_no
        reg_no = int(entry1.get())
        global name
        name = entry2.get()
        #print (pid,name)
            
        sql = "select * from patient1 where reg_no= %s and name = %s"
        val = (reg_no,name)
            
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
            
        i = None
            
        if len(myresult) == 0 :
            #print("Entered patient not found")
            i = False

        else:
            #print(myresult[0])
            #print("Entered patient found")
            i = True
            
    except:
        #print("An error occured")
        i = False
    if(i==True):
        window2.destroy()
        
        global window3
        window3 = Tk()
        window3.title("Patient Login Successful")
        #window3.geometry("400x200")
        window3.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

        #name = entry2.get()
        #status is used to differentiate quit for both appointment and Signin/up
        global status
        status = True

        label1 = Label(window3,text="Welcome to Newlife Hospital "+str(name),fg="green").pack()
        button1 = Button(window3,text="Click to go to Home Page",command=pat_home).pack()

        window3.mainloop()
    else:
        window2.destroy()
        
        global window4
        window4=Tk()
        window4.title("Patient Login Not Successful")
        #window4.geometry("400x400")
        window4.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

        #name = entry2.get()

        button1 = Button(window4,text="Click to try again",command=sign_in_repeat).pack(side=TOP)
        button2 = Button(window4,text="Click to exit",command=window4.quit).pack(side=BOTTOM)

        window4.mainloop()
    return()
    
#Patient sign-up and inputing of values
def sign_up_click():
    global window20

    try:
        window22.destroy()
    except:
        #print ("W22 kill failed")
        print()
    try:
        window1.destroy()
    except:
        #print ("W1 kill failed")
        print()
    try:
        window23.destroy()
    except:
        #print ("W23 kill failed")
        print()

    window20 = Tk()
    window20.title("Patient Signup")
    #window20.geometry("500x500")
    window20.geometry('%dx%d+%d+%d' % (500, 500, 100, 100))
    
    label1 = Label(window20,text="Enter your name:")
    label1.grid(row=0,column=0)
    
    global entry1
    entry1 = Entry(window20,borderwidth=5)
    entry1.grid(row=0,column=1)
    
    label2 = Label(window20,text="Enter your age:")
    label2.grid(row=1,column=0)
    
    global entry2
    entry2 = Entry(window20,borderwidth=5)
    entry2.grid(row=1,column=1)
    
    label3 = Label(window20,text="Enter your gender(F/M/O):")
    label3.grid(row=2,column=0)
    
    global entry3
    entry3 = Entry(window20,borderwidth=5)
    entry3.grid(row=2,column=1)
    
    label4 = Label(window20,text="Enter your blood group:")
    label4.grid(row=3,column=0)
    
    global entry4
    entry4 = Entry(window20,borderwidth=5)
    entry4.grid(row=3,column=1)
    
    label5 = Label(window20,text="Enter your email_id:")
    label5.grid(row=4,column=0)

    global entry5    
    entry5 = Entry(window20,borderwidth=5)
    entry5.grid(row=4,column=1)
    
    label6 = Label(window20,text="Enter your phone number:")
    label6.grid(row=5,column=0)
    
    global entry6
    entry6 = Entry(window20,borderwidth=5)
    entry6.grid(row=5,column=1)

    button10 = Button(window20, text = "Sign up", command = sign_up_patient)
    button10.grid(row = 0, column = 2)
    window20.mainloop()
    
    return()

#Adding patient to patient1
def sign_up_patient():
    try:
        global name 
        a = entry1.get() #name
        b = int(entry2.get()) #age
        c = entry3.get() #gender
        d = entry4.get() #email
        e = entry5.get() #phone
        f = int(entry6.get())
        if (0<len(a)<100 and 0<b<120 and 0<len(c)<4 and 0<len(d)<100 and len(str(f))==10):
            col = 0
            mycursor.execute("SELECT COUNT(reg_no) FROM patient1")
                
            for x in mycursor:
                col=x[0]
                
            global reg_no
            reg_no=col+1 
            

            sql = "insert into patient1(reg_no,name,age,gender,bloodgroup,email_address,ph_no) values ( %s, %s, %s, %s, %s, %s, %s)"
            val = (reg_no,a,b,c,d,e,f)
                
            mycursor.execute(sql,val)
            mydb.commit()
            i=True
            '''hello = entry1.get() + " has successfully signed up"+reg_no
            label7 = Label(window2, text = hello)
            label7.grid(row = 7, column = 0)'''
            
        else:
            #print("Entry failed here")
            i=False


        if(i==True):
            try:
                window20.destroy()
            except:
                #print ("W20 kill failed")
                print()

            global window21    
            window21=Tk()
            window21.title("Patient Login Successful")
            #window21.geometry("450x400")
            window21.geometry('%dx%d+%d+%d' % (450, 400, 100, 100))

            global status 
            status = True 
            #name = entry2.get()

            label1 = Label(window21,text="Welcome to Newlife Hospital "+str(a),fg="green").pack()
            label2 = Label(window21,text="Your has been account created").pack()
            label3 = Label(window21,text="Your Registration Number or Password:"+str(reg_no)).pack()
            label4 = Label(window21,text="(Sign in will require you to remember your Registration number)").pack()
            button1 = Button(window21,text="Click to go to Home Page",command=pat_home).pack(side=BOTTOM)

            window21.mainloop()
            
        else:
            try:
                window20.destroy()
            except:
                #print ("W20 kill failed")
                print()
            
            global window22
            window22=Tk()
            window22.title("Patient Sign up Not Successful")
            window22.geometry("400x400")

            button1 = Button(window22,text="Click to try again",command=sign_up_click).pack(side=TOP)
            button2 = Button(window22,text="Click to exit",command=window22.quit).pack(side=BOTTOM)

            window22.mainloop()

    except:
        #print("Unexpected error:", sys.exc_info()[0])
        '''hello2="Please enter correct details."
        label8=Label(window2, text=hello2)
        label8.grid(row=7,column=0)'''
        try:
            window20.destroy()
        except:
            #print ("W20 kill failed")
            print()
        global window23
        window23=Tk()
        window23.title("Patient Sign up Not Successful")
        #window23.geometry("400x400")
        window23.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

        button1 = Button(window23,text="Click to try again",command=sign_up_click).pack(side=TOP)
        button2 = Button(window23,text="Click to exit",command=window23.quit).pack(side=BOTTOM)

        window23.mainloop()

#__main__            
w0 = Tk()

#appoint_create()

w0.title("Newlife Hospitals")
w0.geometry('%dx%d+%d+%d' % (400, 400, 100, 100))

label1 = Label(w0 , text = "Hello user are you a ",fg="green").pack()

checkbox1 = Checkbutton(w0,text="Patient",command=patient_click).pack()
checkbox2 = Checkbutton(w0,text="Doctor",command=doc_click).pack()

button1 = Button(w0,text="Exit",command=w0.quit,bg="gray").pack(side=BOTTOM)

w0.mainloop()
