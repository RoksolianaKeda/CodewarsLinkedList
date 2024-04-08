class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise IndexError("List is empty")

    current = node
    current_index = 0

    while current:
        if current_index == index:
            return current
        current = current.next
        current_index += 1
    raise IndexError("Index out of range")