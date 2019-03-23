#PF-Assgn-36
'''
Created on Feb 26, 2019

@author: vijay.pal01
'''

def create_largest_number(number_list):
      number_list.sort(reverse=True)
      count=0
      new_number_list=[None]*1
      for i in range(0,len(number_list)):
          count = i
          new_number_list = str(number_list[i])
          count+=1
          new_number_list=print(new_number_list + (new_number_list+1))    
            
          
          
              
            
      return 1       
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)

