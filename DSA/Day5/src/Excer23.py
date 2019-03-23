#DSA-Exer-23
'''
Created on Mar 19, 2019

@author: vijay.pal01
'''
def arrange_tickets(tickets_list):
    #Remove pass and write your logic here
    vacant_list = ["V"]*20
    for i in tickets_list:
        vacant_list.pop(int(i[1:])-1)
        vacant_list.insert((int(i[1:])-1),i)
    first_list = vacant_list[:10]
    next_list = vacant_list[10:]
    while("V" in next_list):
        next_list.remove("V")
    for i in range(0,len(first_list)):
        if(first_list[i]=="V"):
            first_list.pop(i)
            first_list.insert(i,next_list.pop(0))
    return first_list
        
tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
