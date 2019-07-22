'''
Created on Mar 13, 2019

@author: vijay.pal01
'''
class Customer:
    def __init__(self,customer_id, customer_name, age, account):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__age = age
        self.__account = account

    def get_customer_id(self):
        return self.__customer_id


    def get_customer_name(self):
        return self.__customer_name


    def get_age(self):
        return self.__age


    def get_account(self):
        return self.__account

    def take_card(self):
        pass
        
    def withdraw_amount(self,amount):
        pass
    
    
class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance

    def get_account_type(self):
        return self.__account_type


    def get_balance(self):
        return self.__balance


    def get_min_balance(self):
        return self.__min_balance


    def set_balance(self, value):
        self.__balance = value

class PriviligedCustomer(Customer):
    def __init__ (self,customer_id, customer_name, age, account, bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.__bonus_points = bonus_points

    def get_bonus_points(self):
        return self.__bonus_points

    def withdraw_amount(self):
        pass
    def increase_bonus(self):
        pass
        
    