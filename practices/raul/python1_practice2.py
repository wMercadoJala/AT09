#PRACTICE 03.1
number = 11
print("Number is even" if (number % 2) == 0 else "Number is odd")

var = 100
if ( var  == 100 ) : print("Value of expression is: %d" % (var))
print("That’s all!!")

#PRACTICE 03.2
def is_prime_number(param):
    is_prime = False
    divider = 2
    if param == 2:
        is_prime = True
    while divider <= (param - 1):
        if (param % divider) == 0:
            is_prime = False
            divider = param = 1
        else: is_prime = True
        divider += 1
    return is_prime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in range(len(numbers)):
    if is_prime_number(numbers[i]):
        print("Number: ", numbers[i], " is prime.")
    else: print("Number: ", numbers[i], " isn't prime.")
