'''
Created on Mar 18, 2019

@author: vijay.pal01
'''
#DSA-Tryout
import random
def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
    
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
    return print(no_of_guesses)
     
#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    element_list=initialize_list_of_elements(n)
    number = random.randrange(1,n+1)
    find_it(number, element_list)


#Pass different values to play() and observe the output
play(400)