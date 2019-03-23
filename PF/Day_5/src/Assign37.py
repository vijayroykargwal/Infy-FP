#PF-Assgn-37
'''
Created on Feb 26, 2019

@author: vijay.pal01
'''

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

child_id=(10,20,30,40,50)
child_id_list=list(child_id)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    
    total_chocolates=sum(chocolates_received)
    
    return total_chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    
    
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
         
    elif(child_id_rewarded not in child_id):
            print("Child id is invalid")
            
    else:
        for i in range(0,len(child_id_list)):
                if(child_id_list[i]==child_id_rewarded):
                    chocolates_received[i]=chocolates_received[i]+extra_chocolates
                    return chocolates_received



print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)