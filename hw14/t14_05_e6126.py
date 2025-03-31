class Node:
    def __init__(self, item: int):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.back = None

    def empty(self):
        return self.head is None and self.back is None

    def push(self, n: int):
        node = Node(n)
        if self.empty():
            self.head = node
        else:
            self.back.next = node
        self.back = node
        self.count += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        current = self.head
        res_item = current.item
        self.head = self.head.next

        if self.head is None:
            self.back = None
        self.count -= 1

        return res_item

    def front(self):
        if self.empty():
            return "error"
        return self.head.item

    def size(self):
        return self.count

    def clear(self):
        while not self.empty():
            self.pop()

        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            res = queue.execute(line)
            print(res)
            if res == "bye":
                break