class Stack:

    def __init__(self, maxsize=100):
        self._items = [0 for _ in range(maxsize)]
        self._cur = -1

    def push(self, item):
        self._cur += 1
        self._items[self._cur] = item
        return "ok"

    def pop(self):
        if self._cur >= 0:
            res = self._items[self._cur]
            self._cur -=1
            return res
        return "error"

    def back(self):
        if self._cur >= 0:
            return self._items[self._cur]
        return "error"

    def size(self):
        return self._cur + 1

    def clear(self):
        self.__init__(len(self._items))
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break


