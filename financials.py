from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import data







def fetchdetails(sbaccvar,disprow):
    global trnsent
    for doc in data.db.subaccounts.find({"subaccountname":sbaccvar}):
        Label(trnsent,text=doc["mainaccountno"],bg="white").grid(row=disprow,column=0)
        Label(trnsent,text=doc["mainaccounttitle"],bg="white").grid(row=disprow,column=1)
        Label(trnsent,text=int(doc["subaccountno"]),bg="white").grid(row=disprow,column=2)



# Financials Portal
def finsptl(top,portallabel,b1,b2,b3,b4,b5):
    portallabel.config(text="Financials Portal",bg="#058DC7")
    portallabel.place(x=0,y=350)
    b3.place_forget()
    b1.config(text="Balance Sheet", width = 20, command=lambda :messagebox.showinfo("BS","Balance Sheet"))
    b1.place(x = 50, y = 450)
    b2.config(text="Bank Position", width = 20)
    b2.place(x = 287.5, y = 450)
    b4.config(text="Ledgers/ Accounts", width = 20, command=lambda :ldgrwin())
    b4.place(x = 887.5, y = 450)
    b5.config(text="Enter Transaction", width = 20,command=lambda :trnsent())
    b5.place(x = 1150, y = 450)

    # def ldgrwin():
    #     ldgrwin=Toplevel(bg="white")
    #     ldgrwin.geometry("400x400")
    #     ldgrwin.title("CAAEWMS ledgers")
    #     ldgrlbl=Label(ldgrwin,text="CAA Welfare Fund Ledgers",bg="white",fg="#058DC7",font=("Arial",15,"bold")).place(x=10,y=20)
        
    

    
    def trnsent():
        global trnsent
        counter=0
        rowvar=5
        colvar=0
        entdatalist=[]
        drcrlist=["Debit","Credit"]
        
        sbacctnmslist=[]
        for acc in data.db.subaccounts.find():
            sbacctnmslist.append(acc["subaccountname"])
        sbacctnmslist.sort()
        
        trnsent=Toplevel()
        trnsent.geometry("1366x768")
        trnsent.config(bg="white")
        trnsent.title("Enter Transaction")
        trnsentlbl=Label(trnsent,text="Enter new transaction in CAA Welfare Fund",bg="white",fg="#058DC7",font=("Arial",15,"bold"),pady=25).grid(row=0,column=0,columnspan=6)
        dtlbl=Label(trnsent,text="Date (DD/MM/YY) :",anchor="e",bg="white",font=("Arial",11,"bold"),width=25,pady=10).grid(row=2,column=4)
        dtvar=StringVar(trnsent)
        dtent=Entry(trnsent,textvariable=dtvar,bg="white",font=("Arial",11,"bold"),width=25).grid(row=2,column=5)
        mnaccnolbl=Label(trnsent,text="Main Account No",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=20,height=2).grid(row=3,column=0)
        mnaccnmlbl=Label(trnsent,text="Main Account Title",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=35,height=2).grid(row=3,column=1)
        sbaccnolbl=Label(trnsent,text="Sub Account No",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=20,height=2).grid(row=3,column=2)
        sbaccnmlbl=Label(trnsent,text="Sub Account Title",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=40,height=2).grid(row=3,column=3)
        amtlbl=Label(trnsent,text="Amount",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=28,height=2).grid(row=3,column=4)
        drcrlbl=Label(trnsent,text="Debit/Credit",bg="#058DC7",fg="white",font=("Arial",11,"bold"),width=30,height=2).grid(row=3,column=5)
        empspc=Label(trnsent,bg="white").grid(row=4,columnspan=6)
        while counter<=10:
            exec("global sbaccnmvar%d"%(counter))
            exec("sbaccnmvar%d=StringVar(trnsent)"%(counter))
            exec("sbaccnmvar%d.set(\"Select account name\")"%(counter))
            exec("sbaccnmmenu%d=OptionMenu(trnsent,sbaccnmvar%d,*sbacctnmslist,command=lambda sbaccnmvar%d:fetchdetails(sbaccnmvar%d,%d)).grid(row=rowvar+1,column=colvar+3)"%(counter,counter,counter,counter,rowvar+1))
            exec("global amtentvar%d"%(counter))
            exec("amtentvar%d=IntVar(trnsent)"%(counter))
            exec("amtent%d=Entry(trnsent,textvariable=amtentvar%d,justify=RIGHT).grid(row=rowvar+1,column=colvar+4)"%(counter,counter))
            exec("global drcrvar%d"%(counter))
            exec("drcrvar%d=StringVar(trnsent)"%(counter))
            exec("drcrmenu%d=OptionMenu(trnsent,drcrvar%d,*drcrlist).grid(row=rowvar+1,column=colvar+5)"%(counter,counter))
            exec("entdatalist.append([sbaccnmvar%d,amtentvar%d,drcrvar%d])"%(counter,counter,counter))
            Label(trnsent,text="",bg="white").grid(row=rowvar+2)
            counter+=1
            rowvar+=1
        submitbutton=Button(trnsent,text="Submit entry",width=40)
        submitbutton.grid(row=rowvar+4,column=2,columnspan=2)
    
    # submitbutton.grid_forget()
    
    #     global sbaccnmvar1
    #     sbaccnmvar1=StringVar(trnsent)
    #     sbaccnmvar1.set("Select Account Name")
    #     sbaccnmmenu1=OptionMenu(trnsent,sbaccnmvar1,*sbacctnmslist,command=lambda x:fetchdetails(sbaccnmvar1)).grid(row=7,column=3)
    #     global amtvar1
    #     amtvar1=IntVar(trnsent)
    #     amtent1=Entry(trnsent,textvariable=amtvar1,justify=RIGHT).grid(row=7,column=4)
    #     global drcrvar1
    #     drcrvar1=StringVar(trnsent)    
    #     drcrmenu1=OptionMenu(trnsent,drcrvar1,*sbacctnmslist).grid(row=7,column=5)
        
    #     submitbutton=Button(trnsent,text="Submit entry",width=40)
    #     submitbutton.grid(row=9,column=2,columnspan=2)
    #     trnsent.mainloop()

    # def fetchdetails(sbaccvar):
    #     global trnsent
    #     for doc in data.db.subaccounts.find({"subaccountname":sbaccvar.get()}):
    #         Label(trnsent,text=doc["mainaccountno"],bg="white").grid(row=7,column=0)
    #         Label(trnsent,text=doc["mainaccounttitle"],bg="white").grid(row=7,column=1)
    #         Label(trnsent,text=int(doc["subaccountno"]),bg="white").grid(row=7,column=2)

        
