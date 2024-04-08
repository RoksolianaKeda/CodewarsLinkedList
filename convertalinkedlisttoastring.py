def stringify(node):
    if node is None:
        return "None"

    result = []
    current = node
    while current:
        result.append(str(current.data))
        current = current.next

    result.append("None")
    return " -> ".join(result)