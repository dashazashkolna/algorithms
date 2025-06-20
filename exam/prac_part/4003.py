class TreeNode:

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.head = None
        self.left = None
        self.right = None

    def Insert(self, val: int) -> None:
        """Вставити число val в Бінарне Дерево Пошуку"""
        if self.head is None:
            self.head = TreeNode(val)

    def _helper_insert(self, node, val):
        if val < node.val:
            if node.val is None:
                node.left = TreeNode(val)
            else: self._helper_insert(node.left, val)
        else:
            if node.val is None:
                node.right = TreeNode(val)
            else: self._helper_insert(node.right, val)


    def SumLeft(self) -> int:
        """Вивести суму всіх лівих листків в дереві"""
        if self.head is None:
            return 0

        total = 0

        def dfs(self, node, is_left):
            if node is None:
                return

            if node.left is None and node.right is None and is_left:
                total += node.val
                return

            dfs(node.left, True)
            dfs(node.right, False)

        dfs(self.head, False)
        return total


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    tree = Tree()
    for num in numbers:
        tree.Insert(num)

    print(tree.SumLeft())
