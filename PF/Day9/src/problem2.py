#PF-Prac-2
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def bracket_pattern(input_str):
    #Remove pass and write your code here
    if(input_str.startswith(")") or input_str.endswith("(")):
        return False
    if(input_str.count("(")==input_str.count(")")):
        return True
    else:
        return False
        

    
input_str="(())("
print(bracket_pattern(input_str))