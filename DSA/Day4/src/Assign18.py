#DSA-Assgn-18
'''
Created on Mar 18, 2019

@author: vijay.pal01
'''


def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    list1 = []
    text = text.split()
    for i in text:
        if i not in vocabulary:
            list1.append(i)
    if(len(list1)!=0):
        return set(list1)
    else:
        return -1
#Pass different values
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)