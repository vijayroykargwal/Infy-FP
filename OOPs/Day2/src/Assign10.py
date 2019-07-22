#OOPR-Assgn-10
'''
Created on Mar 6, 2019

@author: vijay.pal01
'''


class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration=duration
        self.__call_type= call_type
        

class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            list1=i.split(",")
            self.list_of_call_objects.append(CallDetail(list1[0],
                    list1[1],list1[2],list1[3]))

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)