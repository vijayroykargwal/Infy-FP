#DSA-Assgn-26
'''
Created on Mar 20, 2019

@author: vijay.pal01
'''
def count_strings(number):
    #Remove pass and write your logic here
    a=[0 for i in range(number)] 
    b=[0 for i in range(number)] 
    a[0] = b[0] = 1
    for i in range(1,number): 
        a[i] = a[i-1] + b[i-1] 
        b[i] = a[i-1] 
    return a[number-1] + b[number-1] 

#Pass different values to the function and test your program
number=3
print("The number of strings that can be made are:",count_strings(number))