import math


def is_odd_or_even(number):
    """
    This print if a number is odd or even.
    :param number: Number to evaluate.
    :return:
    """
    odd = "number is odd "
    even = "Number is ever"
    r = [even, odd][(number % 2) != 0]
    print(r)


def are_prime(values):
    """
    Return a list with the prime numbers of the value list entered.
    :param values: Values to evaluate if are prime numbers.
    :return: A list of prime numbers.
    """
    result = []
    for number in values:
        if number <= 1:
            continue
        elif number == 2:
            result.append(number)
        else:
            if is_prime(number) is True:
                result.append(number)
    return result


def are_prime2(min, max):
    """
    Return a list of prime numbers between the min and max number entered.
    :param min: Value min to find the prime numbers.
    :param max: Value max to find the prime numbers.
    :return: A prime number list between the min an max number entered.
    """
    result = []
    for number in range(min, max):
        if number <= 1:
            continue
        elif number == 2:
            result.append(number)
        else:
            if is_prime(number) is True:
                result.append(number)
    return result


def is_prime(number):
    """
    Evaluate if the number is prime.
    :param number: value to evaluate if is prime.
    :return: if is prime True else False.
    """
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime


def area_of_circle(r):
    """
    This method calculate the are of a circle sending the radio.
    :param r:
    :return:
    """
    if r > 10:
        print("Circle's area is: ", math.pi * r ** 2)
    else:
        print("To get the area you should enter a number greater than 10")


def sum_to(n):
    """
    This method do the sum of all integer numbers up to and including only until any value lower than 35.
    :param n: value lower than 35
    :return:
    """
    result = 0
    var = 1
    if n < 35:
        while var <= n:
            result = result + var
            var += 1
    else:
        print("You can enter only number less than 36")
    print("The sum is: ", result)


def days_in_month(month):
    """
    This print the month's days.
    :param month: Month to print number of days.
    :return:
    """
    days_31 = 31
    days_30 = 30
    if month is "January":
        days = days_31
    elif month is "February":
        days = 28
    elif month is "March":
        days = days_31
    elif month is "April":
        days = days_30
    elif month is "May":
        days = days_31
    elif month is "June":
        days = days_30
    elif month is "July":
        days = days_31
    elif month is "August":
        days = days_31
    elif month is "September":
        days = days_30
    elif month is "October":
        days = days_31
    elif month is "November":
        days = days_30
    elif month is "December":
        days = days_31
    else:
        days = "None"
    print(month, ": ", days, " days")


# Tests to area_of_circle.
area_of_circle(10)
area_of_circle(12)

# Test for sum_to.
sum_to(10)

# Test for days_in_month.
days_in_month("September")

# Test to evaluate if a number is odd or even.
is_odd_or_even(2)

# Test to get the prime numbers.
values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 30, 31, 36]
print("The next number are prime: ", are_prime(values1))

print("The next number are prime: ", are_prime2(1, 36))

