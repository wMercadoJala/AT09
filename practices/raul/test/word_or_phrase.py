import random

class WordOrPhrase:

    name = "Hanggman Game"

    def __init__(self):
        self.words = ["HELLO", "BEAUTIFUL", "SOMETIMES"]

    def get_word(self):
        return random.choice(self.words)

