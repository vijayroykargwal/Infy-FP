#OOPR-Exer-1
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

                                                        
def purchase_mobile(price,brand):
    if  brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    return total_price
def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    return total_price


purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
print(purchase_mobile(20000,"Apple"))
print(purchase_shoe(200,"leather"))