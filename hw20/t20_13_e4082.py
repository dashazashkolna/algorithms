import sys

input = sys.stdin.read

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = (1 if data[i] > 0 else -1 if data[i] < 0 else 0)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] * self.tree[2 * i + 1]

    def query(self, l, r):
        res = 1
        l += self.n
        r += self.n + 1
        while l < r:
            if l % 2 == 1:
                res *= self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res *= self.tree[r]
            l //= 2
            r //= 2
        return res

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = (1 if value > 0 else -1 if value < 0 else 0)
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] * self.tree[2 * idx + 1]


def main():
    data = input().splitlines()
    index = 0
    result = []

    while index < len(data):
        n, k = map(int, data[index].split())
        index += 1
        arr = list(map(int, data[index].split()))
        index += 1

        seg_tree = SegmentTree(arr)
        answer = []

        for _ in range(k):
            query = data[index].split()
            index += 1
            if query[0] == 'P':
                i, j = map(int, query[1:])
                product = seg_tree.query(i - 1, j - 1)
                answer.append('0' if product == 0 else '+' if product > 0 else '-')
            elif query[0] == 'C':
                i, v = map(int, query[1:])
                seg_tree.update(i - 1, v)

        result.append(''.join(answer))

    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
