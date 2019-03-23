#PF-Assgn-34
'''
Created on Feb 26, 2019

@author: vijay.pal01
'''
from itertools import count

def find_pairs_of_numbers(num_list,n):
    count=0
    for i in range(0,len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j]==n):
                count+=1
     
    return count
              
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))