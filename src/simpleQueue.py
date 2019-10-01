import queue
#Queue is created
list = queue.Queue()
# Data is inserted into Queue using put() data is inserted at the end
list.put(5)
list.put(9)
list.put(1)
list.put(7)
# get() takes data from head of queue
print(list.get())
print(list.get())
print(list.get())
print(list.get())