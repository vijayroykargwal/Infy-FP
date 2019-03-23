#DSA-Assgn-3
'''
Created on Mar 13, 2019

@author: vijay.pal01
'''


def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for i in list1:
        for j in list2:
            if(2*i==j):
                new_list.append(i)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))