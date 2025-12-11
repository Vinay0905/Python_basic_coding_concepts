class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node
        self.length=1
    
        
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def push(self,value):
        new_node=Node(value)
        if self.length==0:
            self.new_node=new_node
            self.bottom=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.length+=1
        return self.length

    def pop(self):
        if self.length==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.length-=1
        return temp.value
        
my_stack=Stack(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.print_stack()
print("*\n*\n*")
print(my_stack.pop())
