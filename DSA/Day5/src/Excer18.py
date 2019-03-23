#DSA-Exer-18
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''


def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum 
    #element in a sub-list and return 
    #the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    minimum_value = min(num_list[start_index:])
    index = num_list.index(minimum_value)
    return index

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
print("Index of the next minimum element is",
       find_next_min(num_list,start_index))
