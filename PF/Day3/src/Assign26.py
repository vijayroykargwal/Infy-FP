#PF-Assgn-26
'''
Created on Feb 22, 2019

@author: vijay.pal01
'''
from builtins import int


def solve(heads,legs):
      error_msg="No solution"
      chicken_count=0
      rabbit_count=0
      if(heads>0 and legs>0 and legs>heads):
         rabbit_count = (legs - 2 * heads)
         rabbit_count = rabbit_count//2
         chicken_count = heads - rabbit_count 
         if((rabbit_count+chicken_count)==heads):
             if((4*rabbit_count+2*chicken_count)==legs):
                 return print( chicken_count, rabbit_count)
             else:
                  return print(error_msg)
         else:
             return print(error_msg)
      else:
              return print(error_msg)
     
     
          
      
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(23,67)