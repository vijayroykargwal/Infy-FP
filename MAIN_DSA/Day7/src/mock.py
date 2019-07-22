#DSA-Assgn-302
'''
Created on Mar 24, 2019

@author: vijay.pal01
'''

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import Queue,Stack

def queue_ordering(input_queue,input_stack):
    #Do not modify the size of output_queue
    output_queue=Queue(input_queue.get_max_size())
    list1=[]
    list2=[]
    while(not(input_queue.is_empty())):
        list1.append(input_queue.dequeue())
    while(not(input_stack.is_empty())):
        list2.append(input_stack.pop())
    i=0
    while(i<len(list2)):
        if(list2[i]==1):
            list1.append(list1[0])
            list1.pop(0)
            print(list1)
        elif(list2[i]==2):
            list1.insert(0, list1[-1])
            list1.pop(-1)
        i=i+1
    for i in list1:
        output_queue.enqueue(i)  
    #Write your code here
    return output_queue

#You may modify the below code for testing
input_stack=Stack(4)
input_stack.push(2)
input_stack.push(1)
input_stack.push(2)
input_stack.push(1)


input_queue=Queue(5)
input_queue.enqueue('X')
input_queue.enqueue('a')
input_queue.enqueue('b')
input_queue.enqueue('c')

output_queue=queue_ordering(input_queue, input_stack)
output_queue.display()