import random


class WordOrPhrase:
    words_or_phrases = []

    def __init__(self):
        self.words_or_phrases = ['JALA', 'WORLD 2', 'JALA FUNDATION', 'QA AND QC', 'AT-09']

    def get_value_of_words_or_phrases(self):
        return random.choice(self.words_or_phrases)
