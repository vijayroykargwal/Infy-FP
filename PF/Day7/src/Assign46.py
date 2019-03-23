#PF-Assgn-46
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''


def nearest_palindrome(number):
    while(number>=0):
     number+=1 
     str1= ''
     str2=''
     str1=str1+str(number)
     str2=str1[::-1]
     if(str2==str1):
         break
     
         
     continue
    return number
number=99
print(nearest_palindrome(number))