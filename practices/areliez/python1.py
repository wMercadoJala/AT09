def perform_operation(operator, number_one, number_two):
    """
    This method do the basic operation sending the operator and two numbers.
    :param operator: The operator to do the operation.
    :param number_one: First value to do the operation.
    :param number_two: Second value to do the operation.
    :return:
    """
    if operator == "+":
        result = number_one + number_two
    elif operator == "-":
        result = number_one - number_two
    elif operator == "*":
        result = number_one * number_two
    elif operator == "/":
        result = divide(number_one, number_two)
    else:
        result = "You enter an invalid operator"
    return result


def divide(number_one, number_two):
    if number_two != 0:
        result = number_one / number_two
    else:
        result = "A number can't divide by 0"
    return result


# Value to execute perform_operation function
value_one = 5
value_two = 0
value_for_operator = "/"

# Print the result of perform_operation function.
print(perform_operation(value_for_operator, value_one, value_two))
