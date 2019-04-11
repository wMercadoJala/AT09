#Suppose any line of text can contain at most one url that starts with “http://” and ends at the next
#space in the line. Write a fragment of code to extract and print the full url if it is present.
url="Encontrar esta url http://www.google.com/ e imprimirla http://www.aprende.org otro mas http://www.hotmail.com "
urlsplit = url.split()
list = []
for i in urlsplit:
    new = i.replace('http://', '')
    if (i != new): list.append(new)

print (list)


