# '''Create and print a dictionary'''
# mobileDict={
#     "brand": "Motorola",
#     "model": "One Power",
#     "year": 2018,
#     }
# print(mobileDict)
# #print(mobileDict.items())
# '''Accessing items of a dictionary'''
# itemYear=mobileDict["year"]
# itemModel=mobileDict.get("model")
# 
# '''Changing values of a dictionary'''
# mobileDict={
#     "brand": "Motorola",
#     "model": "One Power",
#     "year": 2018
#     }
# mobileDict["year"]=2017
# itemYear=mobileDict["year"]
# 
# '''Print keys of a dictionary'''
# for x in mobileDict:
#     print(x)
# 
# '''Print values'''
# for x in mobileDict:
#     print(mobileDict[x])
# 
# for x in mobileDict.values():
#     print(x)
# 
# '''Loop through both keys and values'''
# for x, y in mobileDict.items():
#     print(x, y)
# 
# '''Length of dictionary'''
# print(len(mobileDict))

'''Adding and removing items'''
mobileDict={
    "brand": "Motorola",
    "model": "One Power",
    "year": 2018
    }
mobileDict["color"] = "black"
mobileDict["screen"] = "Amoled"
print(mobileDict)


# print(mobileDict.pop("color"))
# print(mobileDict)