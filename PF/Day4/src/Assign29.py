#PF-Assgn-29
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''

def calculate(distance,no_of_passengers):
    
    
    
    total_fuel_price = 70 *(distance/10)
    total_ticket_price = 80 * (no_of_passengers)
    profit = total_ticket_price - total_fuel_price
    if(profit>=0):
        return profit
    else:
        return -1 
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=1
no_of_passengers=1
print(calculate(distance,no_of_passengers))