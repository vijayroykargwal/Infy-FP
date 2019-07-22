#DSA-Exer-22
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code earlier written for this function
    temp = num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]= temp


def order_heights(student_list,height_list):
    #Write your logic here
     
    end_index=len(height_list)
    for index1 in range(0, end_index-1):
        swapped=False
        
        for index2 in range(0, (end_index-index1-1)):
            if(height_list[index2]>height_list[index2+1]):
                swap(height_list, index2, index2+1)
                swap(student_list, index2, index2+1)
                swapped=True;
        if(swapped==False):
            break 
    
        
    return[student_list,height_list]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])
