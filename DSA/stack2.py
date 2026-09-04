class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
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
print("pop:", myStack.pop())
print("Stack after pop:", myStack.stack)
print("peek:", myStack.peek())
print("isEmpty:", myStack.isEmpty())
print("size:", myStack.size())