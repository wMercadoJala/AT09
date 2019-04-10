#Hangman Game quiz

import random


class WordOrPhrase:
    def __init__(self):
        self.words = ['hello', 'python', 'testing']

    def get_word(self):
        r = random.randint(0, len(self.words)-1)
        return self.words[r]

    def addnewword(self, word):
        self.words.append(word)
    # For add words to list words


class Game:
    guessed = []
    failKey = 0
    colgado = [" O ", " \\ ", " / ", " | ", " / ", " \\ "]
    w = WordOrPhrase()
    word = ""

    def __init__(self):
        pass

    def drawWord(self):
        new = ''
        for w in self.word:
            if w in self.guessed:
                new = new + w
            else:
                new = new + ' _ '
        print(new)

    def askKey(self):
        key = input('Guess a letter: ')
        self.guessed.append(key)
        if key not in self.word:
            self.failKey += 1

    def drawColgado(self):
        new = ''
        for i in range(self.failKey):
            new = new + self.colgado[i]
        print(new)

    def won(self):
        for i in self.word:
            if i not in self.guessed:
                return False
        return True

    def play(self):
        self.word = self.w.get_word()
        endgame = False
        while endgame is False:
            self.drawWord()
            self.askKey()
            self.drawColgado()
            if self.failKey > 5:
                endgame = True
            elif self.won():
                endgame = True

        if self.won():
            print("You win!")
        else:
            print("You loose!")


if __name__ == "__main__":
    newGame = Game()
    newGame.w.addnewword("java")
    newGame.play()


