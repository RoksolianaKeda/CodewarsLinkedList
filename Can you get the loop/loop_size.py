def loop_size(node):
    visited = set()
    current = node
    loop_start = None

    while current:
        if current in visited:
            loop_start = current
            break

        visited.add(current)
        current = current.next
    
    if not loop_start:
        return 0
    loop_size = 1
    current = loop_start.next
    while current != loop_start:
        loop_size += 1
        current = current.next
    
    return loop_size