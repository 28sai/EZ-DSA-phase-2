#create a stack using user input and extract only even numbers
stack=[]
stack2=[]
def push():
    n=int(input("element: "))
    stack.append(n)
    print(stack)
def even_and_odd():
    n=input()
    if n=="e":
        for i in stack:
            if i%2==0:
                stack2.append(i)
        print(stack2)
        stack2.clear()
            
    elif n=="o":
        for i in stack:
            if i%2!=0:
                stack2.append(i)
        print(stack2)
        stack2.clear()
   
while True:
    print("selectt ur choice: 1.push 2.pop 3.peek 4.display 5.size 6.quit")
    choice=int(input("enter ur choice: "))
    if choice==1:
        push()
    elif choice==2:
        even_and_odd()
    else:
        break
    