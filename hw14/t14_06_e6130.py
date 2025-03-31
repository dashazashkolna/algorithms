class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.end = None
        self.counter = 0

    def empty(self):
        return self.head is None and self.end is None

    def push_front(self, item):
        node = Node(item)
        node.next = self.head
        if not self.empty():
            self.head.prev = node
        else:
            self.end = node
        self.head = node
        self.counter += 1

        return "ok"

    def push_back(self, item):
        node = Node(item)
        node.prev = self.end
        if self.empty():
            self.head = node
        else:
            self.end.next = node
        self.end = node
        self.counter += 1

        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
        cur_head = self.head
        res_item = cur_head.item
        self.head = self.head.next
        if self.head is None:
            self.end = None
        else:
            self.head.prev = None
        self.counter -= 1

        return res_item

    def pop_back(self):
        if self.empty():
            return "error"
        cur_back = self.end
        res_item = cur_back.item
        self.end = self.end.prev
        if self.end is None:
            self.head = None
        else:
            self.end.next = None
        self.counter -= 1

        return res_item

    def front(self):
        if self.empty():
            return "error"
        return self.head.item

    def back(self):
        if self.empty():
            return "error"
        return self.end.item

    def size(self):
        return self.counter

    def clear(self):
        while not self.empty():
            self.pop_back()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    d = Deque()
    with open("input.txt") as f:
        for line in f:
            res = d.execute(line)
            print(res)
            if res == "bye":
                break
