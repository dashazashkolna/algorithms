import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        return None

    def top(self):
        if not self.empty():
            return self.items[-1]
        return None

    def empty(self):
        return len(self.items) == 0


def is_possible(n, permutation):
    station = Stack()
    current = 1
    target_ptr = 0

    while current <= n or not station.empty():
        if not station.empty() and station.top() == permutation[target_ptr]:
            station.pop()
            target_ptr += 1
            if target_ptr == n:
                return True
        elif current <= n:
            station.push(current)
            current += 1
        else:
            break

    return False


def process_input(input_data):
    lines = input_data.split('\n')
    ptr = 0

    while ptr < len(lines):
        line = lines[ptr].strip()
        ptr += 1

        if not line:
            continue

        n = int(line)
        if n == 0:
            break

        while True:
            if ptr >= len(lines):
                break

            line = lines[ptr].strip()
            ptr += 1

            if not line:
                continue

            if line == '0':
                print()
                break

            permutation = list(map(int, line.split()))
            if len(permutation) != n:
                continue

            if is_possible(n, permutation):
                print("Yes")
            else:
                print("No")


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_data = f.read()
    else:
        input_data = sys.stdin.read()

    process_input(input_data)


if __name__ == '__main__':
    main()