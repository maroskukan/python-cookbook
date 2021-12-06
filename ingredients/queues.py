import queue

q = queue.Queue()

# test if queue is empty
q.empty()

q.put("bag1")
q.put("bag2")
q.put("bag3")

# test if queue is empty
q.empty()

# Returns bag1
q.get()
