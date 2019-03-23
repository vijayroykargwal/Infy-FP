#PF-Exer-35
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''


def count_names(name_list):
    count1=0
    count2=0
    str1=""
    str2=""
    for i in range(0,len(name_list)):
      str1 = str1+name_list[i]
    count2 = str1.count("at")
    
    for i in range(0,len(name_list)):
        if(len(name_list[i])==3):
            str2= str2+name_list[i]
            count1= str2.count("at")
    print("_at -> ",count1)
    print("%at% -> ",count2)
    #start writing your code here
    
    return 1
            
            
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print("_at -> ",count1)
    #print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=['Rat', 'saturday']
count_names(name_list)