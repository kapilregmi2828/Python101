class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.length +=1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"

        popped_item = self.head
        self.head = self.head.next
        self.length -= 1
        return popped_item.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.head.value

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end = "->")
            currentNode = currentNode.next
        print()

myStack = Stack()

myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Linked List: ", end = "")
myStack.traverseAndPrint()
print("Peek", myStack.peek())
print("Popped Item:", myStack.pop())
print("Linked list after pop:", end = "")
myStack.traverseAndPrint()
print("Peek", myStack.peek())
print("Is Empty?", myStack.isEmpty())
print("Size", myStack.size())