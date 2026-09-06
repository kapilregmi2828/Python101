class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLowestValue(head):
    minValue = head.value
    currentNode = head.next
    while currentNode:
        if currentNode.value < minValue:
            minValue = currentNode.value
        currentNode = currentNode.next
    return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(9)
node5 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value of the linked list is:", findLowestValue(node1))