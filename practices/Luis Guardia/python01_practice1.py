# excersice 1

def add(number_one , number_two):
    """
    :param numberOne:
    :param numberTwo:
    :return: the sum of 2 numbers.
    """
    result_of_adding_2_numbers = number_one + number_two
    print("The sum of", number_one,"+" ,number_two,"is",result_of_adding_2_numbers)

def subtract(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the subtract of 2 numbers.
    """
    result_of_subtract_2_numbers = number_one - number_two
    print("The subtract of", number_one, "-", number_two, "is", result_of_subtract_2_numbers)

def multiply(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the multiply of 2 numbers
    """
    result_of_multiply_2_numbers = number_one * number_two
    print("The multiply of", number_one, "*", number_two, "is", result_of_multiply_2_numbers)

def divide(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the divide of 2 numbers
    """
    result_of_divide_2_numbers = number_one / number_two
    print("The divide of", number_one, "/", number_two, "is", result_of_divide_2_numbers)

def get_module(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the module between 2 numbers
    """
    result_of_get_module_2_numbers = number_one % number_two
    print("The module of", number_one, "%", number_two, "is", result_of_get_module_2_numbers)

def raise_power(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the raise power of 2 numbers
    """
    result_of_raise_power_2_numbers = number_one ** number_two
    print("The raise Power of", number_one, "elevated to", number_two, "is", result_of_raise_power_2_numbers)

def bottom_rounding(number_one , number_two):
    """
    :param number_one:
    :param number_two:
    :return: the lower rounding of a division.
    """
    result_of_bottom_rounding_2_numbers = number_one // number_two
    print("The bottom Rounding of", number_one, "/", number_two, "is", result_of_bottom_rounding_2_numbers)

# call to add function
add(100 , 50)
# call to subtract function
subtract(500 , 250)
# call to multiply function
multiply(100 , 20)
# call to divide function
divide(250 , 50)
# call to getModule function
get_module(105 , 10)
# call to raisePower function
raise_power(10 , 2)
# call to bottomRounding function
bottom_rounding(99 , 10)


def perform_operation( number1, number2,operation):
    """
    :param number1:
    :param number2:
    :param operation:
    :return: performs a mathematical operation according to parameter operation.
    """
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    elif operation == "%":
        result = number1 % number2
    elif operation == "**":
        result = number1 ** number2
    else:
        result = "This operation is not valid"
    print("The result is:",result)

print(perform_operation(5,6,"*"))


