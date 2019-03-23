#DSA-Exer-24

def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy 
    approach to make the change for the amount 
    using the currencies in the denomination list.
    The function should return the total number of
     notes needed to make the change. If change cannot 
     be obtained for the given amount, then return -1. 
     Return 1 if the amount is equal to one of the currencies 
     available in the denomination list.  '''
    number_of_notes = 0
    if(amount in denomination_list):
        return 1
    maximum_value = max(denomination_list)
    while(amount!=0): 
        number_of_notes+=1
        if(maximum_value<=amount):
            amount = amount-maximum_value
            index = denomination_list.index(maximum_value)
            maximum_value = max(denomination_list)
        else:
            number_of_notes-=1
            index = denomination_list.index(maximum_value)
            denomination_list.pop(index)
            if(len(denomination_list)==0):
                return -1
            maximum_value = max(denomination_list)
            
        continue
    return number_of_notes
                
                
          
#Pass different values to the function and test your program
amount= 3
denomination_list = [30, 10, 20]
make_change(denomination_list, amount)
