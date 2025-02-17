
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size = 1000003
EMPTY = None
DELETED = 'DEL'

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, table
    count = 0
    table = [EMPTY] * size

def _hash(author):
    """ Генерує хеш для автора. """
    hash_value = 0
    prime = 31
    for char in author:
        hash_value = (hash_value * prime + ord(char)) % size
    return hash_value

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    i = _hash(author)
    while table[i] is not EMPTY and table[i] is not DELETED:
        if table[i][0] == author:
            table[i][1].add(title)
            return
        i = (i + 1) % size
    table[i] = (author, {title})

def find(author, title):
    """ Перевіряє, чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = _hash(author)
    while table[i] is not EMPTY:
        if table[i] is not DELETED and table[i][0] == author:
            return title in table[i][1]
        i = (i + 1) % size
    return False

def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = _hash(author)
    while table[i] is not EMPTY:
        if table[i] is not DELETED and table[i][0] == author:
            table[i][1].discard(title)
            if not table[i][1]:
                table[i] = DELETED
            return
        i = (i + 1) % size

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не містить книг заданого автора,
    то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = _hash(author)
    while table[i] is not EMPTY:
        if table[i] is not DELETED and table[i][0] == author:
            return sorted(table[i][1])
        i = (i + 1) % size
    return []


if __name__ == "__main__":
    init()
    addBook("Шевченко", "Кобзар")
    addBook("Шевченко", "Катерина")
    print(find("Шевченко", "лалаленд"))

    print(find("Шевченко", "Кобзар"))
    delete("Шевченко", "лалаленд")
    delete("Шевченко", "Кобзар")

    print(table)

    print(findByAuthor("Шевченко"))
