import random


class WordOrPhrase:
    words = ["CAR", "TELEPHONE", "MIRROR", "COMPUTER", "BOTTLE"]

    def get_random_word(self):
        index = random.randint(-1, len(self.words) - 1)
        return self.words[index]


class Game:
    word = ''
    word_transform = ''
    word_player = ''
    body = ''
    time = 0
    lost = False

    def __init__(self):
        self.get_word = WordOrPhrase()
        self.word = self.get_word.get_random_word()
        self.word_player = len(self.word) * '_'
        self.word_transform = self.word
        print(self.word)

    def is_character_in_word(self, character):

        if self.word.find(character) != -1:
            auxiliary = self.word_transform
            auxiliary = auxiliary.replace(character, "#")
            self.word_transform = auxiliary
            self.lost = True
            print("Exist this character")
        else:
            self.lost = False
            self.time += 1
            print("Don't exist this character")

    def print_word_player(self):
        index = 0
        result = ''
        for character in self.word:
            try:
                if '#' == self.word_transform[index]:
                    result = result + character
                else:
                    result = result + "_"
            except IndexError:
                result = self.word_player
            index += 1
        self.word_player = result
        print(result)

    def is_player_guess(self):
        hanged = '\/|\/O'
        if self.lost is False:
            self.body = hanged[0: self.time]
            if hanged == self.body:
                print("YOU LOSE")
                print(self.word)
        if self.word == self.word_player:
            print("YOU WIN!!!")
            self.time = 6
        print(self.body)


def main():
    test = Game()
    while test.time != 6:
        test.is_character_in_word(input("PUT YOUR LETTER IN UPPER CASE: "))
        test.print_word_player()
        test.is_player_guess()


main()
