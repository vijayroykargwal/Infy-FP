#PF-Assgn-31
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''

def check_palindrome(word):
    
    
     str= word
     str1=word[::-1]
     if(str == str1):
         return True
     else:
         return False
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
