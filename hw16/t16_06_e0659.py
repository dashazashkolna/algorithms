import sys
from collections import defaultdict

class GameNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.is_leaf = False
        self.result = None

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())

    nodes = [None] * (n + 1)
    for i in range(1, n + 1):
        nodes[i] = GameNode(i)

    for i in range(2, n + 1):
        parts = sys.stdin.readline().split()
        node_type = parts[0]
        parent = int(parts[1])

        nodes[i].parent = nodes[parent]
        nodes[parent].children.append(nodes[i])

        if node_type == 'L':
            nodes[i].is_leaf = True
            nodes[i].result = int(parts[2])

    def evaluate(node, is_maximizing):
        if node.is_leaf:
            return node.result

        if is_maximizing:
            max_eval = -float('inf')
            for child in node.children:
                eval = evaluate(child, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = evaluate(child, True)
                min_eval = min(min_eval, eval)
            return min_eval

    result = evaluate(nodes[1], True)

    if result > 0:
        print("+1")
    elif result < 0:
        print("-1")
    else:
        print("0")

if __name__ == "__main__":
    main()