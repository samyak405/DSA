class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
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
            new_node.prev = temp          # FIX: prev link set

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

    def delete(self, value):
        temp = self.head

        # 1. Search for the node
        while temp is not None and temp.data != value:
            temp = temp.next

        # 2. Not found
        if temp is None:
            print("Value is not in the list")
            return

        # 3. Deleting the head
        if temp == self.head:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
        else:
            # 4. Middle or last node
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev

    # Sirf reverse order me print karta hai (list change nahi hoti)
    def print_reverse(self):
        temp = self.head
        print("List in reverse order:", end=" ")
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def reverse(self):
        cur = self.head
        last = None
        while cur:
            cur.prev, cur.next = cur.next, cur.prev
            last = cur
            cur = cur.prev
        self.head = last

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

    def count_occurrence(self, value):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.data == value:
                count += 1
            temp = temp.next
        return count


# ---------- Testing ----------
dll = DoublyLinkedList()
dll.append(Node(10))
dll.append(Node(20))
dll.append(Node(30))
dll.append(Node(40))
dll.append(Node(10))
dll.append(Node(20))
dll.append(Node(30))
dll.traverse()              # 10->20->30->40

dll.insert(5, 100)
dll.traverse()              # 10->20->30->40->100

dll.insert(3, 200)
dll.traverse()              # 10->20->200->30->40->100

dll.delete(20)
dll.traverse()

print("Count of 10:", dll.count_occurrence(10))
print("Count of 20:", dll.count_occurrence(20))

dll.print_reverse()         # 100 40 30 200 10
dll.find_middle()           # Middle: 30
dll.pair_sums()             # Pair sums: [210, 70, 100]

dll.reverse()
dll.traverse()              # 100->40->30->200->10
