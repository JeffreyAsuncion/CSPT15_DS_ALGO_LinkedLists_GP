"""
Given a reference to the head node of a singly-linked list, 

write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.
In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.
In order to do this in O(n) time, you should only have to traverse the list
once.
*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # Your code here

    # create a ref to the head of list (our current node)
    current_node = head_of_list
    # create a pointer for the prev (set to null, None, nullptr)
    prev = None
    # create a pointer for a next (set to null, None, nullptr)
    next = None

    # while the current node exists (traverse the linked list while the current node is not none)
    while current_node:
        # my next pointer get set to the current node `next`
        """This switches the pointer"""
        next = current_node.next
        # my current nodes next get set to the prev
        """This switches the pointer and FLIPS the Node"""
        current_node.next = prev
        # set prev pointer to my current node
        """This is the swap"""
        prev = current_node
        # set ref of current to next (increment to the next node in the chain)
        """This is the traversal"""
        current_node = next

    # return the node that the pre pointer is currently pointing to 
    return prev
    