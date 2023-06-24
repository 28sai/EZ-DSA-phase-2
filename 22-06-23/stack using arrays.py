stack=[]
def push():
    n=int(input("element: "))
    stack.append(n)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        x=stack.pop()
        print("removed element is",x)
        print(stack)
def peek():
    if not stack:
        print("empty")
    else:
        print(stack[-1])
def display():
    if not stack:
        print("empty")
    else:
        for i in stack:
            print(i)
def size():
    if not stack:
        print("empty")
    else:
        print(len(stack))

while True:
    print("selectt ur choice: 1.push 2.pop 3.peek 4.display 5.size 6.quit")
    choice=int(input("enter ur choice: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        size()
    else:
        break