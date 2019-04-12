import string
def replace_character(phrase):
    '''
    :param phrase:
    :return: a string replacing the value of a character.
    '''
    print(phrase.replace("i", "I"))

word_test = "Mississippi"
# call to function replace_character
replace_character(word_test)

def replace_characters(phrase):
    '''
    :param phrase:
    :return: a string replacing the value of a or two characters.
    '''
    print(phrase.replace("om", "am"))
    print(phrase.replace("o", "a"))

phrase_test = "I love spom! Spom is my favorite food.Spom, spom, yum!"
# call to function replace_characters
replace_characters(phrase_test)

def show_url(string_url):
    '''
    :param string_url:
    :return: prints the valid url's of a phrase
    '''
    separate_words = string_url.split(" ")
    for url in separate_words:
        if url.find("http://") == 0:
            print(url[7:])

string_url = "http://www.chelseafc.com/en esta no es una url http://www.deepl.com/es/translator"
# call to function show_url
show_url(string_url)

diccionary = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0,
              'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
              'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0,
              'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
def find_strings(strings):
    '''
    :param strings: 
    :return: a dictionary with the number of repetitions of each character
    '''''
    for letter in strings:
        if letter.islower():
            ocurrencias = strings.count(letter)
            diccionary.update({letter:ocurrencias})

phrase = "This is string with upper and lower case letters”, would look this This"
# call to function find_strings
find_strings(phrase)
print(diccionary)

