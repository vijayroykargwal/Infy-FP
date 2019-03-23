#PF-Prac-12
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def generate_sentences(subjects,verbs,objects):
    #start writing your code here
    list1=[]
    for i in range(len(subjects)):
        for j in range(len(verbs)):
            for k in range(len(objects)):
                list1.append(subjects[i]+" "+verbs[j]+" "+objects[k])
                
                

    
    return list1

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))