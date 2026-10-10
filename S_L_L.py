
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 1

            while temp and count < pos - 1:
                temp = temp.next
                count += 1

            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Invalid position")

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


list1 = Sll()

n1 = Node(10)
n2 = Node(20)
n3 = Node(15)

list1.append(n1)
list1.append(n2)
list1.insert(n3, 2)

list1.print()
