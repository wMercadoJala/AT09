
# Practice 1 y 2
this_is_variable1 = int(input("first enter a integer number: "))
this_is_variable2 = int(input("final enter a integer number: "))
operator = input("enter the operator: ")

def operatores(date):
    '''
    verifies if the data is a valid operator
    :param date: the desired operator
    :return: if operator exist
    '''
    is_operator = False
    entrant = ["+", "-", "*", "/"]
    if (date in entrant):
        is_operator = True
    return is_operator

def arithmetic_operations(operator, this_is_variable1, this_is_variable2):
   if(operatores(operator)):
       if(operator == "+"):
           print("This is the result", this_is_variable1 + this_is_variable2, "with the operator", operator)
       elif(operator == "-"):
           print("This is the result", this_is_variable1 - this_is_variable2, "with the operator", operator)
       elif(operator == "*"):
           print("This is the result", this_is_variable1 * this_is_variable2, "with the operator", operator)
       else:
           print("This is the result", this_is_variable1 / this_is_variable2, "with the operator", operator)
   else:
        print("The operation you want to perform does not exist")


arithmetic_operations(operator, this_is_variable1, this_is_variable2)