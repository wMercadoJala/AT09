import math


def area_of_circle(r):
    '''
    This method calculate the are of a circle sending the radio.
    :param r:
    :return:
    '''
    if r > 10:
        print("Circle's area is: ", math.pi * r ** 2)

    else:
        print("To get the area you should enter a number greater than 10")


def sum_to(n):
    '''
    This method do the sum of all integer numbers up to and including only until any value lower than 35.
    :param n: value lower than 35
    :return:
    '''
    result = 0
    var = 1
    if n < 35:
        while var <= n:
            result = result + var
            var += 1
    else:
        print("You can enter only number less than 36")
    print(result)


# Tests to area_of_circle.
area_of_circle(10)
area_of_circle(12)

# Test for sum_to
sum_to(10)
