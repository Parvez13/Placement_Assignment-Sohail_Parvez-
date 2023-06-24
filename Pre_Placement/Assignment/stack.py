# Implementation of stack using a list
my_stack = []

# Append (push() method in stack)
def stack_push(my_stack, data):
    my_stack.append(data)
stack_push(my_stack, 'a')
stack_push(my_stack, 'b')
stack_push(my_stack, 'c')
stack_push(my_stack, 'd')
print(my_stack)
# ['a', 'b', 'c', 'd']

# Pop
def stack_pop(my_queue):
    my_queue.pop()
stack_pop(my_stack)
stack_pop(my_stack)
print(my_stack)
# ['a', 'b']

# IsEmpty
def is_empty(my_stack):
    if len(my_stack) == 0:
        return True
    else: 
        return False

print(is_empty(my_stack))