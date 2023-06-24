class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
            
            
    def display(self):
        if self.head is None:
            print("stack is empty")
        else:
            curr=self.head
            while curr.next:
                print(curr.data,end="-->")
                curr=curr.next
            print(curr.data)
            
            
obj=Stack()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()
obj.pop()
obj.display()

