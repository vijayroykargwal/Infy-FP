#OOPR-Exer-6
'''
Created on Mar 6, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Vehicle:
    def __init__(self):
        self.mileage = None
        self.fuel_left = None
    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left<=5):
            return 0
        else: 
            return (self.mileage)*((self.fuel_left)-5)
    def identify_distance_travelled(self,initial_fuel):
        return (initial_fuel-(self.fuel_left))*(self.mileage)
    
v1 = Vehicle()
v1.mileage = 75
v1.fuel_left = 8
print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(15))
