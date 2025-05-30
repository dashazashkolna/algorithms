class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1 << (self.n - 1).bit_length()
        self.tree = [0] * (2 * self.size)
        self.tree[self.size:self.size + self.n] = data
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index >>= 1
            new_val = self.tree[2 * index] + self.tree[2 * index + 1]
            if self.tree[index] == new_val:
                break
            self.tree[index] = new_val

    def find_max_prefix(self, max_sum):
        if self.tree[1] <= max_sum:
            return self.n
        idx = 1
        total = 0
        while idx < self.size:
            left = 2 * idx
            if total + self.tree[left] <= max_sum:
                total += self.tree[left]
                idx = left + 1
            else:
                idx = left
        return min(idx - self.size, self.n)


def main():
    n = int(input())
    weights = list(map(int, input().split()))
    st = SegmentTree(weights)

    m = int(input())
    output = []
    for _ in range(m):
        line = input().split()
        if line[0] == '1':
            res = st.find_max_prefix(int(line[1]))
            output.append(str(res))
        else:
            st.update(int(line[1]) - 1, int(line[2]))

    print('\n'.join(output))


if __name__ == "__main__":
    main()