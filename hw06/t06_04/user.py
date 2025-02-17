class Node:
    def __init__(self, author: str, title: str):
        self.author: str = author
        self.titles: set = {title}
        self.next: [None | Node] = None


size: int = 1000003
slots: list[None | Node]


def hash(author: str) -> int:
    """ Генерує хеш для автора. """
    hash_value = 0
    prime = 31
    for char in author:
        hash_value = (hash_value * prime + ord(char)) % size
    return hash_value


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]


def addBook(author: str, title: str) -> None:
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.author == author:
            node.titles.add(title)
            return
        node = node.next

    new_node = Node(author, title)
    new_node.next = slots[i]
    slots[i] = new_node


def find(author: str, title: str) -> bool:
    """ Перевіряє, чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.author == author:
            return title in node.titles
        node = node.next
    return False


def delete(author: str, title: str) -> None:
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = hash(author)
    node = slots[i]
    if node is None:
        return

    if node.author == author:
        node.titles.discard(title)
        if not node.titles:
            slots[i] = node.next
        return

    prev = node
    node = node.next
    while node is not None:
        if node.author == author:
            node.titles.discard(title)
            if not node.titles:
                prev.next = node.next
            return
        prev = node
        node = node.next


def findByAuthor(author: str) -> list:
    """ Повертає список книг заданого автора.
    Якщо бібліотека не містить книг заданого автора,
    то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = hash(author)
    node = slots[i]
    while node is not None:
        if node.author == author:
            return sorted(node.titles)
        node = node.next
    return []