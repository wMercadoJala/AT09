from practices.raul.test.word_or_phrase import WordOrPhrase

class Game:
    def __init__(self, word, gamer_name):
        self.word = word
        self.gamer_name = gamer_name
        self.letter = ''

    def put_a_letter(self):
        res = False
        letter = input("Input a letter please!! ")
        if len(letter) > 1:
            print("Please put a alone letter.")
            self.put_a_letter()
        else:
            print("Great!!")
        for char in self.word:
            if char == letter:
                res = True
                break
        return res

    def print_letter(self, letter):
        i = 0
        for char in self.word:
            if char == letter:
                pass
            i += 1





word = WordOrPhrase()
print(word.get_word())

game = Game(word.get_word(), "Raul")
print(game.put_a_letter())
t = 'hello'
