'''Creating, defining a list'''
list1=[10,20,30]
for x in list1:
    print(x)

#A list can be declared with a None value

listN=[None, None]
listN1=[None]*5 #Which means there are 5 elements defined as None

print('----------------------------')

'''List can be a collection of heterogeneous data'''

list2=[10,12.3,'c',"Lists"]
for x in list2:
    print(x)

print('----------------------------')

'''Check if an element is present in a list'''

list3=[10,20,30,40,50]
if 60 in list1:
    print("Present")
else:
    print("Absent")

#not in can also be used similarly

print('----------------------------')

'''Accessing individual elements of a list or changing a single value of a list using its index'''

list4=[10,20,30,40,50]
print(list4[3])

#Modifying a list
print("Before modification:"+str(list4[2]))
list4[2]=100
print("After modification:"+str(list4[2]))

print('----------------------------')

'''Ways to access a list'''

characters=["Chandler","Monica","Phoebe","Joey","Rachel","Ross"]

print("Iterating the list using range()")
for index in range(0,len(characters)):
    print(characters[index])

print("Iterating the list using keyword in")
for charac in characters:
    print(charac)

print('----------------------------')

'''Concatenating two lists '''
a=["North","South"]
b=["East", "West"]
directions=a+b
print(directions)

print('----------------------------')

''' List SLicing '''
items=["Purse","Notepad","Pen","Mobile","Earphones"]
print(items[-2])
new_items=items[1:4]
print(new_items)
new_items=items[-3:-1]
print(new_items)

print('----------------------------')

'''Few list functions'''
list5=[10,70,39,82,5,99,27,12,18,82]
print("Length of list:"+str(len(list5)))
print("Count of 82:"+str(list5.count(82)))
print("Index of 82:"+str(list5.index(82)))
list5.append(99)
list5.insert(3, 96)
list5.remove(82)
list5.reverse()
list5.sort(reverse=False) #Ascending
list5.sort(reverse=True) #Descending
