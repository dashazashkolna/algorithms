EMPTY = None


class Contacts:
    def __init__(self, size):
        self._size = size
        self._table = [EMPTY for _ in range(size)]
        self._count = 0

    def hash(self, key):
        return key % self._size

    def set(self, key):
        i = self.hash(key)

        while self._table[i] is not EMPTY:
            if self._table[i] == key:
                return
            i = (i + 1) % self._size

        self._count += 1
        self._table[i] = key



if __name__ == "__main__":
    n = int(input())
    l = set(list(map(int, input().split())))
    c = Contacts(1000003)
    for x in l:
        c.set(x)

    print(c._count)