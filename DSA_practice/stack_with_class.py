class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Stack:", myStack.stack)

print("Peek:", myStack.peek())

print("Popped Item: ", myStack.pop())

print("Stack after poped item:", myStack.stack)

print("is Empty?", myStack.isEmpty())

print("Size is:", myStack.size())