#PF-Assgn-22
'''
Created on Feb 22, 2019

@author: vijay.pal01
'''

def find_leap_years(given_year):

    # Write your logic here
     
     list_of_leap_years = [None]*15
     
     if(given_year>0):
         
         for i in range(0,15):
             while(not(given_year%4==0 and given_year%100!=0 or given_year%400==0)):
                 given_year = given_year+1
                 
               
             list_of_leap_years[i]=given_year
             while(given_year%4==0 and given_year%100!=0 or given_year%400==0):
                 given_year = given_year+1
             continue
         
         
         return list_of_leap_years
         
             
            
       
              

list_of_leap_years=find_leap_years(1684)
print(list_of_leap_years)