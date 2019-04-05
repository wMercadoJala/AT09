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
for i in range(3, len(numbers)):
    if is_prime_number(numbers[i]):
        print("Number: ", numbers[i], " is prime.")
    else: print("Number: ", numbers[i], " isn't prime.")

#PRACTICE 04.1
def area_of_circle(radio):
    if radio > 10:
        pi = 3.1415
        area = pi * (radio ** 2)
        print("Area is equal: ", area)
    else: print("the value of ratio have to greater of 10")


area_of_circle(11)

#PRACTICE 04.2
def sum_to(until_number):
    sum = 0
    addition = 1
    max_number = 35
    while (addition <= until_number) and (addition <= max_number):
        sum += addition
        addition += 1
    print(sum)
sum_to(50)

#PRACTICE 05
def is_valid_month(month):
    is_valid = False
    valid_month = {"January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December"}
    if month in valid_month: is_valid = True
    return is_valid

def days_in_month(month):
    if is_valid_month(month):
        if month == "January": print(month, "has ", 31, "days")
        elif month == "February": print(month, "has ", 28, "days")
        elif month == "March": print(month, "has ", 31, "days")
        elif month == "April": print(month, "has ", 30, "days")
        elif month == "May": print(month, "has ", 31, "days")
        elif month == "Jun": print(month, "has ", 30, "days")
        elif month == "July": print(month, "has ", 31, "days")
        elif month == "August": print(month, "has ", 31, "days")
        elif month == "September": print(month, "has ", 30, "days")
        elif month == "October": print(month, "has ", 31, "days")
        elif month == "November": print(month, "has ", 30, "days")
        elif month == "December": print(month, "has ", 31, "days")
    else: print("None")
days_in_month("July")
