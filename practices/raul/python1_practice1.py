#PRACTICE 01
value_of_first_number = 5
value_of_second_number = 2
result_of_adds_value_of_first_number_and_value_of_second_number = value_of_first_number + value_of_second_number
print("Result of addition two values: ", value_of_first_number, " + ", value_of_second_number, " = ", result_of_adds_value_of_first_number_and_value_of_second_number)
result_of_subtract_value_of_first_number_and_value_of_second_number = value_of_first_number - value_of_second_number
print("Result of subtraction between two values: ", value_of_first_number, " - ", value_of_second_number, " = ", result_of_subtract_value_of_first_number_and_value_of_second_number)
result_of_multiplies_value_of_first_number_and_value_of_second_number = value_of_first_number * value_of_second_number
print("Result of multiplication two values: ", value_of_first_number, " * ", value_of_second_number, " = ", result_of_multiplies_value_of_first_number_and_value_of_second_number)
result_of_divides_value_of_first_number_and_value_of_second_number = value_of_first_number // value_of_second_number
print("Result of division two values: ", value_of_first_number, " / ", value_of_second_number, " = ", result_of_divides_value_of_first_number_and_value_of_second_number)
result_of_modulus_value_of_first_number_and_value_of_second_number = value_of_first_number % value_of_second_number
print("Result of modulus between two values: ", value_of_first_number, " % ", value_of_second_number, " = ", result_of_modulus_value_of_first_number_and_value_of_second_number)
result_of_exponent_value_of_first_number_and_value_of_second_number = value_of_first_number ** value_of_second_number
print("Result of exponent two values: ", value_of_first_number, "(" , value_of_second_number, ")", " = ", result_of_exponent_value_of_first_number_and_value_of_second_number)


#PRACTICE 02
def make_operation(operator, value_first, value_second):
    result = 0
    if empty_operator(operator):
        if operator == "+":
            result = value_first + value_second
        elif operator == "-":
            result = value_first - value_second
        elif operator == "*":
            result = value_first * value_second
        elif operator == "/":
            result = value_first // value_second
        elif operator == "%":
            result = value_first % value_second
        print("The result of use this operator: ", "'", operator, "'", "between these two values: ", value_first, " and", value_second, " is:")
    else:
        print("The operator : ", operator, " isn't valid!!", )
    return result


def empty_operator(operator):
    is_operator = False
    operators = ["+", "-", "*", "/", "%"]
    if operator in operators:
        is_operator = True
    return is_operator


print(make_operation("+", 10, 3))
print(make_operation("-", 10, 3))
print(make_operation("*", 10, 3))
print(make_operation("/", 10, 3))
print(make_operation("%", 10, 3))

