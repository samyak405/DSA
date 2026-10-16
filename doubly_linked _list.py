class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class SinglyLinkedList:
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

    def traverse(self):
        values = []
        cur = self.head
        while cur:
            values.append(str(cur.data))
            cur = cur.next
        print("->".join(values) if values else "List is empty")

    def insert(self, pos, data):
        if pos < 1:
            print("Invalid position")
            return

        node = Node(data)

        # Insert at head
        if pos == 1:
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            self.head = node
            return

        cur = self.head
        for i in range(pos - 2):
            if cur is None:
                break
            cur = cur.next

        if cur is None:
            print("Insert failed")
            return

        node.next = cur.next
        node.prev = cur
        if cur.next is not None:
            cur.next.prev = node
        cur.next = node

    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle:", slow.data)
        return slow.data

    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return
        if self.head == key:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data == key:
            cur = cur.next
        if cur.next == None:
            print(f"{key} not found")
        else:
            cur.next = cur.next.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def pair_sums(self):
        sums = []
        cur = self.head
        while cur:
            if cur.next:
                sums.append(cur.data + cur.next.data)
                cur = cur.next.next
            else:
                sums.append(cur.data)
                cur = cur.next
        print("Pair sums:", sums)
        return sums

dll=SinglyLinkedList()
dll.append(Node(10))
dll.append(Node(20))
dll.append(Node(30))
dll.append(Node(40))
dll.traverse()


dll.insert(5, 100)
dll.traverse()

dll.insert(3, 200)
dll.traverse()