MOD = 1000000007
Q = 127


class TreeNode:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.children = []


def build_tree(n, parents, values):
    nodes = [TreeNode(i, values[i]) for i in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].children.append(nodes[i])
    return root, nodes

def dfs(node, answers):
    if not node.children:
        return [node.value]

    all_values = []
    for child in node.children:
        child_vals = dfs(child, answers)
        all_values.extend(child_vals)

    all_values.append(node.value)

    if len(all_values) >= 2:
        all_values.sort()
        min_diff = min(all_values[i+1] - all_values[i] for i in range(len(all_values)-1))
        answers[node.idx] = min_diff

    return all_values

def solve(n, parent_list, value_list):
    root, nodes = build_tree(n, parent_list, value_list)
    answers = {}
    dfs(root, answers)

    result = 0
    for i, val in answers.items():
        result = (result + val * pow(Q, i, MOD)) % MOD

    return result

if __name__ == "__main__":
    n = int(input())
    parents = []
    values = []
    for _ in range(n):
        p, v = map(int, input().split())
        parents.append(p)
        values.append(v)

    print(solve(n, parents, values))