#OOPR-Assgn-29
'''
Created on Mar 11, 2019

@author: vijay.pal01
'''
#Start writing your code here
from abc import ABCMeta, abstractmethod
class Customer(metaclass = ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None

    def get_customer_name(self):
        return self.__customer_name

    @abstractmethod
    def calculate_bill_amount(self):
        pass
    
class OccasionalCustomer(Customer):
    __counter= 1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.__counter += 1  
        self.bill_id = "O" + str(OccasionalCustomer.__counter)

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if(self.get_distance_in_kms()>=1 and self.get_distance_in_kms()<=5):
            return True
        else:
            return False
        
        
    def calculate_bill_amount(self):
        if(self.validate_distance_in_kms()==True):
            bill_amount = 50
            delivery_charge =0
            if(self.get_distance_in_kms()>=1 and self.get_distance_in_kms()<=2):
                delivery_charge = 5*self.get_distance_in_kms()
            elif(self.get_distance_in_kms()>2 and 
                 self.get_distance_in_kms()<=5):
                delivery_charge = 7.5*self.get_distance_in_kms()
            bill_amount += delivery_charge
            Customer.bill_amount = bill_amount
            return Customer.bill_amount
        else:
            Customer.bill_amount = -1
            return Customer.bill_amount
        
        
class RegularCustomer(Customer):
    __counter= 100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer.__counter+=1
        self.bill_id = "R" + str(RegularCustomer.__counter)

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    def validate_no_of_tiffin(self):
        if(self.get_no_of_tiffin()>=1 and self.get_no_of_tiffin()<=7):
            return True
        else:
            return False
        
        
    def calculate_bill_amount(self):
        if(self.validate_no_of_tiffin()==True):
            cost_per_tiffin = 50
            no_of_days = 7
            bill_amount = cost_per_tiffin*self.get_no_of_tiffin()*no_of_days
            Customer.bill_amount = bill_amount
            return Customer.bill_amount
        else:
            Customer.bill_amount = -1
            return Customer.bill_amount
        
        
    
        