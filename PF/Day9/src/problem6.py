#PF-Prac-6
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def list123(nums):
    #start writing your code here
    n =  len(nums)
    for i in range(n):
        if(nums[i]==1 and (i==n or i==n-1)):
            return False
        elif(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
    return False

    

nums=[1,2,3,4,5]
print(list123(nums))