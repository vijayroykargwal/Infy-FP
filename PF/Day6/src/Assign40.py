#PF-Assgn-40
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''
new_word=""
def is_palindrome(word):
     word=word.upper()
     new_word=word[::-1]
      
     
     if(new_word==word):
         return True
     else:
         return False
    
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")