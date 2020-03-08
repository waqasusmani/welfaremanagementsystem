from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import data
import csv



# Employees Management Portal
def empmngtptl(top,portallabel,b1,b2,b3,b4,b5):
    portallabel.config(text="Employees Portal",bg="#058DC7")
    portallabel.place(x=0,y=350)
    b1.config(text="Add new employee", width = 20, command=lambda :newempwin())
    b1.place(x = 50, y = 450)
    b2.config(text="Delete employee", width = 20, command=lambda :delempwin())
    b2.place(x = 287.5, y = 450)
    # b3.config(text="List of employees", width = 20, command=lambda :listempwin())
    # b3.place(x = 587.75, y = 450)
    b4.config(text="List of employees", width = 20, command=lambda :listempwin())
    b4.place(x = 887.5, y = 450)
    b5.config(text="Employee information", width = 20, command=lambda :empinfowin())
    b5.place(x = 1150, y = 450)

    # New employee window
    def newempwin():
        newempwin=Toplevel(bg="white")
        newempwin.geometry("400x400")
        newempwin.title("CAAEWMS Add new employee")
        newemplbl=Label(newempwin,text="Add new employee to CAA Welfare Fund",bg="white",fg="#058DC7",font=("Arial",15,"bold")).place(x=10,y=20)
        caanolbl=Label(newempwin,text = "CAA No.",bg="white").place(x=10,y=70)
        global caanoentvar
        caanoentvar=IntVar(newempwin)
        caanoent = Entry(newempwin,textvariable=caanoentvar).place(x = 125, y = 70)
        namelbl=Label(newempwin,text = "Name",bg="white").place(x=10,y=100)
        global nameentvar
        nameentvar=StringVar(newempwin)
        nameent = Entry(newempwin,textvariable=nameentvar).place(x = 125, y = 100)
        desglbl=Label(newempwin,text = "Designation",bg="white").place(x=10,y=130)
        global desgentvar
        desgentvar=StringVar(newempwin)
        desgent = Entry(newempwin,textvariable=desgentvar).place(x = 125, y = 130)
        deptlbl=Label(newempwin,text = "Department",bg="white").place(x=10,y=160)
        global deptentvar
        deptentvar=StringVar(newempwin)
        deptent = Entry(newempwin,textvariable=deptentvar).place(x = 125, y = 160)
        loclbl=Label(newempwin,text = "Location",bg="white").place(x=10,y=200)
        global locvar
        locvar=StringVar(top)
        locvar.set('Select location')
        locmenu = OptionMenu(newempwin,locvar,*data.locations).place(x = 125, y = 200)
        submit=Button(newempwin,text="Submit",command=empadd).place(x=10,y=250)
        newempwin.mainloop()
    
    def empadd():
        subaccno=0
        for doc in data.mainaccounts.find({"accountnumber":11}):
            if doc["accountnumber"]<=10 and doc["lastsubaccno"]==0:
                subaccno=doc["accountnumber"]*100000+1
            elif doc["accountnumber"]>=10 and doc["lastsubaccno"]==0:
                subaccno=doc["accountnumber"]*10000+1
            else:
                subaccno=doc["lastsubaccno"]+1
        emp=data.Employee(caanoentvar.get(),nameentvar.get(),desgentvar.get(),deptentvar.get(),locvar.get(),subaccno)
        empdict={'CAA No': emp.caano, 'Name': emp.name, 'Designation': emp.designation, 'Department': emp.department, 'Location': emp.location, 'subaccountno':emp.subaccnumber}  
        data.employeescol.insert_one(empdict)
        data.subaccounts.insert_one({"mainaccountno":11,"mainaccounttitle":"Employees Accounts","subaccountno":subaccno,"subaccountname":"%d-%s"%(emp.caano,emp.name)})
        data.mainaccounts.update_one({"accountnumber":11},{"$set":{"lastsubaccno":subaccno}})
        messagebox.showinfo("Employee added","%s added to %s"%(emp.name,emp.location))
    # Delete employee window
    def delempwin():
        delempwin=Toplevel(bg="white")
        delempwin.geometry("600x600")
        delempwin.title("CAAEWMS Delete employee")
        delbl=Label(delempwin,text="Delete employee from CAAEEMS",pady=25,bg="white",fg="#058DC7",font=("Arial",15,"bold")).pack()
        empspc1=Label(delempwin,bg="white").pack()
        global caanovar
        caanovar = IntVar(delempwin)
        caanovar.set('Select CAA no. from list')
        caanos=[]
        for document in data.db.employeescol.find():
            caanos.append(document["CAA No"])
            caanos.sort()
        global empmenu
        empmenu = OptionMenu(delempwin,caanovar,*caanos,command=nameemptodel).pack()
        empspc2=Label(delempwin,bg="white").pack()
        global empnamevar
        empnamevar = StringVar(delempwin)
        empnamevar.set("No employee selected")
        empname = Label(delempwin,textvariable=empnamevar,bg="white").pack()
        empspc3=Label(delempwin,bg="white").pack()
        delbut=Button(delempwin,text="Press to delete selected employee",font=("bold"),fg="red",command=delempfn).pack()
        empspc4=Label(delempwin,bg="white").pack()
        warning=Label(delempwin,text="Warning! All the record of the selected employee will be permanently deleted", font=("bold"),fg="red",bg="white").pack()
        delempwin.mainloop()
        
    def nameemptodel(event):
        for document in data.db.employeescol.find():
            if document["CAA No"]==caanovar.get():
                empnamevar.set(document["Name"])
        
    def delempfn():
        data.db.employeescol.delete_one({"CAA No":caanovar.get()})
        messagebox.showinfo("x","%s deleted"%(empnamevar.get()))

    # List of employees window    
    def listempwin():
        listempwin=Toplevel(bg="white")
        listempwin.geometry("1366x768")
        listempwin.title("CAAEWMS List of Employees")
        listlabel=Label(listempwin,text="CAA Welfare Fund List of Employees",background="white",pady=25,fg="#058DC7",font=("Arial",15,"bold")).grid(row=0,column=0,columnspan=6)
        caanolabel=Label(listempwin,text="CAA No",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=25).grid(row=3,column=0)
        namelabel=Label(listempwin,text="Name",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=28).grid(row=3,column=1)
        desglabel=Label(listempwin,text="Designation",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=28).grid(row=3,column=2)
        deptlabel=Label(listempwin,text="Department",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=28).grid(row=3,column=3)
        loclabel=Label(listempwin,text="Location",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=28).grid(row=3,column=4)
        oslabel=Label(listempwin,text="Total outstanding",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=30).grid(row=3,column=5)
        row=4
        dictlist=[]
        for document in data.db.employeescol.find():
            dictlist.append(document)
        dictlist=sorted(dictlist,key=lambda i: i["CAA No"])
        print(dictlist)
        for dict in dictlist:    
            Label(listempwin,text=dict["CAA No"],background="white").grid(row=row,column=0)
            Label(listempwin,text=dict["Name"],background="white").grid(row=row,column=1)
            Label(listempwin,text=dict["Designation"],background="white").grid(row=row,column=2)
            Label(listempwin,text=dict["Department"],background="white").grid(row=row,column=3)
            Label(listempwin,text=dict["Location"],background="white").grid(row=row,column=4)
            disbamt=0
            for disb in data.db.disbursement.find({"CAA No":dict["CAA No"]}):
                disbamt+=disb["Disbursement"]
            recamt=0
            for rec in data.db.recovery.find({"CAA No":dict["CAA No"]}):
                recamt+=rec["Recovery"]    
            Label(listempwin,text=disbamt-recamt,background="white").grid(row=row,column=5)
            row+=1

    # Disbursement entry window
    def entdisbwin():
        entdisbwin=Toplevel(bg="white")
        entdisbwin.geometry("600x600")
        entdisbwin.title("CAAEWMS Enter Disbursement")
        entdisblbl=Label(entdisbwin,text="Enter New Disbursement Here",bg="white",pady=20,fg="#058DC7",font=("Arial",15,"bold")).place(x=10,y=10)
        disbdtlbl=Label(entdisbwin,text="Date of disbursement:",bg="white").place(x=10,y=80)
        disbdtfmtlbl=Label(entdisbwin,text="(DD/MM/YYYY)",bg="white").place(x=370,y=80)
        global disbdtstr
        disbdtstr=StringVar(entdisbwin)
        disbdtent=Entry(entdisbwin,textvariable=disbdtstr).place(x=200,y=80)
        disbcaanolbl=Label(entdisbwin,text="CAA No:",bg="white").place(x=10,y=140)
        global disbcaanovar
        disbcaanovar=IntVar(entdisbwin)
        disbcaanovar.set('Select CAA no. from list')
        disbcaanos=[]
        for document in data.db.employeescol.find():
            disbcaanos.append(document["CAA No"])
            disbcaanos.sort()
        global disbcaanosmenu
        disbcaanosmenu = OptionMenu(entdisbwin,disbcaanovar,*disbcaanos,command=nameemptodisb).place(x=200,y=140)
        global disbempnamevar
        disbempnamevar = StringVar(entdisbwin)
        disbempnamevar.set("No employee selected")
        disbempname = Label(entdisbwin,textvariable=disbempnamevar,bg="white").place(x=200,y=190)
        disbamtlbl=Label(entdisbwin,text = "Amount disbursed:",bg="white").place(x=10,y=260)
        global disbamtvar
        disbamtvar=IntVar(entdisbwin)
        disbamtent = Entry(entdisbwin,textvariable=disbamtvar).place(x=200,y=260)
        disbpartlbl=Label(entdisbwin,text="Particulars:",bg="white").place(x=10,y=330)
        global disbpartvar
        disbpartvar=StringVar(entdisbwin)
        disbpartent=Entry(entdisbwin,textvariable=disbpartvar,justify=LEFT).place(height=150,width=700,x=200,y=330)
        disbsubmitbtn=Button(entdisbwin,text="Submit",font=("bold"),fg="black",command=entdisbfn).place(x=200,y=500)

    def nameemptodisb(event):
        for document in data.db.employeescol.find():
            if document["CAA No"]==disbcaanovar.get():
                disbempnamevar.set(document["Name"])
    
    def entdisbfn():
        dayvar=int(disbdtstr.get()[0]+disbdtstr.get()[1])
        monthvar=int(disbdtstr.get()[3]+disbdtstr.get()[4])
        yearvar=int(disbdtstr.get()[6]+disbdtstr.get()[7]+disbdtstr.get()[8]+disbdtstr.get()[9])
        datevar=(yearvar,monthvar,dayvar)
        data.db.disbursement.insert_one({"Date":datevar,"CAA No":disbcaanovar.get(),"Particulars":disbpartvar.get(),"Disbursement":disbamtvar.get()})
        messagebox.showinfo("Disbursement recorded","Disbursement of %d recorded successfully against %s"%(disbamtvar.get(),disbempnamevar.get()))

    # Recovery entry window
    def entrecwin():
        entrecwin=Toplevel(bg="white")
        entrecwin.geometry("600x600")
        entrecwin.title("CAAEWMS Enter Recovery")
        entreclbl=Label(entrecwin,text="Enter New Recovery Here",bg="white",pady=20,fg="#058DC7",font=("Arial",15,"bold")).place(x=10,y=10)
        recdtlbl=Label(entrecwin,text="Date of recovery:",bg="white").place(x=10,y=80)
        recdtfmtlbl=Label(entrecwin,text="(DD/MM/YYYY)",bg="white").place(x=370,y=80)
        global recdtstr
        recdtstr=StringVar(entrecwin)
        recdtent=Entry(entrecwin,textvariable=recdtstr).place(x=200,y=80)
        reccaanolbl=Label(entrecwin,text="CAA No:",bg="white").place(x=10,y=140)
        global reccaanovar
        reccaanovar=IntVar(entrecwin)
        reccaanovar.set('Select CAA no. from list')
        reccaanos=[]
        for document in data.db.employeescol.find():
            reccaanos.append(document["CAA No"])
            reccaanos.sort()
        global reccaanosmenu
        reccaanosmenu = OptionMenu(entrecwin,reccaanovar,*reccaanos,command=nameemptorec).place(x=200,y=140)
        empspc1=Label(entrecwin,bg="white",height=1).pack()
        global recempnamevar
        recempnamevar = StringVar(entrecwin)
        recempnamevar.set("No employee selected")
        recempname = Label(entrecwin,textvariable=recempnamevar,bg="white").place(x=200,y=190)
        recamtlbl=Label(entrecwin,text = "Amount recovered:",bg="white",pady=5).place(x=10,y=260)
        global recamtvar
        recamtvar=IntVar(entrecwin)
        recamtent = Entry(entrecwin,textvariable=recamtvar).place(x=200,y=260)
        recpartlbl=Label(entrecwin,text="Particulars:",bg="white").place(x=10,y=330)
        global recpartvar
        recpartvar=StringVar(entrecwin)
        recpartent=Entry(entrecwin,textvariable=recpartvar,justify=LEFT).place(height=150,width=700,x=200,y=330)
        recsubmitbtn=Button(entrecwin,text="Submit",font=("bold"),fg="black",command=entrecfn).place(x=200,y=500)

    def nameemptorec(event):
        for document in data.db.employeescol.find():
            if document["CAA No"]==reccaanovar.get():
                recempnamevar.set(document["Name"])
    
    def entrecfn():
        dayvar=int(recdtstr.get()[0]+recdtstr.get()[1])
        monthvar=int(recdtstr.get()[3]+recdtstr.get()[4])
        yearvar=int(recdtstr.get()[6]+recdtstr.get()[7]+recdtstr.get()[8]+recdtstr.get()[9])
        datevar=(yearvar,monthvar,dayvar)
        data.db.recovery.insert_one({"Date":datevar,"CAA No":reccaanovar.get(),"Particulars":recpartvar.get(),"Recovery":recamtvar.get()})
        messagebox.showinfo("Recovery recorded","Recovery of %d recorded successfully against %s"%(recamtvar.get(),recempnamevar.get()))