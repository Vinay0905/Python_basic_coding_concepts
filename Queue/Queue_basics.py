class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
    
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
        
    def enqueu(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first =new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return self.length     
    def dequeu(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp.value
    
    
    
my_queue=Queue(1)
my_queue.enqueu(2)

my_queue.enqueu(3)
# my_queue.print_queue()
print(my_queue.dequeu())
print(my_queue.dequeu())

            
