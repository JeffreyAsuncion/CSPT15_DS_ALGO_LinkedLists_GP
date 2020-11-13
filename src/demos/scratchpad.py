"""
Here we will outline a few concepts in comments and code.
"""

class LinkedListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = current

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):  
        self.head = head
        self.tail = tail

    def append(self, data):
        new_node = LinkedListNode(data)

        if self.tail:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            
            
# (10)->(20)->
lln = LinkedListNode(10)

ll = LinkedList(lln)
ll.append(20)
