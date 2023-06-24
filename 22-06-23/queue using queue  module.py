import queue
a=queue.Queue()
b=queue.Queue()
for i in range(5):
    b.put(i)
print(a.empty())
print(b.empty())
import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(type(L))