'''
Created on Mar 11, 2019

@author: vijay.pal01
'''
class VehicleService:
    def __init__(self,mechanic_list):
        self.__mechanic_list = mechanic_list
    def  assign_vehicle_for_service(self,mechanic_id,vehicle_type):
        if(mechanic_id>=101 and mechanic_id<=105):
            if(vehicle_type == Mechanic.get_specialization()):
                Vehicle.set_vehicle_count()=101
        else:
            raise InvalidMechanicIdException
        
            
        
class Mechanic:
    def __init__(self,mechanic_id,specialization,vehicle_count):
        self.__mechanic_id =mechanic_id
        self.__specialization = specialization
        self.__vehicle_count = vehicle_count
    def get_mechanic_id(self):
        return self.__mechanic_id


    def get_specialization(self):
        return self.__specialization


    def get_vehicle_count(self):
        return self.__vehicle_count


    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id


    def set_specialization(self, specialization):
        self.__specialization = specialization


    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count
        
        
class InvalidMechanicIdException(Exception):
        print("Invalid ID")
class InvalidMechanicSpecializationException(Exception):
        print("Invalid Mechanic Specialization")
    

    