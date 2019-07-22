'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

class Product:
    def _init_(self):
       self.product_id = None
       self.product_name= None
tea_powder = Product()
tea_powder.product_name ="Tea"
tea_powder.product_id = 1001
milk = Product()
milk.product_name= "milk"
milk.product_id=1002

# class Employee:
#     def _init_(self):
#         self.emp_id= None
#         self.emp_name = None
#         self.salary = None
#         
#     def calculate_salary(self, no_of_LOP):
#         r= (20-no_of_LOP)*1000
#         self.salary = r
# 
# e1 = Employee()
# e1.calculate_salary(3)
# print("Salary",e1.salary)


class Customer:
    def __init__(self,id1):
        self.id = id1

c1=Customer(200)
print(c1.id)


class Employee:

    def get_salary(self):
        return self.__salary


    def set_salary(self, value):
        self.__salary = value


    def get_emp_id(self):
        return self.__emp_id


    def get_emp_name(self):
        return self.__emp_name


    


    def set_emp_id(self, value):
        self.__emp_id = value


    def set_emp_name(self, value):
        self.__emp_name = value


    

    def _init_(self):
        self.__emp_id= None
        self.__emp_name = None
        self.__salary = None
        
    def calculate_salary(self, no_of_LOP):
        r= (20-no_of_LOP)*1000
        self.__salary = r
    emp_id = property(get_emp_id, set_emp_id, None, None)
    emp_name = property(get_emp_name, set_emp_name, None, None)
    salary = property(get_salary, set_salary, None, None)
    salary = property(get_salary, set_salary, None, None)

e1 = Employee()
e1.calculate_salary(3)
print("Salary",e1.salary)