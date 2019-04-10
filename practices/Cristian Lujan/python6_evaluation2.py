from python6_evaluation import WordOrPhrase


class Game(WordOrPhrase):

    def __init__(self):
        self.word_guess = WordOrPhrase()

    def game_run(self):
        hanged = ['''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']
        list_word_guess = []
        list_word_show = []
        attempts = 6
        print_hanged = ''
        index = 0
        print(self.word_guess)
        list_word_guess = list(self.word_guess.return_a_word())
        for item in list_word_guess:
            list_word_show.append('_')
        letter = ''

        run = True
        while run:
            ## Mostramos la palabra a adivinar
            print(' '.join(list_word_show))

            ## Pedimos una letra
            letter_input = input('Give me a letter: ')

            ## Convertimos todas las letras en minusculas
            letter = letter_input.lower()

            ## Comprueba si se ha equivocado
            fallo = False
            if letter not in list_word_guess:
                ## Ha fallado
                fallo = True

                attempts = attempts - 1
                print('You failed!!! You have {attempts} attempts'.format(attempts = attempts))
                print_hanged = (hanged[index])
                index += 1

            else:
                ## Adivinado, sustituimos
                for key, value in enumerate(list_word_guess):
                    if value == letter:
                        list_word_show[key] = value
            ### Comprueba si ha terminado la partida se le acaban los intentos
            if attempts <= 0:
                run = False
                print('You have lost, the word was "{words}"'.format(words = ''.join(list_word_guess)))
            elif list_word_guess == list_word_show:
                run = False
                print('You have won, the word was "{words}"'.format(words = ''.join(list_word_guess)))
            print(print_hanged)

run = Game()
run.game_run()