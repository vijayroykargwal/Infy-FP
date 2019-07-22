#DSA-Assgn-13
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''




from src.DataStructures import Stack

def change_smallest_value(number_stack):
    #write your logic here
    list1 = []
    while(not(number_stack.is_empty())):
        a = number_stack.pop()
        list1.append(a)
    min_value = min(list1)
    
    for i in range(0,list1.count(min_value)):
        list1.remove(min_value)
        number_stack.push(min_value)
    for i in list1[::-1]:
        number_stack.push(i)

    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()