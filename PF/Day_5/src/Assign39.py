#PF-Assgn-38
'''
Created on Mar 1, 2019

@author: vijay.pal01
'''
def check_double(number):
    str1=""
    str1=str1+str(number)
    list1=list(str1)
    
    double_number=number*2
    str2=""
    str2=str2+str(double_number)
    list2=list(str2)
    
    if(len(list1)==len(list2)):
        count=0
        for i in list1:
            for j in list2:
                if(i==j):
                    count+=1
                    
        if(count==len(list1)):
            return True
        else:
            return False
    else:
        return False


print(check_double(125874))