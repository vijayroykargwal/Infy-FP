#OOPR-Assgn-15
'''
Created on Mar 7, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Parrot:
    __counter = 7000
    def __init__(self,name,color):
        self.__name = name
        Parrot.__counter+=1
        self.__unique_number = Parrot.__counter
        self.__color = color

    def get_name(self):
        return self.__name


    def get_unique_number(self):
        return self.__unique_number


    def get_color(self):
        return self.__color

p1 = Parrot("Bob","Green")
print(p1.get_name())
print(p1.get_unique_number())
print(p1.get_color())

  
        