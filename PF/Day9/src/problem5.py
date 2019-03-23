#PF-Prac-5
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def count_digits_letters(sentence):
    #start writing your code here
    count1=0
    count2=0
    sentence=sentence.replace(' ', '')
    for i in range(0,len(sentence)):
        if(sentence[i].isdigit()):
            count1+=1
        if(sentence[i].isalpha()):
            count2+=1    
        
            
            
    result_list=[count2,count1]
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))