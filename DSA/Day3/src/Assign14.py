#DSA-Assgn-14
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''
from src.DataStructures import Queue

def check_numbers(number_queue):
    #write your logic here

    new_queue = Queue(number_queue.get_max_size())
    while(not(number_queue.is_empty())):
        pop = number_queue.dequeue()
        count = 0
        for x in range (1,11):
            if(pop%x == 0):
                count+=1
        if(count == 10):
            new_queue.enqueue(pop)
    return new_queue

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)