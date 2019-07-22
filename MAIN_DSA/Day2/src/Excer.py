import re
str ="Encountered Error : error code E101"
if(re.search(r"E...r",str)!=None):
    str2=re.sub(r"E(\d{3})",r"#\1",str)
        
    
