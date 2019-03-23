#PF-Assgn-32
'''
Created on Feb 25, 2019

@author: vijay.pal01
'''

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    
    pcount=0
    ocount=0
    ecount=0
    pmsl=[]
    pmsl=patient_medical_speciality_list
    
    for i in range(0,len(pmsl)):
        if(pmsl[i]=='P'):
            pcount=pcount+1
            
        elif(pmsl[i]=='O'):
            ocount=ocount+1
            
        elif(pmsl[i]=='E'):
            ecount=ecount+1
            
    if(pcount>ocount and pcount>ecount):
            speciality="Pediatrics"
            
    elif(ocount>pcount and ocount>ecount):
            speciality="Orthopedics"
            
    elif(ecount>pcount and ecount>ocount):
            speciality="ENT"
        
    
    # write your logic here

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)