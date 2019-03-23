#PF-Prac-11
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''
def find_upper_and_lower(sentence):
    #start writing your code here
    count1=0
    count2=0
    for i in sentence:
        if(i.isupper()):
            count1+=1
        if(i.islower()):
            count2+=1
    result_list=[count1,count2]
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))