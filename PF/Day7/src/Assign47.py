#PF-Assgn-47
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''
sentence="The sun rises in the east"
def encrypt_sentence(sentence):
 vowel_set = set("aeiouAEIOU")
 new_list=[]
 new_str=""
 sentence = sentence.split(" ")
 
 for i in range(0,len(sentence)):
     if(i%2==0):
         sentence[i]= sentence[i][::-1]
         new_list.append(sentence[i])
     else:
         vowels=list()
         consonants=list()
         for letter in sentence[i]:
             if letter in vowel_set:
                 vowels.append(letter)
             else:
                 consonants.append(letter)
         new_string = "".join(consonants) + "".join(vowels)
         new_list.append(new_string)  
 for i in range(0,len(new_list)):
     if(i==0):
         new_str= new_str+ new_list[i]
     else:
         new_str = new_str+" "+new_list[i]
         
         
     
 
 
 return new_str

 
 
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)