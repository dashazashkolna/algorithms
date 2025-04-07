class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None

class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        if not self.head or not self.head.next or k == 0:
            return

        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return

        current.next = self.head
        steps_to_new_head = length - k
        new_tail = self.head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        new_tail.next = None
        self.tail = new_tail

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


import sys

def safe_input():
    try:
        return input().strip()
    except EOFError:
        return ''

n_line = safe_input()
if n_line:
    n = int(n_line)
    values_line = safe_input()
    if values_line:
        values = map(int, values_line.split())
        linked_list = List()
        for val in values:
            linked_list.addToTail(val)

        while True:
            k_line = safe_input()
            if not k_line:
                break
            k = int(k_line)
            linked_list.RotateRight(k)
            linked_list.Print()
