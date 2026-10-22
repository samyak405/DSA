
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next

    def print_stack(self, temp):
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse_stack(self, st1):
        temp = self.top
        while temp:
            st1.push(Node(temp.data))
            temp = temp.next


st = Stack()
st1 = Stack()

st.push(Node(1))
st.push(Node(2))
st.push(Node(3))
st.push(Node(4))

print("Stack elements:")
st.print_stack(st.top)

st.pop()

print("Stack after pop:")
st.print_stack(st.top)

st.reverse_stack(st1)

print("Stack after reverse:")
st1.print_stack(st1.top)
