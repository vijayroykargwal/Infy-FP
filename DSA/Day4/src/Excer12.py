'''
Created on Mar 18, 2019

@author: vijay.pal01
'''
#DSA-Tryout

import random

def find_it(num,element_list):
    no_of_guesses=0
    for i in element_list:
        no_of_guesses+=1
        if(i==num):
            print("Element Found")
            break;
        else:
            print("Element Not Found")
    return print(no_of_guesses)
    #Remove pass and copy the solution earlier written for this function here
    #Modify it, if required
   

def initialize_list_of_elements(n):
    #Modify the code to initialize the list of elements in ascending order
    #Try with descending order also
    list_of_elements=[]
    for i in range(n+1,1,-1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def play(n):
    #Remove pass and copy the solution earlier written for this function here
    element_list=initialize_list_of_elements(100)
    number = random.randrange(1,101)
    find_it(number, element_list)

#Pass different values to play() and observe the output
play(400)