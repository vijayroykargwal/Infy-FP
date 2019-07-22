#OOPR-Exer-4
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def set_name(self, name):
          self.__name = name
    
    def set_gender(self, gender):
          self.__gender = gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender

    
    
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")    
    
    
e1 = Athlete("Maria","girl")
e1.running()

