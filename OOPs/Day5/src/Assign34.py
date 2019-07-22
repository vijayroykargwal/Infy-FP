#OOPR-Assgn-34
'''
Created on Mar 13, 2019

@author: vijay.pal01
'''

class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False
#Implement the class here