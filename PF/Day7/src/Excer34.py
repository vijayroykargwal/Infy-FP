#PF-Exer-34
from math import factorial
import random
from math import factorial
def find_number_of_combination(number_of_flavours):
 total=0
 n = number_of_flavours
 r=0
 while(r<=number_of_flavours):
      total=total+factorial(n)/(factorial(n-r)*factorial(r))
      r=r+1
        
        
 return (total)
#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)