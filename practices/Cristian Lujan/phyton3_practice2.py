# 1
def check_url(sentence):
    '''
    This method separates the urls from a sentence.
    :param sentence: sentence for analyze
    :return:
    '''
    words = sentence.split(" ")
    for url in words:
        if url.find("http://") == 0:
            print(url[7:])
        elif url.find("https://") == 0:
            print(url[8:])

check_url("http://www.codewars.com welcome https://www.deepl.com/es/")

# 2
def replace(song, old, new):
    '''
    this method converts letters from a phrase
    :param song: words for convert
    :param old: letter old
    :param new: letter new
    :return song:
    '''
    song = song.replace(old, new)
    print(song)
    return song

replace("Mississippi", "i", "I")

replace("I love spom! Spom is my favorite food.Spom, spom, yum!","o","a")

# 3
import string
def count_words(words):
    '''
    counts the number of repeated letters that exist in the phrase
    :param words: a sentence
    :return:
    '''
    my_string_new = words.replace(" ","")
    letters = string.ascii_lowercase
    letters_list = list(letters)
    my_list = list(my_string_new)
    comparison = {}
    count = 0
    for item in my_list:
        if item in letters_list:
            count = my_list.count(item)
            comparison[item] = count
    resultado = sorted(comparison.items())
    for indice in resultado:
        print(indice)

count_words('ThiS is String with Upper and lower case Letters')
