# Queue is a data structure that follows first in first out (FIFO)
# People standing in a line is a good example of queue. 
# The person who comes first will be served first.

queue = []

queue.append('A')  # Enqueue operation
queue.append('B')  # Enqueue operation
queue.append('C')  # Enqueue operation
print("Queue:", queue)

# peek operation
print("Peek:", queue[0])

# Dequeue operation
dequeueElement = queue.pop(0)
print("Dequeued Element:", dequeueElement)
print("Queue after dequeue:", queue)

# Check if the queue is empty
isEmpty = not bool(queue)
print("Is the queue empty?", isEmpty)

# Check the size of the queue
print("Size:", len(queue))  
