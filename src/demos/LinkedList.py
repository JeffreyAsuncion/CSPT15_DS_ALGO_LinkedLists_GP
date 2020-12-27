"""
Here we will outline a few concepts in comments and code.
"""

class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self, head=None):  
        self.head = head

    def append(self, data):
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        else:
            self.head = new_node    


# (10)->(20)->
lln = LinkedListNode(10)

# pass lln to LinkedList as head
ll = LinkedList(lln)
ll.append(20)
