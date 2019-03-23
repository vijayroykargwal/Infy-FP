'''
Created on Mar 14, 2019

@author: vijay.pal01
'''
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
def fun(prv,nxt,data):
    if(nxt==None):
        return
    if(nxt.get_data()==data):
        global sample
        sample.add(data)
        prv.set_next(nxt.get_next())
        return
    else:
        fun(nxt,nxt.get_next(),data)

sample=LinkedList()
sample.add(10)
sample.add(20)
sample.add(5)
sample.add(55)
sample.add(38)
sample_head=sample.get_head()

fun(sample_head, sample_head,5)
print(sample_head.get_next().get_next().get_next().get_next().get_next().get_data())