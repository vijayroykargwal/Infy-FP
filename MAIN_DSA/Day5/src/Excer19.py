#DSA-Exer-19
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''


def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp = num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]= temp


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    minimum_value = min(num_list[start_index:])
    index = num_list.index(minimum_value)
    return index

def selection_sort(num_list):
    #Remove pass and implement the 
    #selection sort algorithm to sort 
    #the elements of num_list in ascending order
    for i in range(0,len(num_list)-1):
        swap(num_list, i, find_next_min(num_list, i))


#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)
