#PF-Prac-37
'''
Created on Mar 21, 2019

@author: vijay.pal01
'''
def sum_of_list(num_list):
    if(len(num_list)!=0):
            lst = num_list
    else:
        return 0
        
        
    return lst[0] + sum_of_list(lst[1:])
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)