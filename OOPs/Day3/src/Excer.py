'''
Created on Mar 7, 2019

@author: vijay.pal01
'''
class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)