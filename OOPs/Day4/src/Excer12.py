#OOPR-Exer-12
'''
Created on Mar 8, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status = trained_status
        self.__experience = experience
    def rides_vehicle(self):
        if(self.__trained_status==True and self.__experience>0):
            return True
        else:
            return False
        
        
class CycleRider(Rider):
    def rides_blindfolded(self):
        if(self.__trained_status==True and self.__experience>0):
            return True
        else:
            return False

class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status, experience)
        self.__race_license = race_license
    
    def rides_in_dome(self):
        if(self.__trained_status==True and self.__experience>0 and 
           self.__race_license==True):
            return True
        else:
            return False

        
