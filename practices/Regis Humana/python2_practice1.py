def is_even(number):
    '''
    Return a message if the number is odd or even.
    :param number: to examine.
    :return: print a message.
    '''
    print("The number is even" if number%2 == 0 else "The number is odd")


def is_prime(min, max):
    '''
    This method determinate if the number between min and max is prime or not.
    :param min: under max.
    :param max: more than min.
    :return: print of prime or not prime numbers.
    '''
    for number in range(min, max + 1):
        count = 0
        num = 1
        while num <= number:
            if number % num == 0:
                count += 1
            num += 1
        print((str(number) + " is a prime") if count is 2 else (str(number) + " is not a prime"))


def area_of_circle(radius):
    '''
    Calculate the area of radius.
    :param radius: length of center to the circumference.
    :return: print the radius is more than 10.
    '''
    PI = 3.1416
    result = radius**2 * PI
    if result > 10:
        print("Circle Area:", result)
    else:
        print("Circle Area is less than 10")


def sum_to(number):
    '''
    Sum of all the numbers  until the number variable and until 35.
    :param number:
    :return: Total sum.
    '''
    num = 1
    result = 0
    while num <= number:
        if num < 35:
            result += num
        else:
            break
        num += 1
    print(result)


def days_in_month(month):
    '''
    Compare the month that is send it and give the days of that month.
    :param month:
    :return:
    '''
    if month is "January":
        result = 31
    elif month is "February":
        result = 28
    elif month is "March":
        result = 31
    elif month is "April":
        result = 30
    elif month is "May":
        result = 31
    elif month is "June":
        result = 30
    elif month is "July":
        result = 31
    elif month is "August":
        result = 31
    elif month is "September":
        result = 30
    elif month is "October":
        result = 31
    elif month is "November":
        result = 30
    elif month is "December":
        result = 31
    else:
        result = "None"
    print("Days of the month are:", result)


is_even(2)
is_prime(1, 23)
area_of_circle(5)
area_of_circle(1)
sum_to(10)
sum_to(40)
sum_to(50)
days_in_month("June")
days_in_month("Hello")
