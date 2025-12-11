class Node:
    def __init__(self,v):
        self.v=v
        self.next=None
class LinkedList:
    def __init__ (self,v):
        new_node=Node(v)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,v):
        new_node=Node(v)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp

    def prepend(self,v):
        new_node=Node(v)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    def get(self,i):
        if self.length==0:
            return None
        else:
            temp=self.head
            for _ in range(i):
                temp=temp.next
            return temp

    def set_vaue(self,v,i)  :
        if self.length==0:
            return None
        else:
            temp=self.get(i)
            if temp:
                temp.v=v
                return True
            return False

    def insert_node(self,v,i):
        if i<0 or i>self.length:
            return False
        if i==0:
            return self.prepend(v)
        if i==self.length:
            return self.append(v)
        new_node=Node(v)
        temp=self.get(i-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    
    def remove(self,i):
        if i<0 or i>=self.length:
            return None
        if i==0:
            return self.pop_first()
        if i==self.length-1:
            return self.pop()
        prev=self.get(i-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        



    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.v)
            temp=temp.next



My_linkedList=LinkedList(1)
My_linkedList.append(2)
# My_linkedList.pop()

My_linkedList.append(34234)
My_linkedList.append(4)
# My_linkedList.print_list()
My_linkedList.print_list()
My_linkedList.reverse()
My_linkedList.print_list()

