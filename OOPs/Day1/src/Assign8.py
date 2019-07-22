#OOPR-Assgn-8
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None
    def get_student_id(self):
        return self.__student_id


    def get_age(self):
        return self.__age


    def get_marks(self):
        return self.__marks


    def set_student_id(self, student_id):
        self.__student_id = student_id


    def set_age(self, age):
        self.__age = age


    def set_marks(self, marks):
        self.__marks = marks
        
    def validate_marks(self):
        if(self.get_marks()>=0 and self.get_marks()<=100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.get_age()>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.get_marks()>=0 and self.get_marks()<=100 and self.get_age()>20):
            if(self.get_marks()>=65):
                return True
            else:
                return False
        else:
            return False
        
s1 = Student()
s1.set_student_id(167)
s1.set_age(22)
s1.set_marks(74)
s1.validate_marks()
s1.validate_age()
s1.check_qualification()        
        

    
