#OOPR-Exer-7
'''
Created on Mar 7, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__ticket_id =None
        self.__source=source
        self.__destination = destination

    def get_passenger_name(self):
        return self.__passenger_name


    def get_ticket_id(self):
        return self.__ticket_id


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination


    
    def validate_source_destination(self):
        if(self.__source.lower()=="delhi" and
        (self.__destination.lower()=="mumbai" or
        self.__destination.lower()=="chennai" or 
        self.__destination.lower()=="pune" or 
        self.__destination.lower()=="kolkata")):
            return True
        else:
            return False
       
    def generate_ticket(self):
        if(self.__source.lower()=="delhi" and
        (self.__destination.lower()=="mumbai" or
        self.__destination.lower()=="chennai" or 
        self.__destination.lower()=="pune" or 
        self.__destination.lower()=="kolkata")):
            Ticket.counter+=1
            if(Ticket.counter<10):
                self.__ticket_id=self.__source.upper()[0]+self.__destination.upper()[0]+"0"+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source.upper()[0]+self.__destination.upper()[0]+str(Ticket.counter) 
            
            return self.get_ticket_id()
        
        

            
               
   
