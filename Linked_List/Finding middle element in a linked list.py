# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

# function should return index to the any valid peak element
def findMid(head):
    temp = head
    i=1
    while temp:
        temp = temp.next
        i+=1
    mid = (i/2)+1
    tpoint = head
    j=1
    while j<mid:
        element = tpoint.data
        tpoint = tpoint.next
        j+=1
    return element
    # Code here
    # return the value stored in the middle node
