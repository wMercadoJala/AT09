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
        self.letter = input("Input a letter please!! ").upper()
        self.letter.upper()
        if len(self.letter) > 1:
            print("Please put a alone letter.")
            self.put_a_letter()
        else:
            res = self.letter in self.word
        return res

    def print_letter(self):
        for i in range(len(self.word)):
            if self.letter == self.word[i]:
                print('into: ', i)
                self.visible_characters[i] = self.letter
        for i in range(len(self.visible_characters)):
            print(self.visible_characters[i], end = ' ')

    def print_hangman(self, part_number):
        hangman = ['/', '\\', '|', '/', '\\', '0']
        i = 0
        while i < part_number:
            print(hangman[i])
            i += 1

    def visible_characters_to_word(self):
        return ''.join(str(word) for word in self.visible_characters)


def init_game():
    lives = 6
    hangman_pos = 1
    word = WordOrPhrase()
    text = word.get_word()
    print("guess: ",text)
    game = Game(text, "Raul")
    while lives > 0 and (game.word != game.visible_characters_to_word()):
        if game.put_a_letter():
            game.print_letter()
            print('Great !!!')
        else:
            game.print_hangman(hangman_pos)
            lives -= 1
            hangman_pos += 1
            print('wrong !!!')
    if lives == 0:
        print("You lost :(")
    else:
        print('You are a winner!! :)')


init_game()
