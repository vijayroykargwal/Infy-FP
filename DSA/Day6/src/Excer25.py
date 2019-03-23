#DSA-Exer-25
'''
Created on Mar 20, 2019

@author: vijay.pal01
'''
from cherrypy._cpcompat import xrange


def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    #Remove pass and write your logic here
    new_list=[]
    i = 0
    for j in range(1,len(finish_time_list)):
        if(start_time_list[j]>=finish_time_list[i]):
            new_list.append(activity_list[i])
            i=j
        
   
#Pass different values to the function and test your program
activity_list=[11, 12, 32, 44, 53, 62]
start_time_list=[12, 14, 21, 31, 16, 18]
finish_time_list=[20, 16, 25, 35, 17, 20]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)