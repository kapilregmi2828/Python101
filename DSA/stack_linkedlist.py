# Stack Implementation using Linked List
# Linked list is a way of storing data where each piece of data is connected to the next piece. 

# Head --> Node1 --> Node2 --> Node3 --> None

# Node is usually of 2 parts one is data and other is pointer to next node. 

# Head if first node of linked list 
# Null is the last node of linked list which points to None.

# lets creat a Stack using linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()

# create a stack Object
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Linked List Stack:", end="")
myStack.traverseAndPrint()
print("Peek:", myStack.peek())
print("Pop:", myStack.pop())

print("Linked List Stack after pop:", end="")
myStack.traverseAndPrint()

print("Is Empty:", myStack.isEmpty())
print("Size:", myStack.stackSize())