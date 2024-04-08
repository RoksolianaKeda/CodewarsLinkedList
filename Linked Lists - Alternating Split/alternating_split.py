class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if head is None or head.next is None:
        raise ValueError("Not enough nodes")
    first_head = None
    second_head = None
    current = head
    is_first = True

    while current:
        if is_first:
            if first_head is None:
                first_head = current
                first_current = first_head
            else:
                first_current.next = current
                first_current = first_current.next
        else:
            if second_head is None:
                second_head = current
                second_current = second_head
            else:
                second_current.next = current
                second_current = second_current.next

        is_first = not is_first
        current = current.next

    first_current.next = None
    second_current.next = None
    return Context(first_head, second_head)