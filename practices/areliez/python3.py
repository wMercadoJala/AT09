import re


def get_url(text):
    """
    Print the url in of a text.
    :param text: To fiend the url.
    :return:
    """
    index = text.find("http://")
    if index >= 0:
        new_text = text[index + 7: len(text)]
        index_space = new_text.find(" ")
        url = new_text[0: index_space]
        print("The url of text is: ", url)
    else:
        print("There isn't url in the text")


def count_chars(sentence):
    """
    Find the coincidence by letter.
    :param sentence:
    :return: 
    """
    coincidence = {}
    list_dict = []
    for letter in sentence:
        letter_fiend = letter

        if letter_fiend.isupper() or (re.match('[a-z]', letter_fiend)) is None:
            continue
        else:
            cant_of_letter = sentence.count(letter_fiend)
            coincidence[letter_fiend] = cant_of_letter

    for key, value in coincidence.items():
        list_dict.append((key, value))
    list_dict.sort()
    print("They are the number the coincidence by letter")
    for var in list_dict:
        print(var)
    print("\n")


# Test for fiend the coincidence by letter in a text.
count_chars("ThiS is String with Upper and lower * case Letters* /")

# Test to get the url in a text.
get_url("This is an http://myurl.fj for the example")
