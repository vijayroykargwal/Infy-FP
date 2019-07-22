#DSA-Assgn-11
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''
from src.DataStructures import Queue

def merge_queue(queue1,queue2):
    #write your logic here
    queue_size = queue1.get_max_size()+queue2.get_max_size()
    merged_queue = Queue(queue_size)
    for i in range(0,queue_size):
        a = queue1.dequeue()
        if(a is not None):
            merged_queue.enqueue(a)
        b = queue2.dequeue()
        if(b is not None):
            merged_queue.enqueue(b)
    
    return merged_queue

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()