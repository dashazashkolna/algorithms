import re

class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def _hash(self, key):
        h = 0
        for char in key:
            h = h * 31 + ord(char)
        return h % self.size

    def insert(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.size
        self.table[index] = key
        self.count += 1

    def exists(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
        return False


def clean_word(word):
    return re.sub(r"[.,:;!?\"'-]", "", word).lower()


def check_text(dictionary, text):
    known_words = HashTable()
    for word in dictionary:
        known_words.insert(word)

    text_words = set()
    for line in text:
        for word in re.findall(r"\b[a-zA-Z]+\b", line):
            text_words.add(clean_word(word))

    missing_in_text = {word for word in dictionary if word not in text_words}
    unknown_in_text = {word for word in text_words if not known_words.exists(word)}

    if not unknown_in_text and not missing_in_text:
        return "Everything is going to be OK."
    elif unknown_in_text:
        return "Some words from the text are unknown."
    else:
        return "The usage of the vocabulary is not perfect."


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readline().split()
        n, m = int(data[0]), int(data[1])

        dictionary = [clean_word(f.readline().strip()) for _ in range(n)]
        text = [f.readline().strip() for _ in range(m)]

    print(check_text(dictionary, text))
