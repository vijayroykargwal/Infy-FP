#PF-Prac-1
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def add_string(str1):
  #start writing your code here
    n=len(str1)
    if(n<3):
        return str1
    if(str1.endswith("ing")):
        str1+="ly"
    else:
        str1+="ing"
    return str1
        
    
      

  
    return str1

str1="com"
print(add_string(str1))