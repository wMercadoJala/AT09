import random

class WordOrPhrase:

    name = "Hanggman Game"

    def __init__(self):
        self.words = ["Hello", "beautiful", "sometimes"]

    def get_word(self):
        return random.choice(self.words)

