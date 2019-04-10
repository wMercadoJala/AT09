from practices.raul.test.word_or_phrase import WordOrPhrase

class Game:

    def __init__(self, word, gamer_name):
        self.word = word
        self.gamer_name = gamer_name
        self.letter = ''
        self.visible_characters = self.get_empty_array()

    def get_empty_array(self):
        array = []
        for i in range(len(self.word)):
            array.append('_')
        return array

    def put_a_letter(self):
        res = False
        self.letter = input("Input a letter please!! ")
        if len(self.letter) > 1:
            print("Please put a alone letter.")
            self.put_a_letter()
        else:
            if (self.letter in self.word) != -1:
                res = True
            print("Great!!")

        return res

    def print_letter(self):
        for i in range(len(self.word)):
            if self.letter is self.word[i]:
                self.visible_characters[i] = self.letter
        print(self.visible_characters)





word = WordOrPhrase()
text = word.get_word()
print(text)
game = Game(text, "Raul")

if game.put_a_letter():
    print('positive ' + str(game.print_letter()))
else:
    print('negative')
