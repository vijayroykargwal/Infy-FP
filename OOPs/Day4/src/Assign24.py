#OOPR-Assgn-24
'''
Created on Mar 8, 2019

@author: vijay.pal01
'''
#Start writing your code here
class Apparel:
    counter=100
    def __init__(self,price,item_type):
        Apparel.counter+=1
        self.__item_id= Apparel.counter
        self.__price=price
        self.__item_type=item_type
        if(self.get_item_type()=="Cotton"):
            self.__item_id = "C"+str(Apparel.counter)
        elif(self.get_item_type()=="Silk"):
            self.__item_id = "S"+str(Apparel.counter)
            
            

    def get_item_id(self):
        return self.__item_id


    def get_price(self):
        return self.__price


    def get_item_type(self):
        return self.__item_type

    def calculate_price(self):
        self.__price = 1.05*self.get_price() 
        
    def set_price(self,price):
        self.__price= price

class Cotton(Apparel):
    def __init__(self,price,discount):
        self.__discount= discount
        super().__init__(price,"Cotton")
        
        

    def get_discount(self):
        return self.__discount

    def calculate_price(self):
        super().calculate_price()
        price=1.05*(self.get_price()-(self.get_discount()/100)*self.get_price())
        self.set_price(price)
        
class Silk(Apparel):
    def __init__(self,price):
        self.__points=None
        super().__init__(price, "Silk")
        Apparel.counter+=1
        

    def get_points(self):
        return self.__points

    def calculate_price(self):
        super().calculate_price()
        if(self.get_price()>10000):
            self.__points = 10
        elif(self.get_price()<=10000):
            self.__points = 3
        price = 1.1*(self.get_price())
        self.set_price(price)
        
            
    
        
        