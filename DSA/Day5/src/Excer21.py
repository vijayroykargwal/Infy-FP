#DSA-Exer-21
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''


def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low = 0
    high = len(num_list)-1
    if(low==high):
        return num_list
    else:
        mid = len(num_list)//2
        l_list = merge_sort(num_list[:mid])
        r_list= merge_sort(num_list[mid:])
        sorted_list = merge(l_list,r_list)
        return sorted_list
def merge(left_list,right_list):
    # Remove pass and write the logic to merge 
    #the elements in the left_list and right_list
    # and return the sorted list
    i = 0
    j = 0
    sorted_list = []
    while(i<(len(left_list)) and j<(len(right_list))):
        if(left_list[i]<=right_list[j]):
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    for x in left_list:
        if x not in sorted_list:
            sorted_list.append(x)
    for y in right_list:
        if y not in sorted_list:
            sorted_list.append(y)
    return sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
