class Node:
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
        
def IS_BALANCED_PARENTHESES(string):
    stack=Stack()
    for char in string:
        if char == "(":
            stack.push(char)
        elif char==")":
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()


print(IS_BALANCED_PARENTHESES("()(()"))

print(IS_BALANCED_PARENTHESES("()()()"))
print(IS_BALANCED_PARENTHESES(')('))