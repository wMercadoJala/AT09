value1_for_arithmetic_operation = 10
value_2_for_arithmetic_operation = 2


def operation_arithmetic():
    """
    Print operations arithmetic.
    :return:
    """
    print("Operations arithmetic")
    addition = value1_for_arithmetic_operation + value_2_for_arithmetic_operation
    subtraction = value1_for_arithmetic_operation - value_2_for_arithmetic_operation
    division = value1_for_arithmetic_operation / value_2_for_arithmetic_operation
    modulus = value1_for_arithmetic_operation % value_2_for_arithmetic_operation
    exponent = value1_for_arithmetic_operation ** value_2_for_arithmetic_operation
    floor_division = value1_for_arithmetic_operation // value_2_for_arithmetic_operation
    print("Addition: ", addition)
    print("subtraction: ", subtraction)
    print("Division: ", division)
    print("Modulus: ", modulus)
    print("Exponent: ", exponent)
    print("Floor division: ", floor_division, "\n")


def perform_operation(operator, number_one, number_two):
    """
    This method do the basic operation sending the operator and two numbers.
    :param operator: The operator to do the operation.
    :param number_one: First value to do the operation.
    :param number_two: Second value to do the operation.
    :return:
    """
    print("Perform operation")
    int_value_1 = int(number_one)
    int_value_2 = int(number_two)
    if operator == "+":
        result = int_value_1 + int_value_2
    elif operator == "-":
        result = int_value_1 - int_value_2
    elif operator == "*":
        result = int_value_1 * int_value_2
    elif operator == "/":
        result = divide(int_value_1, int_value_2)
    else:
        result = "You enter an invalid operator"
    return result


def divide(number_one, number_two):
    if number_two != 0:
        result = number_one / number_two
    else:
        result = "A number can't divide by 0"
    return result


# Print the operation arithmetic
operation_arithmetic()

# Value to execute perform_operation function
value_one = "5"
value_two = "0"
value_for_operator = "/"

# Print the result of perform_operation function.
print(perform_operation(value_for_operator, value_one, value_two))
