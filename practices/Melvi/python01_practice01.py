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
#findNextSquare(114) --> returns -1 since 114 is not a perfect.

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

#Complete the function which takes two arguments and returns all numbers which are divisible
#by given divisor. First argument is an array of numbers and the second is the divisor.
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

print (no_space("H o l a ."))

'''Write a program that reads a string and returns a table of the letters of the alphabet
in alphabetical order which occur in the string together with the number of times each letter occurs. ​
Case should be ignored. A sample output of the program when the user enters the data ​
“ThiS is String with Upper and lower case Letters”,
'''
input_text = 'ThiS is String with Upper and lower case Letters'
lista = ['a','c','d','e','g','h','i','l','o','p','r','s','t','w','u']
dic = {}
for i in lista:
   dic.update({i:(input_text.count(i))})

print (dic)

#Refactor
'''Write a program that reads a string and returns a table of the letters of the alphabet
in alphabetical order which occur in the string together with the number of times each letter occurs. ​
Case should be ignored. A sample output of the program when the user enters the data ​
“ThiS is String with Upper and lower case Letters”,
'''


def ordered_count(input_text):
    lista = []
    tam = len(input_text)
    text = input_text
    while tam > 0:
        lista.append((text[0], input_text.count(text[0])))
        text = text.replace(text[0], "")
        tam = len(text)

    return lista

#test
print (ordered_count("ThiS is String with Upper and lower case Letters"))

'''Your task is to remove all duplicate words from string, leaving only single (first) words entries.
Example:
Input:
'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output:
'alpha beta gamma delta' '''

def remove_duplicate_words(text):
    lista = ""
    newtext = text.split()
    while newtext:
        lista = lista + newtext[0] + " "
        text = text.replace(newtext[0], "")
        newtext = text.split()

    lista = lista.strip()
    return lista
#Test
print (remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

'''A Rule of Divisibility by 7
A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits. Continue to do this until a number known to be divisible or not by 7 is obtained; you can stop when this number has at most 2 digits because you are supposed to know if a number of at most 2 digits is divisible by 7 or not.
The original number is divisible by 7 if and only if the last number obtained using this procedure is divisible by 7.
Examples:
1 - m = 371 -> 37 − (2×1) -> 37 − 2 = 35 ; thus, since 35 is divisible by 7, 371 is divisible by 7.
The number of steps to get the result is 1.
2 - m = 1603 -> 160 - (2 x 3) -> 154 -> 15 - 8 = 7 and 7 is divisible by 7.'''

def seven(number):
    cont = 0
    while number > 99:
        a = number % 10
        b = number // 10
        number = b-(a*2)
        cont += 1

    return tuple((number,cont) )
#Test
print (seven(1063))

''' FizzBuzz
Return an array containing the numbers from 1 to N, where N is the parametered value.
N will never be less than 1 (in C#, N might be less then 1).
C# ONLY: If N is smaller then or equal to 0, throw an ArgumentOutOfRangeException!
Replace certain values however if any of the following conditions are met:
If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead'''


def fizzbuzz(number):
    lista = []
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                lista.append("FizzBuzz")
            else:
                lista.append("Fizz")
        else:
            if i % 5 == 0:
                lista.append("Buzz")
            else:
                lista.append(i)

    return lista
#Test
print (fizzbuzz(30))

'''Reverse words
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.
Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''
import re
def reverse_words(text):
    newstr = re.split(r'(\s+)', text)
    result = ""
    for j in newstr:
        new = ""
        for i in range(len(j) - 1, -1, -1):
            new = new + j[i]
        result += new

    return result

#Test
print (reverse_words("double  spaces"))

'''Sum Factorial
Factorials are often used in probability and are used as an introductory problem for looping constructs.
In this kata you will be summing together multiple factorials.
Here are a few examples of factorials:
4 Factorial = 4! = 4 * 3 * 2 * 1 = 24
6 Factorial = 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
In this kata you will be given a list of values that you must first find the factorial, and then return their sum.
For example if you are passed the list [4, 6] the equivalent mathematical expression would be 4! + 6! which would equal 744.
'''

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_factorial(lst):
    suma = 0
    for i in lst:
        suma = suma + factorial(i)

    return suma
#Test
print (sum_factorial([4,6]))

'''Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
'''
def replace_exclamation(text):
    list=["a","e","i","o","u","A","E","I","O","U"]
    for i in list:
        text=text.replace(i,"!")
    return text

#Test
print (replace_exclamation("ABCDE"))

'''Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
Remove n exclamation marks in the sentence from left to right. n is positive integer.
Examples
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"'''
def remove(text, number):
    text=text.replace("!","",number)
    return text

#test
print (remove("!!!Hi !!hi!!! !hi",1))
print (remove("!!!Hi !!hi!!! !hi",5))