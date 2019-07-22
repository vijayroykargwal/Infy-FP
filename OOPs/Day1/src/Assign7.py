#OOPR-Assgn-7
'''
Created on Mar 5, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Instructor:
    def __init__(self):
        self.__instructor_name= None
        self.__technology_skill =None
        self.__experience = None
        self.__avg_feedback = None
    def get_instructor_name(self):
        return self.__instructor_name


    def get_technology_skill(self):
        return self.__technology_skill


    def get_experience(self):
        return self.__experience


    def get_avg_feedback(self):
        return self.__avg_feedback


    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name


    def set_technology_skill(self, technology_skill):
            self.__technology_skill=technology_skill


    def set_experience(self, experience):
        self.__experience = experience


    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback =avg_feedback
    def check_eligibility(self):
        if(self.get_experience()>3 and self.get_avg_feedback()>=4.5):
            return True
        elif(self.get_experience()<=3 and self.get_avg_feedback()>=4):
            return True
        else:
            return False
    def allocate_course(self,technology):
        s=self.check_eligibility()
        if(technology in self.__technology_skill and s ):
            return True
        else:
            return False

I1 = Instructor()
I1.set_instructor_name("Vijay")
I1.set_experience(3)
I1.set_avg_feedback(4)
I1.set_technology_skill(['C++','JAVA'])
I1.check_eligibility()
I1.allocate_course('C++')

