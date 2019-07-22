#OOPR-Assgn-3
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = None
    def purchases(self):
        bill_amount = self.bill_amount
        amount = 0.95*bill_amount
        return amount
    def pays_bill(self,amount):
        return( self.customer_name, "pays bill amount of Rs.",amount)
    
c1 = Customer()
c1.customer_name = "Vijay"
c1.bill_amount = 5000
print(c1.pays_bill(c1.purchases()))