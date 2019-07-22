'''
Created on Mar 18, 2019

@author: vijay.pal01
'''
#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    no_of_guesses=0
    for i in element_list:
        no_of_guesses+=1
        if(i==num):
            print("Element Found")
            break;
        else:
            print("Element Not Found")
    return (no_of_guesses)

def find_it_binary(num,element_list):
    #remove pass and copy the code written earlier for binary search
    no_of_guesses=0
    while(1):
        sorted(element_list)
        no_of_guesses+=1
        n = len(element_list)
        mid = n//2
        if(num==element_list[mid-1]):
            break
        elif(num>element_list[mid]):
            element_list=element_list[mid:n]
        elif(num<element_list[mid]):
            element_list=element_list[0:mid]
        continue
    return (no_of_guesses)

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    start=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
    end=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end-start)))

#Pass different values to play() and observe the output
play(40000)