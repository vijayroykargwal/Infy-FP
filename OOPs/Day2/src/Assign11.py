#OOPR-Assgn-11
'''
Created on Mar 6, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
    def get_flower_name(self):
        return self.__flower_name


    def get_price_per_kg(self):
        return self.__price_per_kg


    def get_stock_available(self):
        return self.__stock_available


    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name.upper()


    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg


    def set_stock_available(self, stock_available):
        self.__stock_available =stock_available
    def validate_flower(self):
        if(self.get_flower_name()=="ORCHID" or 
           self.get_flower_name()=="ROSE" or 
           self.get_flower_name()=="JASMINE"):
            return True
        else:
            return False
    def validate_stock(self,required_quantity):
        if(required_quantity<=self.get_stock_available()):
            return True
        else:
            return False
    def sell_flower(self,required_quantity):
        if((self.get_flower_name()=="ORCHID" or self.get_flower_name()=="ROSE" 
            or self.get_flower_name()=="JASMINE") and 
           (required_quantity<self.get_stock_available())):
            self.set_stock_available(
            self.get_stock_available()-required_quantity)
            return self.get_stock_available()
        
    def check_level(self):
        if(self.get_flower_name()=="ORCHID"):
            if(self.get_stock_available()<15):
                return True
            else:
                return False
        elif(self.get_flower_name()=="ROSE"):
            if(self.get_stock_available()<25):
                return True
            else:
                return False
        elif(self.get_flower_name()=="JASMINE"):
            if(self.get_stock_available()<40):
                return True
            else:
                return False
        else:
            return False
            
