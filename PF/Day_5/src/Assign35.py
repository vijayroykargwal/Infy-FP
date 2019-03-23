#PF-Assgn-35
'''
Created on Feb 26, 2019

@author: vijay.pal01
'''


#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
list_of_marks=list(list_of_marks)
average=0
count=0
def find_more_than_average():
    
    for i in list_of_marks:
        average= (i+(i-1))/2
    for i in range(0,len(list_of_marks)):
        
        if(list_of_marks[i]>average):
            
            list_of_marks[i]=count
            count+=1
        
        
    
           
     
    #Remove pass and write your logic here

def sort_marks():
    list_of_marks.sort(reverse=False)
    list_of_marks = tuple(list_of_marks)
    return list_of_marks
    #Remove pass and write your logic here

def generate_frequency():
    pass
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())