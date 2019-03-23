#PF-Assgn-33
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''


def find_common_characters(msg1,msg2):
      #Remove pass and write your logic here
    str1=""
    for i in range(0,len(msg1)):
        for j in range(0,len(msg2)):
            if((msg1[i]==msg2[j]) and (msg1[i] not in str1)):
                str1 += msg1[i]
    if(len(str1)>0):
      return (str1)
    else:
        return -1
        

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)