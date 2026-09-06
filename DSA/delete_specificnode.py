class Node:
    def __init__(self, value):
        self.value =value
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.value, end = "->")
        currentNode = currentNode.next
    print("null")

def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    if currentNode.next is None:
        return head
    currentNode.next = currentNode.next.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(6)
node4 = Node(9)
node5 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Linked List before deleting node:", end="")
traverseAndPrint(node1)     

node1 = deleteSpecificNode(node1, node4)

print("\nAfter Deletion:")

traverseAndPrint(node1)

