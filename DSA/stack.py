# Stack is a linear data structure that follows the Last In First Out (LIFO) principle. 
# The last element added to the stack will be the first one to be removed.

stack = []
# Push elements onto the stack
stack.append("A")
stack.append("B")
stack.append("C")
# peek at the top element of the stack
print("Top element of the stack is:", stack[-1])

# Pop elements from the stack
print("Popped element from the stack is:", stack.pop())
print("Stack after popping:", stack)    

# Check if the stack is empty
if not stack:
    print("Stack is empty")

isEmpty = not bool(stack)
print("Is the stack empty?", isEmpty)

# size of the stack
print("Size of the stack is:", len(stack))