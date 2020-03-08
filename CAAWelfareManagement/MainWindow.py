from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import empmngt
import financials
import data

#Authenticate user from username and password and allow entry into the app
def authenticate():
    username=uservar.get()
    password=passvar.get()
    notfound=0
    for document in data.db.userpass.find():
        if document["user"]==username and document["password"]==password:
            mainwindow()
            break            
        else:
            notfound+=1
            print("notfound: %s"%(notfound))
    if notfound >= data.db.userpass.count(): #Count number of documents in database
        messagebox.showinfo("Wrong Credentials","Please enter correct username and password")
    
#Cancel sign-in
def signindestroy():
    signin.destroy() 

#Employees module
def employees():
    empmngt.empmngtptl(top,portallabel,b1,b2,b3,b4,b5)

#Finance module
def finance():
    financials.finsptl(top,portallabel,b1,b2,b3,b4,b5)


# Main window
def mainwindow():
    global top
    global portallabel
    global b1
    global b2
    global b3
    global b4
    global b5
    
    signin.destroy()

    top = Tk()  
    top.geometry("1366x768") # Set window size (when not maximized)
    top.title("CAA Employees Welfare Management System")
    top.configure(background="white")
    # caalogo=PhotoImage(file='/home/waqas/Programming/Python/CAAWelfareManagement/CAA-Logo.png')
    # caalogo=ImageTk.PhotoImage(Image.open("CAA-Logo.png"))    
    caalogo=PhotoImage(file='CAA-Logo.png') # Above two commented lines would give the same result
    appimg=Label(top,image=caalogo,background="white").pack()
    applbl = Label(top,text = "CAA Employees Welfare Management System",padx=580,pady=25, fg="#058DC7", font=("Arial", 25, "bold"),background="white").pack()
    empman = Button(top, text = "Employees Management", height = 3, width = 50, bd = 5, command=employees).pack()
    emptyspace = Label(top,background="white").pack()
    fins = Button(top, text = "Financials", height = 3, width = 50, bd = 5, command=finance).pack()
    emptyspace = Label(top,padx=5, pady=5,background="white").pack()
    portallabel=Label(top,text = "",font=("Arial",15,"bold"),height = 3, width = 124, bg = "white", fg = "white", relief= GROOVE)
    b1=Button(top)
    b2=Button(top)
    b3=Button(top)
    b4=Button(top)
    b5=Button(top)
    awlbl = Label(top, text = "Developed by AW Inspirations",padx=25,pady=10,font=("Times",12,"italic","bold"),background="white").pack(side=BOTTOM)  
    top.mainloop()  


#Sign-in window
signin = Tk()
signin.geometry("600x400")
signin.title("Sign-in")
signin.configure(background="white")
userlbl=Label(signin,text="User Name",bg="white").place(x=20,y=20)
uservar=StringVar(signin)
userent=Entry(signin,textvariable=uservar).place(x=100,y=20)
passlbl=Label(signin,text="Password",bg="white").place(x=20,y=60)
passvar=StringVar(signin)
passent=Entry(signin,show="*",textvariable=passvar).place(x=100,y=60)
submit=Button(signin,text="Submit",command=authenticate).place(x=20, y=100)
submit=Button(signin,text="Cancel",command=signindestroy).place(x=110, y=100)
signin.mainloop()
    
