class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key < key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)
        elif self.key > key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)

    def is_path(self, path, i=0):
        if i >= len(path) or path[i] != self.key:
            return False
        elif i == len(path) - 1:
            return self.left is None and self.right is None
        next = path[i+1]
        if next < self.key and self.left:
            return self.left.is_path(path, i+1)
        elif next > self.key and self.right:
            return self.right.is_path(path, i+1)
        else:
            return False


if __name__ == '__main__':
    n = list(map(int, input().split()))
    tree = SearchTree(n[0])
    for x in n[1:]:
        tree.insert(x)

    if tree.is_path(n):
        print("YES")
    else:
        print('NO')

