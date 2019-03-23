#PF-Prac-8
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''
def calculate_net_amount(trans_list):
    #start writing your code here
    a = 0
    for i in trans_list:
        if(i.startswith("D")):
            a+=int(i[2:])
        if(i.startswith("W")):
            a-=int(i[2:])
    net_amount = a
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))