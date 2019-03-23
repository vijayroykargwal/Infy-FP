#PF-Prac-9
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def generate_dict(number):
    #start writing your code here
    new_dict = {}
    for i in range(number):
        new_dict.__setitem__(i+1, ((i+1)**2))
        

    
    return new_dict

number=20
print(generate_dict(number))