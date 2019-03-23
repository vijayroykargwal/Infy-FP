#PF-Assgn-23
'''
Created on Feb 22, 2019

@author: vijay.pal01
'''

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    count=0
    #Write your logic here
    for i in range(0,len(gems_list)):
        for j in range(0,len(reqd_gems)):
            if(gems_list[i]==reqd_gems[j]):
                 bill_amount+=price_list[i]*reqd_quantity[j]
                 count+=1
                
    if(count==len(reqd_gems)):
        if(bill_amount>30000):
            return bill_amount*0.95
        else:
          return bill_amount
    return -1

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]


price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]


reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity)
print(bill_amount)