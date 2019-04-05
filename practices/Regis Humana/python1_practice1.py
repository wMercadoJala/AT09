def arithmetic_operators():
    '''
    This method does all of the arithmetic operations and print them.
    :return:
    '''
    sum_of_2_numbers = 2 + 2
    minus_of_2_numbers = 5 - 3
    multi_of_3_numbers = 1 * 5 * 3
    div_of_2_numbers = 6 / 3
    exp_of_9 = 9**2
    mod_of_20 = 20 % 3
    floor_division = 9 // 2

    print("Sum:", sum_of_2_numbers)
    print("Subtract:", minus_of_2_numbers)
    print("Multiply:", multi_of_3_numbers)
    print("Division:", div_of_2_numbers)
    print("Exponential:", exp_of_9)
    print("Module:", mod_of_20)
    print("Floor division:", floor_division)


def perform_operation(operation, number_one, number_two):
    '''
    This method does an arithmetic operation between two numbers and print them.
    :param operation:
    :param number_one:
    :param number_two:
    :return:
    '''
    result = 0
    if operation is '*':
        result = int(number_one) * int(number_two)
    elif operation is '+':
        result = int(number_one) + int(number_two)
    elif operation == '-':
        result = int(number_one) - int(number_two)
    elif operation == '/':
        result = int(number_one) / int(number_two)
    print("Operation Result is : ", result)


def number_comparision(number, list_number):
    '''
    This method takes a number and a list, and compare every element with the number.
    Then sum, subtract, multiply, division, mod.
    :param number:
    :param list_number:
    :return:
    '''
    equals = 0
    mayor = 0
    minor = 0
    different = 0
    sum_list = 0
    minus_list = 100
    multi_list = 1
    div_list = 100
    for element in list_number:
        if number == element:
            equals += 1
        elif number < element:
            mayor += 1
        elif number > element:
            minor += 1
        if number is not element:
            different += 1
        sum_list += element
        minus_list -= element
        multi_list *= element
        div_list /= element
    mod_list = multi_list
    mod_list %= sum_list

    print("Equal numbers :", equals)
    print("Mayor numbers :", mayor)
    print("Minor numbers :", minor)
    print("Different numbers :", different)
    print("Sum of list :", sum_list)
    print("Subtract of the list to 100 :", minus_list)
    print("Multiply of the list :", multi_list)
    print("Division of the list to 100 :", div_list)
    print("Module of multiply_list and sum_list :", mod_list)


print("***********ARITHMETIC OPERATORS*****************")
arithmetic_operators()
print("***********PERFORM OPERATION********************")
perform_operation("/", "2", "2")
print("***********NUMBER COMPARISION*******************")
number_comparision(7, [2, 2, 3, 5, 8, 8, 9])
