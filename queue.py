class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        if self.rear :
            self.rear.next = Node(data)
            self.rear = self.rear.next
        else:
            self.front = self.rear = Node(data)
    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp = temp.next
    def dequeue(self):
        if self.rear:
            temp=self.front
            self.front = self.front.next
            temp=None
        else:
            print("Queue is empty")



q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print()
print("queue after dequeuing:")
q.dequeue()
q.print()
