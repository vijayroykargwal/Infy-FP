#PF-Exer-22
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''


def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    airline = ["AI","BA"]
    source = ["Bangalore","Australia"]
    destination =["London","France"]
    count=101
    
    no_of_ticket =[None]*10 
    
    if(no_of_passengers<5 and airline=='AI'):
          
          for i in range(0,10):
              
             no_of_ticket[i]= count
             count +=1
          ticket_number_list = no_of_ticket
         
      
    else:
        count = count+9
        for i in range(0,5):
            
             no_of_ticket[i]= str(count)
             count -=1
       
          
        ticket_number_list = airline[0]+":"+source[0][0:3]+":"+destination[0][0:3]+":"+no_of_ticket[4] 
    return ticket_number_list
      
        
            
    
    #Use the below return statement wherever applicable
    

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))