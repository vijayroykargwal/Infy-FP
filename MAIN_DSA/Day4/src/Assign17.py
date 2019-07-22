#DSA-Assgn-17
'''
Created on Mar 18, 2019

@author: vijay.pal01
'''


def find_matches(country_name):
    list1 = []
    for i in match_list:
        if((i[:3]) == country_name):
            list1.append(i)
    return list1

def max_wins():
    cham = []
    wor = []
    t20 = []
    tmp = []
    new = dict()
    """ChampionShip Check"""
    for i in match_list:
        split_detail = i.split(":")
        if(split_detail[1] == "CHAM"):
            cham.append(split_detail[0])
            tmp.append(split_detail[3])
    if(len(tmp)!=0):        
        while (min(tmp)!=max(tmp)):
            cham.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        new ["CHAM"] = cham
    """T20 Check"""
    tmp = []
    for i in match_list:
        split_detail = i.split(":")
        if(split_detail[1] == "T20"):
            t20.append(split_detail[0])
            tmp.append(split_detail[3])
    if(len(tmp) !=0):
        while (min(tmp)!=max(tmp)):
            t20.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        new ["T20"] = t20

    """World Cup Check"""
    tmp = []
    for i in match_list:
        split_detail = i.split(":")
        if split_detail[1] == "WOR":
            wor.append(split_detail[0])
            tmp.append(split_detail[3])
    if(len(tmp)!=0):
        while (min(tmp)!=max(tmp)):
            wor.pop(tmp.index(min(tmp)))
            tmp.pop(tmp.index(min(tmp)))
        new ["WOR"] = wor 
    return new

def find_winner(country1,country2):
    c1 = 0
    c2 = 0
    for detail in match_list:
        split_detail = detail.split(":")
        
        if split_detail[0] == country1:
            c1+=int(split_detail[3])
        elif split_detail[0] == country2:
            c2+=int(split_detail[3])
    if c1 > c2:
        return country1
    elif c2 > c1:
        return country2
    return "Tie"    

#Consider match_list to be a global variable
#match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0",
#"IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0",
#"PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]
match_list=['AUS:WOR:6:4', 'ENG:CHAM:5:4']
#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()
find_matches("AUS")
max_wins()
find_winner("IND", "AUS")
