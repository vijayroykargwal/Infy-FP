#PF-Prac-31
'''
Created on Mar 21, 2019

@author: vijay.pal01
'''

def sum_of_elements(num_list,number):
    result_sum = 0
    new_num_list=[]
    for i in range(0,len(num_list)):
        if(num_list[i]==number):
            if(i==0):
                new_num_list.append(num_list[i])
                new_num_list.append(num_list[i+1])
                
            elif(i==len(num_list)-1):
                new_num_list.append(num_list[i])
                new_num_list.append(num_list[i-1])
                
            else:
                new_num_list.append(num_list[i-1])
                new_num_list.append(num_list[i])
                new_num_list.append(num_list[i+1])
                
                
    for i in new_num_list:
        if i in num_list:
            num_list.remove(i)    
    if(len(num_list)!=0):
        result_sum = sum(num_list)
    else:
        result_sum = 0
        
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))