#DSA-Assgn-16
'''
Created on Mar 18, 2019

@author: vijay.pal01
'''



from src.DataStructures import Stack,Queue

def separate_boxes(box_stack):
    #Remove pass and write your logic here
    new_queue = Queue(box_stack.get_max_size())
    mod_stack = Stack(box_stack.get_max_size())
    while(not(box_stack.is_empty())):
        data = box_stack.pop()
        if(data=="Red" or data=="Green" or data=="Blue"):
            mod_stack.push(data)
        else:
            new_queue.enqueue(data)
    while(not(mod_stack.is_empty())):
        a = mod_stack.pop()
        box_stack.push(a)
    return(new_queue)

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()