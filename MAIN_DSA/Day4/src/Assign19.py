#DSA-Assgn-19
'''
Created on Mar 18, 2019

@author: vijay.pal01
'''


def last_instance( num_list,  start,  end,  key):
    num_list = num_list[::-1]
    try:
        indx = end-num_list.index(key)
    except ValueError:
        indx = -1
    return indx

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")