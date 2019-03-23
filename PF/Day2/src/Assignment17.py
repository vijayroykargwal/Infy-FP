#PF-Assgn-17
'''
Created on Feb 21, 2019

@author: vijay.pal01
'''


def find_new_salary(current_salary,job_level):
    # write your logic here
    if(job_level==3):
        new_salary = 0.15*current_salary + current_salary
    elif(job_level==4):
        new_salary = 0.07*current_salary + current_salary
    elif(job_level==5):
        new_salary = 0.05*current_salary + current_salary
    else:
        new_salary = 0
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)