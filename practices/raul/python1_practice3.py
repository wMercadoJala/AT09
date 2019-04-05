#PRACTICE 06
text = "this is my favorite url https://github.com/wMercadoJala/AT09 for API Testing"
text_with_init_url = text[text.find("https://"): len(text)]
post_end_url = text_with_init_url.find(" ")
url = text_with_init_url[0:post_end_url]
print("This is the url: ", url)


#PRACTICE 07
def replace_word(text, old_value, new_value):
    print(text.replace(old_value, new_value))


replace_word("Mississippi", "i", "I")
replace_word("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am")
replace_word("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a")


#PRACTICE 08
def counter_letter_in_text(text):
    text_without_space  = text.replace(" ", "")
    print(text_without_space)
    cont = 0
    dic = {}
    for character in text_without_space:
        char_lower = character.lower()
        for charactertwo in text_without_space:
            if (char_lower == charactertwo.lower()) and (character != " "):
                cont += 1

        dic[char_lower] = cont
        cont = 0
    for i in sorted(dic):
        print((i, dic[i]))


counter_letter_in_text("ThiS is String with Upper and lower case Letters")


