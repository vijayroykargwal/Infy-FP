#DSA-Exer-27
'''
Created on Mar 20, 2019

@author: vijay.pal01
'''
#DSA-Exer-27

def max_sum_is(num_list):
    #Remove pass and write your logic here
    n = len(num_list)
    count = [0 for i in range(10)] 
    for i in range(n): 
        for j in range(num_list[i]-1, -1, -1): 
            count[num_list[i]] += count[j] 
        count[num_list[i]] += 1
    result = 0
    for i in range(10): 
        result += count[i] 
    return result


#Pass different values to the function and test your program
num_list=[1, 101, 2, 3, 100, 4, 5]
print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))

