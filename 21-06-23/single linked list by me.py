class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr.next:
                print(curr.data,end="-->")
                curr=curr.next
            print(curr.data)
    def insert_at_beg(self,data):
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def insert_at_end(self,data):
        curr=self.head
        newnode=Node(data)
        if self.head is None:
            print("list is empty")
        else:
            
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def insert_at_position(self,data,pos):
        if pos<=0:
            self.insert_at_beg(data)
        else:
            newnode=Node(data)
            curr=self.head
            for i in range(pos-1):
                curr=curr.next
            newnode.next=curr.next
            curr.next=newnode
    def del_at_beg(self):
        curr=self.head
        if self.head is None:
            print("empty list")
        else:
            self.head=self.head.next
    def del_at_end(self):
        curr=self.head.next
        prev=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr.next:
                curr=curr.next
                prev=prev.next
            prev.next=None
    def del_at_position(self,pos):
        curr=self.head.next
        prev=self.head
        if pos<=0:
            self.del_at_beg(pos)
        else:
            for i in range(pos-1):
                curr=curr.next
                prev=prev.next
            prev.next=curr.next
            curr.next=None
    def search(self,n):
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr:
                if curr.data==n:
                    print("it is present")
                    break
                curr=curr.next
            else:
                print("not present")
                
obj=SLL()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
obj.display()
obj.insert_at_beg(1)
obj.display()
obj.insert_at_end(2)
obj.display()
obj.insert_at_position(3,0)
obj.display()
obj.del_at_beg()
obj.display
obj.del_at_end()
obj.display()
obj.del_at_position(3)
obj.display()
n=int(input())
obj.search(n)
