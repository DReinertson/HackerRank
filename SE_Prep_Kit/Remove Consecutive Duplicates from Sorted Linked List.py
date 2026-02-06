def deleteDuplicates(head):
    # Write your code here
    
    currentNode = head
    
    while currentNode and currentNode.next:
        if currentNode.data == currentNode.next.data:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    
    return head
