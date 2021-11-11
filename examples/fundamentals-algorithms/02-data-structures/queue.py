#!/usr/bin/env python

from collections import deque

# Create a new empty deque object that will function as queue
queue = deque()

# Add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue contents
print(queue)

# Pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
