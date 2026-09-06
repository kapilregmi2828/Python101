class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.value

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.value, end = "->")
            temp = temp.next
        print()

# create a queue Object
myQueue = Queue()
myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")    

print("Linked List Queue:", end="")
myQueue.printQueue()    

print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Linked List Queue after dequeue:", end="")
myQueue.printQueue()

print("Is Empty:", myQueue.isEmpty())
print("Size:", myQueue.size())