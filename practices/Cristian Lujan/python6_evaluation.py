import random

class WordOrPhrase:
    word = ["cellphone", "computer", "keyboard", "mouse", "python", "windows"]
    def __init__(self):
        self.words = WordOrPhrase.word

    def print_word(self):
        print(self.words)

    def return_a_word(self):
        word_shufle = random.choice(WordOrPhrase.word)
        print(word_shufle)
        return word_shufle

# phrases = WordOrPhrase()
# phrases.print_word()
# phrases.return_a_word()
