#OOPR-Assgn-5
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id =None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None

    def get_vehicle_id(self):
        return self.__vehicle_id


    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost


    def get_premium_amount(self):
        return self.__premium_amount


    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id


    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type = vehicle_type


    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost


    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount
    
    def calculate_premium(self):
        if(self.get_vehicle_type()=="Two Wheeler"):
            amount = 0.02*(self.get_vehicle_cost())
            self.set_premium_amount(amount)
            return self.get_premium_amount()
        elif(self.get_vehicle_type()=="Four Wheeler"):
            amount = 0.06*(self.get_vehicle_cost())
            self.set_premium_amount(amount)
            return self.get_premium_amount()
        else:
            return "Invalid Vehicle"
    def display_vehicle_details(self):
        return("Vehicle Type:"+self.get_vehicle_type()+
               "\tVehicle ID:"+self.get_vehicle_id()+"\tVehicle Cost:"+
               str(self.get_vehicle_cost())+"\tPremium Amount:"+
               str(self.get_premium_amount())) 
        
veh1 = Vehicle()
veh1.set_vehicle_type("Four Wheeler")
veh1.set_vehicle_id("RJ31-2930")
veh1.set_vehicle_cost(1000000)
veh1.calculate_premium()
print(veh1.display_vehicle_details())
          
    
