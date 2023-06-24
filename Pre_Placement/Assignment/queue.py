# Implement python queue using list
my_queue = []

# enqueue
def enqueue(my_queue, data):
    my_queue.append(data)
    
enqueue(my_queue, 3)
enqueue(my_queue, 5)
enqueue(my_queue, 8)
enqueue(my_queue, 9)
enqueue(my_queue, 19)
print(my_queue)
# [1, 2, 3, 4, 5]

# deque
def deque(my_queue):
    my_queue.pop(0)

# isEmpty
def isEmpty(my_queue):
    if len(my_queue) == 0:
        return True 
    else:
        return False

deque(my_queue)
deque(my_queue)
print(my_queue)
print(isEmpty(my_queue))