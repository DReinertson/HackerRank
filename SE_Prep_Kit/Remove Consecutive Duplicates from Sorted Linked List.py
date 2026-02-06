def deleteDuplicates(head):
    # Write your code here
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    class LinkedList:
        def __init__(self):
            self.head = None
    
    currentNode = head
    duplicated_linked_list = LinkedList()
    
    while currentNode:
        if not currentNode.next:
            if not duplicated_linked_list.head:
                duplicated_linked_list.head = Node(currentNode.data)
                break
            else:
                duplicate_node.next = Node(currentNode.data)
                break
        if currentNode.data != currentNode.next.data:
            if not duplicated_linked_list.head:
                duplicated_linked_list.head = Node(currentNode.data)
                duplicate_node = duplicated_linked_list.head
            else:
                duplicate_node.next = Node(currentNode.data)
                duplicate_node = duplicate_node.next
                
        currentNode = currentNode.next
    
    return duplicated_linked_list.head
