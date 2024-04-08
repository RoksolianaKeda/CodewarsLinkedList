# from preloaded import Node
class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next
    third = second.next

    second.next = first
    first.next = swap_pairs(third)

    return second