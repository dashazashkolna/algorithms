class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


class List:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def _print_reverse(self, node: Node | None) -> None:
        """метод для рекурсивного зворотного виводу"""
        if node is None:
            return
        self._print_reverse(node.next)
        print(node.data, end=' ')

    def PrintReverse(self) -> None:
        """Вивести елементи Зв’язного Списку в зворотному порядку"""
        self._print_reverse(self.head)
        print()


if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())
    numbers = map(int, sys.stdin.readline().split())
    linked_list = List()
    for num in numbers:
        linked_list.addToTail(num)
    linked_list.Print()
    linked_list.PrintReverse()