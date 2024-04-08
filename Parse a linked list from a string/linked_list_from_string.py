class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s.lower() in ["null", "nil", "nullptr", "null()", "None", "none"]:
        return None
    data = s.split(" -> ")
    head = None
    current = head
    for val in data[:-1]:
        if val!="None":
            node = Node(int(val))
        else:
            node = Node(val)
        if head is None:
            head = node
            current = head
        else:
            current.next = node
            current = current.next
    return head