class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        new_head = reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head