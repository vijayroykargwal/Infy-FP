#PF-Assgn-19
'''
Created on Feb 21, 2019

@author: vijay.pal01
'''


def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(distance_in_kms<=3 and distance_in_kms>0):
       if(food_type=='N' and quantity_ordered>=1):
           bill_amount = 150*quantity_ordered
       elif(food_type=='V' and quantity_ordered>=1):
            bill_amount = 120*quantity_ordered
       else:
            bill_amount = -1
    elif(distance_in_kms>3 and distance_in_kms<=6 and distance_in_kms>0):
         if(food_type=='N' and quantity_ordered>=1):
             bill_amount = 150*quantity_ordered + (distance_in_kms-3)*3
         elif(food_type=='V' and quantity_ordered>=1):
             bill_amount = 120*quantity_ordered + (distance_in_kms-3)*3
         else:
                bill_amount = -1
    elif(distance_in_kms>6 and distance_in_kms>0):
        if(food_type=='N' and quantity_ordered>=1):
            bill_amount = 150*quantity_ordered + (distance_in_kms-6)*6 + 9
        elif(food_type=='V' and quantity_ordered>=1):
            bill_amount = 120*quantity_ordered + (distance_in_kms-6)*6 + 9
        else:
            bill_amount = -1
    else:
        bill_amount = -1
        
    return bill_amount


bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)