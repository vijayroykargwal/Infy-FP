
def list_details(lst):
    print("Present size of the list:")
    print("Size:", len(lst))
     
    lst.append("Mango")
    lst.append("Banana")
    lst.append("Apple")
     
    print("\nSize of the list after adding some items")
    print("Size:", len(lst))
     
    print("\nInserting a new item at the given position:")
    lst.insert(1, "Oranges")
    print(lst)
     
    print("\nDeletion of an item from the list:")
    lst.pop(2)
    print(lst)
    
    
 
     
 
shopping_list=[]
print("Empty list is created with name shopping_list!\n")
 
list_details(shopping_list)


