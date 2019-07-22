#OOPR-Exer-13
'''
Created on Mar 11, 2019

@author: vijay.pal01
'''

#Start writing your code here
from abc import ABCMeta, abstractclassmethod, abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter =101
    def __init__(self,consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter+=1

    def get_consumer_name(self):
        return self.__consumer_name


    def get_consumer_number(self):
        return self.__consumer_number

    @abstractmethod
    def calculate_monthly_rent(self):
        pass
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        if(self.get_base_pack_name()=="Silver" or 
           self.get_base_pack_name()=="Gold" or 
           self.get_base_pack_name()=="Platinum" ):
            return True
        else:
            self.__base_pack_name = "Silver"
            return  "Base package name is incorrect, set to Silver"
        
    def calculate_monthly_rent(self):
        if(self.get_subscription_period()>=1 and 
           self.get_subscription_period()<=24):
                monthly_rent = 0
                discount_amount = 0
                if(self.get_base_pack_name().lower()=="silver"):
                    monthly_rent = 350
                    if(self.get_subscription_period()>12):
                        discount_amount = 350
                elif(self.get_base_pack_name().lower()=="gold"):
                    monthly_rent = 440
                    if(self.get_subscription_period()>12):
                        discount_amount = 440
                elif(self.get_base_pack_name().lower()=="platinum"):
                    monthly_rent = 560
                    if(self.get_subscription_period()>12):
                        discount_amount = 560
                
                return (((monthly_rent*self.get_subscription_period())-
                         discount_amount)
                        /self.get_subscription_period())
        else:
            return -1
                    
                    
                    
        
        
        