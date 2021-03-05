# front, rear 이용
SIZE = 4
Q = [0]*SIZE
front, rear = 0, 0
def isFull():
    # return rear == len(Q)-1
    return (rear+1) % SIZE == front
def isEmpty():
    return front == rear
def enQueue(item):
    global rear
    if isFull(): print("Queue Full")
    else:
        rear = (rear + 1) % SIZE
        Q[rear] = item
def deQueue():
    global front
    if isEmpty() : print("Queue Empty")
    else:
        front = (front + 1) % SIZE
        return Q[front]
    # if front != rear:
    #     front += 1
    #     return Q[front]


def Qpeek() :
    global front, rear
    if isEmpty() :print("Queue Empty")
    else : return Q[(front+1) % SIZE]

enQueue(1)
print(deQueue())
enQueue(2)
print(deQueue())
enQueue(3)
print(deQueue())
enQueue(4)
enQueue(5)
enQueue(6)
print(Qpeek())
print(deQueue())
