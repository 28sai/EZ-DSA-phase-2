queue=[]
def enqueue():
    n=int(input("element: "))
    queue.append(n)
    print(n, "is added in queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        x=queue.pop()
        print("removed element is",x)
def peek():
    if not queue:
        print("empty")
    else:
        print(queue[-1])
def display():
    print(queue)
def size():
    if not queue:
        print("empty")
    else:
        print(len(queue))
while True:
    print("selectt ur choice: 1.enqueue 2.denqueue 3.peek 4.display 5.len 6.quit")
    choice=int(input("enter ur choice: "))
    if choice==1:
        enqueue()
    elif choice==2:
        denqueue()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        size()
    else:
        break

    