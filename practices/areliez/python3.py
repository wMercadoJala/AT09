def count_chars(sentence):
    coincidence = {}
    list_dict = []
    for letter in sentence:
        letter_fiend = letter
        if letter_fiend.isupper() or letter_fiend == " ":
            continue
        else:
            cant_of_letter = sentence.count(letter_fiend)
            coincidence[letter_fiend] = cant_of_letter

    for key, value in coincidence.items():
        list_dict.append((key, value))
    list_dict.sort()
    for var in list_dict:
        print(var)


count_chars("ThiS is String with Upper and lower case Letters")
