#OOPR-Exer-8
'''
Created on Mar 7, 2019

@author: vijay.pal01
'''

class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,i1):
        
        #write the code to make the juggler juggle
        if(self.__name.lower()=="jack bremlov"  and i1.get_name().lower()=="knives"):
            return (Juggler.__name, " is juggling with ", i1.get_name)
        elif(self.__name.lower()=="anthony gatto" and i1.get_name().lower()=="balls"):
            return (Juggler.__name, " is juggling with ", i1.get_name)
        else:
            return -1   

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
j1 = Juggler("Jack Bremlov")
j2=Juggler("Anthony Gatto")
i1= JugglingItem("knives")
i2= JugglingItem("balls")

