import collections
deq = collections.deque()

deq.append(1)   #enQueue
deq.append(2)
deq.append(3)

print(deq.popleft())  #deQueue
print(deq.popleft())
print(deq.popleft())