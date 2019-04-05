# Declaration of the value of the PI constant
PI = 3.1416

def is_even(number):
    """
    :param number:
    :return: print if a number is prime or not
    """
    print("The number:", number, "is even" if number % 2 == 0 else "The number:", number, "is not even")

# call to is_even function
is_even(2)

def generate_list(max, min):
    """
    :param max:
    :param min:
    :return: Function that shows whether a number is prime or not.
    """
    while min <= max:
        if is_prime(min):
            print("The number", min, "is prime")
        else:
            print("The number", min, "is not prime")
        min = min + 1

def is_prime(number):
    """
    :param number:
    :return: function that returns true if a number is prime
    """
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True

# call to function generate_list
generate_list(100, 90)


def circle(radio):
    """
    :param radio:
    :return: function that returns the area of a circle
    """
    if radio > 10:
        print ((radio ** 2) *PI)
    else:
        print ("The value of the radius must be greater than 10")

# call to the function circle
circle(12)

def sum_to(number):
    """
    :param number:
    :return: Function that returns the total sum given a number
    """
    index = 0
    total = 0
    while index <= number:
        if index > 35:
            break
        else:
            total += index
            index += 1
    print("La suma es", total)

# sum_to function call
sum_to(10)

diccionario = {'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
def dates(month):
    """
    :param month:
    :return: The number of days in a specific month
    """
    if(month in diccionario):
        print(month, "has:", diccionario[month], "days")
    else:
        print("None")

# call to function dates
dates("April")
