class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_Node = Node(data)

        if self.head:
            new_Node.next = self.head
        self.head = new_Node
        self.length +=1 

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_Node = self.head

        self.head = self.head.next
        self.length -= 1

        return popped_Node.data

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def traverseAndPrint(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data, end = "->")
            currentNode = currentNode.next
        print()

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("LinkedList:", end = "")
myStack.traverseAndPrint()

print("Peek:", myStack.peek())

print("Pop:", myStack.pop())

print("LinkedList after pop:", end = "")
myStack.traverseAndPrint()

print("is Empty?", myStack.isEmpty())

print("Size:", myStack.size())