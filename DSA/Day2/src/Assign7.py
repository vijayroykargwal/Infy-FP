#DSA-Assgn-7
'''
Created on Mar 14, 2019

@author: vijay.pal01
'''

from src.DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    #write your logic here
    list1=[]
    new_list = LinkedList()
    temp = duplicate_list.get_head()
    while(temp is not None):
        list1.append(temp.get_data())
        temp = temp.get_next()
    set1 = set(list1)
    duplicate_list = list(set1)
    duplicate_list = sorted(duplicate_list)
    for i in range(0,len(duplicate_list)):
        new_list.add(duplicate_list[i])
    duplicate_list = new_list   
    return duplicate_list

#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
print(remove_duplicates(duplicate_list))