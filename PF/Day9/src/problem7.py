#PF-Prac-7
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''
def seed_no(number,ref_no):
    #start writing your code here
    new_number=1
    temp=number
    while(temp!=0):
        remainder=temp%10
        new_number *= remainder
        temp = temp//10
        continue
    if(number*new_number==ref_no):
        return True
    return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))