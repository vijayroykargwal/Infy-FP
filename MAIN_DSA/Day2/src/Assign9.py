#DSA-Assgn-9
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''




from src.DataStructures import LinkedList

def reverse_linkedlist(reverse_list):
    #write your logic here
    list1 = []
    new_list = LinkedList()
    temp = reverse_list.get_head()
    while(temp is not None):
        list1.append(temp.get_data())
        temp = temp.get_next()
    reverse_list = list1[::-1]
    for i in range(0,len(reverse_list)):
        new_list.add(reverse_list[i])
    reverse_list = new_list   
    return reverse_list

#Add different values to the linked list and test your program

reverse_list=LinkedList()
reverse_list.add(10)
reverse_list.add(15)
reverse_list.add(14)
reverse_list.add(28)
reverse_list.add(30)
reversed_linkedlist=reverse_linkedlist(reverse_list)
reversed_linkedlist.display()