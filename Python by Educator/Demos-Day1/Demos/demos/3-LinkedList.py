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
        
        
        #Remove pass and write the logic to add an element
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
        #Remove pass and write the logic to display the elements
        
#     def find_node(self,data):        Day2
#         temp=self.__head
#         while(temp is not None):
#             if(temp.get_data() == data):
#                 print("Data found")
#             temp=temp.get_next()

    def insert(self,data,data_before):
        new_node=Node(data)
        
        counter=0
        if(data_before is None):
            counter=1
            
            self.__head=new_node
            new_node.set_next(temp)
            if(temp.get_next() is None):                
                self.__tail=new_node
            
        else:
            temp=self.__head
            while(temp is not None):                
                if(temp.get_data() == data_before):
                    counter=1
                    new_node.set_next(temp.get_next())
                    temp.set_next(new_node)
                    if(new_node.get_next() is None):
                        self.__tail=new_node
                temp=temp.get_next()
        if(counter==0):
            print("No matching node found")
        else:
            print(list1)
        
        

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

list1=LinkedList()
list1.add("Sugar")
list1.add("Salt")
list1.add("Pepper")
print("Elements in the list:")
list1.display()
list1.insert("Red_Chilli", "Salt")
# list1.find_node("Pepper")

