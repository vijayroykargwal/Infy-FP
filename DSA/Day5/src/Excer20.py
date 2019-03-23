#DSA-Exer-20
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''

def swap(num_list, first_index, second_index):
    #Remove pass and copy the code earlier written for this function
    temp = num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]= temp

def find_next_min(num_list,start_index):
    #Remove pass and copy the code earlier written for this function
    minimum_value = min(num_list[start_index:])
    index = num_list.index(minimum_value)
    return index

def selection_sort(num_list):
    #Remove pass and copy the code earlier written for this function
    #Modify it to return the total number 
    #of passes the algorithm has gone through to sort the list
    no_of_passes = 0
    for i in range(0,len(num_list)-1):
        no_of_passes+=1
        swap(num_list, i, find_next_min(num_list, i))
    return no_of_passes

def bubble_sort(num_list):
    total_no_of_passes=0
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        total_no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2]>num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped=True;
        if(swapped==False):
            break
    return total_no_of_passes

num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]
print("Selection Sort - No. of passes:",selection_sort(num_list))

num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]
print("Bubble Sort - No. of passes:",bubble_sort(num_list))
