#PF-Prac-10
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def string_both_ends(input_string):
    #start writing your code here
    n=len(input_string)
    if(n<2):
        input_string = -1
    elif(n>=2):
        input_string=input_string[:2]+input_string[-2:] 
    return input_string
input_string="w3w"
print(string_both_ends(input_string))