#PF-Assgn-16
'''
Created on Feb 21, 2019

@author: vijay.pal01
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make%5
    if(five_needed<=no_of_five and one_needed<=no_of_one):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    elif(five_needed>no_of_five):
        error=5*(five_needed-no_of_five)
        if(error<=no_of_one):
            print("No. of Five needed :", no_of_five)
            print("No. of One needed  :", one_needed+error)
        else:
            print(-1)
    
    else:
        print(-1)



    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)
make_amount(28,8,5)