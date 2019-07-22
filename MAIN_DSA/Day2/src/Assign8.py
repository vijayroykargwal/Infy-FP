#DSA-Assgn-8
'''
Created on Mar 15, 2019

@author: vijay.pal01
'''


#This assignment needs DataStructures.py file in your package, you can get it from resources page

from src.DataStructures import LinkedList

class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        pass
    def deallocate_table(self,table_number):
        pass
    #Implement other methods here

bakehouse=BakeHouse()
#Invoke the methods of BakeHouse class and test the program