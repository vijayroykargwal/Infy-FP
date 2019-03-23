#PF-Prac-4
'''
Created on Mar 23, 2019

@author: vijay.pal01
'''

def find_nine(nums):
    #Remove pass and write your code here
    n=len(nums)
    for i in range(n):
        if(n<4):
            if(nums[i]==9):
                return True
        if(nums[i]==9 and i<4):
            return True
    return False    
        
        
    

nums=[1, 9, 2, 3, 10]
print(find_nine(nums))