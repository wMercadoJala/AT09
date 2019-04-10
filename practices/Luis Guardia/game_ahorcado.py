import random

class word_or_phrase:
    def __init__(self, phrase):
        self.phrase = phrase

    def setPhrase(self, phrase):
        self.phrase = phrase
    def getPhrase(self):
        return self.phrase

class game:
    letters_selected = list()
    word_inicial = list()
    phrase_find = list()
    phrase_new = list()
    def __init__(self):
        print ("Start the game")
        self.star_game(0)

    def star_game(self, number_attempts):
        self.number_attempts = number_attempts
        number_errors = 0
        print("Enter the string to search: ")
        word_search = input()
        phrase = word_or_phrase(word_search)
        word = phrase.getPhrase()
        for i in word:
            self.word_inicial.append(i)
            self.phrase_find.append(i)
            self.phrase_new.append("_")
        print("This is the word to be found:", word)
        while number_errors < 6:
            print("Enter a character or letter: ")
            character = input()
            if character in word:
                print("This Letter does exist")
                self.phrase_new = self.print_found_character(character, self.phrase_find, self.phrase_new)
                print(self.phrase_new)
                char = "_"
                if char in self.phrase_new:


                    pass
                else:
                    print("You won this game.")
                    break
            else:
                print("This letter does not exist:")
                self.print_attempt_failure(number_errors)
                print(self.phrase_new)
                number_errors = number_errors + 1
                if(number_errors == 6):
                    print("You lost this game.")
            number_attempts = number_attempts + 1

    def get_character(self, character):
        is_letter_valid = False
        character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]
        if character in self.letras_selected:
            is_letter_valid = False
        else:
            is_letter_valid = True
            self.letters_selected.append(character)
            print("The selected character is:", character)
        return is_letter_valid

    def print_found_character(self, character, phrase_find, phrase_new):
        for i in range(len (phrase_find)):
            if character == phrase_find[i]:
                phrase_new[i] = character
        return phrase_new

    def print_attempt_failure(self, number_errors):
        list_errors = ["\\", "/", "|", "\\", "/", "O"]
        print(list_errors[0: number_errors + 1], number_errors + 1, "errors")

inicio_game = game()
