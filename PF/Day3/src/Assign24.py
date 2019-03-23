#PF-Assgn-24
'''
Created on Feb 22, 2019

@author: vijay.pal01
'''

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
      success="Triangle can be formed"
      failure="Triangle can't be formed"

      if(num3 < num1+num2 and num2 < num1+num3 and num1 < num2+num3):
          print(success)
          return success
      else:
         print(failure)
         return failure

    #Use the following messages to return the result wherever necessary
    
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=15
num2=11
num3=1
form_triangle(num1, num2, num3)