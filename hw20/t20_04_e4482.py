import math


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        self.tree_gcd = [0] * (2 * self.size)
        self.tree_lcm = [1] * (2 * self.size)

        for i in range(self.n):
            self.tree_gcd[self.size + i] = data[i]
            self.tree_lcm[self.size + i] = data[i]

        for i in range(self.size - 1, 0, -1):
            self.tree_gcd[i] = math.gcd(self.tree_gcd[2*i], self.tree_gcd[2*i+1])
            self.tree_lcm[i] = self.lcm(self.tree_lcm[2*i], self.tree_lcm[2*i+1])

    def lcm(self, a, b):
        return a * b // math.gcd(a, b) if a and b else 0

    def update(self, pos, value):
        pos += self.size
        self.tree_gcd[pos] = value
        self.tree_lcm[pos] = value
        pos >>= 1

        while pos >= 1:
            new_gcd = math.gcd(self.tree_gcd[2*pos], self.tree_gcd[2*pos+1])
            new_lcm = self.lcm(self.tree_lcm[2*pos], self.tree_lcm[2*pos+1])

            if self.tree_gcd[pos] == new_gcd and self.tree_lcm[pos] == new_lcm:
                break

            self.tree_gcd[pos] = new_gcd
            self.tree_lcm[pos] = new_lcm
            pos >>= 1

    def query(self, l, r):
        res_gcd = 0
        res_lcm = 1
        l += self.size
        r += self.size

        while l <= r:
            if l % 2 == 1:
                res_gcd = math.gcd(res_gcd, self.tree_gcd[l])
                res_lcm = self.lcm(res_lcm, self.tree_lcm[l])
                l += 1
            if r % 2 == 0:
                res_gcd = math.gcd(res_gcd, self.tree_gcd[r])
                res_lcm = self.lcm(res_lcm, self.tree_lcm[r])
                r -= 1
            l >>= 1
            r >>= 1

        return res_gcd, res_lcm


n = int(input())
data = list(map(int, input().split()))

st = SegmentTree(data)

m = int(input())
output = []
for _ in range(m):
    parts = input().split()
    q = int(parts[0])
    l = int(parts[1]) - 1
    r = int(parts[2]) - 1

    if q == 1:
        gcd_val, lcm_val = st.query(l, r)

        if gcd_val < lcm_val:
            output.append("wins")
        elif gcd_val > lcm_val:
            output.append("loser")
        else:
            output.append("draw")
    elif q == 2:
        st.update(l, int(parts[2]))

print('\n'.join(output))
