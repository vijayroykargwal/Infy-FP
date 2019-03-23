#PF-Assgn-48
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''
def find_correct(word_dict):
    correct, almost_correct, wrong = 0, 0, 0
    for key, value in word_dict.items():
        diff_list = set(list(key)).symmetric_difference(set(list(value)))  
        diff = len(diff_list)
        if diff == 0:
            correct += 1
        elif diff <= 2:
            almost_correct += 1
        elif diff > 2:
            wrong += 1

    list1 =list()
    list1.append(correct)
    list1.append(almost_correct)
    list1.append(wrong)
    return list1

word_dict={"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))