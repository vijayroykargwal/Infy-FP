'''
Created on Mar 21, 2019

@author: vijay.pal01
'''
def build_index_grid(rows, columns):
    result_list = []
    for i  in range(rows):
        list1 = []
        for j in range(columns):
            list1.append(str(i)+","+str(j))
        result_list.append(list1)
            

    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)