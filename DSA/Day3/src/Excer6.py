#DSA-Exer-6
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''

                                            
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
        
            return data
    
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
                                        
   
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg


def find_average(num_list):
    #write your logic here
    sum1 = 0
    list1=[]
    for i in range(0,num_list.get_max_size()-1):
        list1.append(num_list.pop())
        sum1+=list1[i]
        
       
    average = sum1/(num_list.get_max_size()-1)
    
    list1 = list1[::-1]
    for i in range(0,num_list.get_max_size()-1):
        num_list.push(list1[i])
    num_list.push(average)
    return num_list

#Push different values to the stack and test your program
num_list=Stack(7)
num_list.push(78)
num_list.push(65)
num_list.push(92)
num_list.push(46)
num_list.push(89)
num_list.push(71)
new_stack=find_average(num_list)
new_stack.display()