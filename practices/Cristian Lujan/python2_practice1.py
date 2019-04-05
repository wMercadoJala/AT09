def odd_even_number(number):
    '''
    this method find out if a number is even or odd
    :param number: number for compared
    :return: A message result
    '''
    print("The number is odd" if number % 2 == 0 else "The number is even")

def area_of_circle(radio):
    '''
    This method returns the area with a radius
    :param radio:
    :return: area of the circle
    '''

    from math import pi
    radio = float(input("Input the radius of the circle : "))
    if radio > 10:
        print("The area of the circle with radius " + str(radio) + " is: " + str(pi * radio ** 2))
    else:
        print("The radius has mayor of 10")

def number_prime():
    num1 = int(input("first enter a integer number: "))
    num2 = int(input("final enter a integer number: "))
    if (num1 > 0) or (num2 > 0):
        for i in range(num1, num2):
            increasing = 2
            is_prime = True
            while is_prime and increasing < i:
                if i % increasing == 0:
                    is_prime = False
                else:
                    increasing += 1
            if is_prime:
                print(i, "es primo")
    else:
        print("ingrese un valor correcto")
