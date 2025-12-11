class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def reverse_string(string):
    stack=Stack()
    rs=""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        rs += stack.pop()
 
    return rs
my_string = 'hello'

print ( reverse_string(my_string) )
