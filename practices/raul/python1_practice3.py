#PRACTICE 06
text = "this is my favorite url https://github.com/wMercadoJala/AT09 for API Testing"
text_with_init_url = text[text.find("https://"): len(text)]
post_end_url = text_with_init_url.find(" ")
url = text_with_init_url[0:post_end_url]
print("This is the url: ", url)


#PRACTICE 07
def replace(text, old_value, new_value):
    print(text.replace(old_value, new_value))


replace("Mississippi", "i", "I")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a")