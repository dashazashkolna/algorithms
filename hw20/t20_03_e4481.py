import math


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        pos += self.size
        self.tree[pos] = value
        pos >>= 1
        while pos >= 1:
            new_val = math.gcd(self.tree[2 * pos], self.tree[2 * pos + 1])
            if self.tree[pos] == new_val:
                break
            self.tree[pos] = new_val
            pos >>= 1

    def query(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                res = math.gcd(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = math.gcd(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res


n = int(input())
data = list(map(int, input().split()))

st = SegmentTree(data)

m = int(input())
output = []
for _ in range(m):
    parts = input().split()
    q = int(parts[0])
    l = int(parts[1])
    r = int(parts[2])
    if q == 1:
        res = st.query(l-1, r-1)
        output.append(str(res))
    elif q == 2:
        st.update(l-1, r)

print('\n'.join(output))
