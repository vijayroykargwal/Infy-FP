#DSA-Assgn-1
'''
Created on Mar 13, 2019

@author: vijay.pal01
'''


def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    list2.reverse()
    for i in range(0,len(list2)):
        if((list1[i] and list2[i]) is not None):
            if(i==0):
                merged_data = merged_data+list1[i]+list2[i]
            else:
                merged_data = merged_data+" "+list1[i]+list2[i]
        else:
            if(list2[i] is None):
                if(i==0):
                    merged_data = merged_data+list1[i]
                else:
                    merged_data = merged_data+" "+list1[i]
            else:
                if(i==0):
                    merged_data = merged_data+list2[i]
                else:
                    merged_data = merged_data+" "+list2[i]
        
        resultant_data= merged_data   
    return resultant_data 

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)