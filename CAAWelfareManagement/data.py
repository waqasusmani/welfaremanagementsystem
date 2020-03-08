from pymongo import MongoClient # import mongo client to connect  


# Creating instance of mongoclient  
client = MongoClient()  

# Creating database  
db = client.caaewms

# Collections
employeescol=db.employeescol
userpass=db.userpass
disbursement=db.disbursement
recovery=db.recovery
mainaccounts=db.mainaccounts
subaccounts=db.subaccounts
vouchers=db.vouchers

#Employee class
class Employee:
  def __init__(self, caano, name, designation, department, location,subaccnumber):
    self.caano = caano
    self.name = name
    self.designation=designation
    self.department=department
    self.location=location
    self.subaccnumber=subaccnumber

locations=['HQCAA','IIAP','JIAP','AIIAP','BKIAP','MIAP','FIAP','QIAP','Select later']

empmainaccount=mainaccounts.find({"accountnumber":11})
for document in empmainaccount:
  print(document)