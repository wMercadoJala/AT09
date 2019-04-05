dict = dict(zip('abcdefghijklmnopqrstuvwxyz', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


def count_letters(message):
    '''
    Counts the quantity of the letters of a phrase.
    '''
    for letter in message:
        letter = letter.lower()
        try:
            dict[letter] = dict[letter] + 1
        except:
            pass
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for element in alpha:
        if dict[element] != 0:
            print(element, dict[element])


def catch_url(path):
    '''
    Capture a URL in a phrase.
    '''
    initial_position = path.find('http://')
    verification = path[initial_position: initial_position + 7]
    if verification == 'http://':
        result = path[initial_position + 7:]
        result = result[: result.find(' ')]
        print(result)
    else:
        print("Unknown path")


def replace(s, old, new):
    '''
    Replace all the portion that are the same like old with new.
    '''
    s.replace(old, new)
    print(s)


message = "ThiS is String with Upper and lower case Letters"
count_letters(message)
catch_url("This is the link http://www.algunlugar.com click on it")
song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
replace(song, "om", "am")
