#PF-Assgn-50
'''
Created on Feb 28, 2019

@author: vijay.pal01
'''


def sms_encoding(data):
 splitted = data.split()
 for i, x in enumerate(splitted):
    if not all(y in 'aeiou' for y in x.lower()):
        splitted[i] = ''.join([y for y in x if y.lower() not in 'aeiou'])

 return(' '.join(splitted))

data="I love Python"
print(sms_encoding(data))