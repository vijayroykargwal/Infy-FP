#OOPR-Assgn-25
'''
Created on Mar 8, 2019

@author: vijay.pal01
'''
#Start writing your code here
class FruitInfo:
    __fruit_name_list=["Apple","Guava","Orange","Grape","Sweet Lime"]
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            indx=FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[indx]
        else:
            return -1
                
        
        
        
        
class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__purchase_id ='P'+str(Purchase.__counter)
        Purchase.__counter+=1
    def get_purchase_id(self):
        return self.__purchase_id


    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        if(FruitInfo.get_fruit_price(self.__fruit_name)!=-1):
            price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
            price = price_per_kg*self.get_quantity()
            if(price_per_kg  == max(FruitInfo.get_fruit_price_list()) 
               and self.get_quantity()>1):
                price = 0.98*price
                if(self.__customer.get_cust_type()=="wholesale"):
                    price = 0.9*price
            elif(price_per_kg==min(FruitInfo.get_fruit_price_list()) 
                 and self.get_quantity()>=5):
                price = 0.95*price
                if(self.__customer.get_cust_type()=="wholesale"):
                    price = 0.9*price
            else:
                if(self.__customer.get_cust_type()=="wholesale"):
                    price = 0.9*price
            
            return price        
        else:
            return -1
                    
    
    
    
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name


    def get_cust_type(self):
        return self.__cust_type