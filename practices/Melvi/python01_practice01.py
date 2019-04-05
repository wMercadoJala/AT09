#Check to see if a string has the same amount of 'x's and 'o's.
#The method must return a boolean and be case insensitive. The string can contain any char.
#Examples input/output:
#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false

def xo(string):
    if ((string.count("x") + string.count("X")) == (string.count("o") + string.count("O"))):
        return True
    else:
        return False

print (xo('xxoo'))

#You might know some pretty large perfect squares. But what about the NEXT one?
#Complete the findNextSquare method that finds the next integral perfect square
#after the one passed as a parameter. Recall that an integral perfect square is
#an integer n such that sqrt(n) is also an integer.
#If the parameter is itself not a perfect square, than -1 should be returned.
#You may assume the parameter is positive.
#Examples:
#findNextSquare(121) --> returns 144
#findNextSquare(625) --> returns 676
#findNextSquare(114) --> returns -1 since 114 is not a perfect

import math
next = 0
def find_next_square(square):
    next = math.sqrt(square)
    if (next != 0):
        if (square%next == 0):
            return (next + 1)**2
        else:
            return -1
    return 1

print (find_next_square(121))

#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers.
#No floats or empty arrays will be passed.
#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#[10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

print (sum_two_smallest_numbers([19, 5, 42, 2, 77]))

#Very simple, given a number, find its opposite.
#Examples:
#1: -1
#14: -14
#-34: 34

def opposite(number): return number*(-1)

print (opposite(14))

#Complete the function which takes two arguments and returns all numbers which are divisible by given divisor. First argument is an array of numbers and the second is the divisor.
#Example
#divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

def divisible_by(numbers, divisor):
    list = []
    for i in numbers:
        if i % divisor == 0:
            list.append(i)
    return list

print (divisible_by([1, 2, 3, 4, 5, 6], 2))

#Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND
# y. All inputs are positive, non-zero digits.
#Example:
#is_divisible(3,1,3)--> True because 3 is divisible by 1 and 3
#is_divisible(12,2,6)--> True because 12 is divisible by 2 and 6
#is_divisible(100,5,3)--> False because 100 is not divisible by 3
#is_divisible(12,7,5)--> False because 12 is neither divisible by 7 nor 5

def is_divisible(number,diviblex,divisibley):
    return number % diviblex == 0 and number % divisibley == 0

print (is_divisible(12,2,6))

#Simple, remove the spaces from the string, then return the resultant string.
def no_space(string):
    texto = ""
    for i in string:
        if i != " ":
            texto += i

    return texto

print (no_space())

'''Write a program that reads a string and returns a table of the letters of the alphabet
 in alphabetical order which occur in the string together with the number of times each letter occurs. ​
Case should be ignored. A sample output of the program when the user enters the data ​
“ThiS is String with Upper and lower case Letters”,
'''
string = 'ThiS is String with Upper and lower case Letters'
letras = ['a','c','d','e','g','h','i','l','o','p','r','s','t','w','u']
dic = {}
for i in letras:
   dic.update({i:(string.count(i))})

print (dic)
