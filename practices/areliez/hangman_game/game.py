from practices.areliez.hangman_game.word_or_phrase import WordOrPhrase


class Game:
    def __init__(self):
        word_or_phrase = WordOrPhrase()
        self.word_or_phrase = word_or_phrase.get_value_of_words_or_phrases()

    def enter_value2(self):
        print("Enter a character please:")
        current_word_to_guess = []
        errors = 0
        self.create_array_for_word(current_word_to_guess)
        while errors < 6:
            character = input()

            character = self.is_one_character(character, current_word_to_guess)

            if character not in self.word_or_phrase:
                errors += 1
                if errors <= 5:
                    self.print_body_by_attempts(errors, current_word_to_guess)
                    print("Try again")
                else:
                    self.print_body_by_attempts(errors, current_word_to_guess)
                    print("You lost")
                    break
            else:
                current_word_to_guess = self.print_coincidence(character, current_word_to_guess)
                if "_" in current_word_to_guess:
                    self.print_current_coincidences(current_word_to_guess)
                    continue
                else:
                    self.print_current_coincidences(current_word_to_guess)
                    print("You win")
                    break

    def is_one_character(self, character, current_word):
        while len(character) > 1:
            print("Enter only one character")
            self.print_current_coincidences(current_word)
            character = input()
        if len(character) == 1:
            character = character.upper()
        return character

    def print_current_coincidences(self, current_word):
        for e in current_word:
            print(e, end=" ")
        print("\n")

    def create_array_for_word(self, current_word):
        while len(current_word) < len(self.word_or_phrase):
            current_word.append("_")
        self.print_current_coincidences(current_word)

    def print_body_by_attempts(self, errors, current_word):
        print("Error number:", errors)
        self.print_error(errors)
        print("\n")
        self.print_current_coincidences(current_word)

    def print_coincidence(self, character, current_word):
        pos = 0
        for char in self.word_or_phrase:
            if char == character:
                current_word[pos] = character
            pos += 1
        return current_word

    def print_error(self, number_attempt):
        body = ["\\", "/", "|", "O"]
        if number_attempt <= 6:
            if number_attempt == 1:
                print(body[3])
            elif number_attempt == 2:
                print(" ", body[3])
                print(body[1])
            elif number_attempt == 3:
                print(" ", body[3])
                print(body[1], body[2])
            elif number_attempt == 4:
                print(" ", body[3])
                print(body[1], body[2], body[0])
            elif number_attempt == 5:
                print(" ", body[3])
                print(body[1], body[2], body[0])
                print(body[1])
            else:
                print(" ", body[3])
                print(body[1], body[2], body[0])
                print(body[1], " ", body[0], "\n")
