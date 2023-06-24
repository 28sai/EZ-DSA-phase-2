class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end=" ")
            curr= curr.next
lst=SLL()
n=int(input())
for i in range(n):
    data=int(input("data item: "))
    lst.append(data)
lst.display()
    

obj=SLL()
n=Node(1)
obj.head=n
n1=Node(2)
obj.head.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
n4=Node(5)
n3.next=n4
n5=Node(6)
n4.next=n5


