class Queue:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = self.Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def front(self):
        if self.is_empty():
            return
        return self.head.value

    def is_empty(self):
        return self.head is None



if __name__ == '__main__':
    n = int(input())
    player1 = Queue()
    player2 = Queue()

    for card in map(int, input().split()):
        player1.enqueue(card)
    for card in map(int, input().split()):
        player2.enqueue(card)

    max_moves = 200000
    move_count = 0
    winner = None

    while not player1.is_empty() and not player2.is_empty() and move_count < max_moves:
        card1 = player1.dequeue()
        card2 = player2.dequeue()

        if (card1 > card2 and not (card1 == n-1 and card2 == 0)) or (card1 == 0 and card2 == n-1):
            player1.enqueue(card1)
            player1.enqueue(card2)
        else:
            player2.enqueue(card1)
            player2.enqueue(card2)

        move_count += 1

    if player1.is_empty():
        print("second", move_count)
    elif player2.is_empty():
        print("first", move_count)
    else:
        print("draw")
