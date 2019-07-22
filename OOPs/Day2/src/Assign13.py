#OOPR-Assgn-13
'''
Created on Mar 6, 2019

@author: vijay.pal01
'''

#Start writing your code here
class Classroom:
    classroom_list = None
    @staticmethod
    def search_classroom(class_room):
        for i in Classroom.classroom_list:
            if (class_room.upper() == i.upper()):
                return 'Found'
        else:
            return -1         