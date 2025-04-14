class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)


def is_same_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.key != t2.key:
        return False
    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    if n != m:
        print(0)
    else:
        t1 = SearchTree(a[0])
        for x in a[1:]:
            t1.insert(x)

        t2 = SearchTree(b[0])
        for x in b[1:]:
            t2.insert(x)

        print(1 if is_same_tree(t1, t2) else 0)
