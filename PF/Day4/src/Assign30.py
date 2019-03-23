#PF-Assgn-30
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''



def encode(message):
    count=0
    message=message+"@"
    value=""
    for i in range(0,len(message)-1):
        if message[i]==message[i+1]:
            count+=1
           
           
        else:
            value+=str(count+1)+message[i]
            count=0 
            
            
    return value 
#Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)