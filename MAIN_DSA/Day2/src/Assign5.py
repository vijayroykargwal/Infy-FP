#DSA-Assgn-5
'''
Created on Mar 14, 2019

@author: vijay.pal01
'''




from src.DataStructures import LinkedList

def create_new_sentence(word_list):
    new_sentence=""
    # Write your logic here
    temp = word_list.get_head()
    while(temp is not None):
        new = temp.get_data()
        if(new=="*" or new=="/"):
            new_sentence+=" "
        elif(new_sentence[-2:]=="  "):
            new_sentence+= new.upper()
        else:
            new_sentence+= new
        temp = temp.get_next()
    new_sentence = new_sentence.replace('  ',' ')
    return new_sentence


word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
print(result)