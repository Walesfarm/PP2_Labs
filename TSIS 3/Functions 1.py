import math
import random
def mass_convert(grams):
  ounces = 28.3495231 * grams
  return ounces
  
def temperature_convert(fahrenheit):
  C = (5/9) * (fahrenheit - 32)
  return C

def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns,ns

def permutations(s, prefix=""):
    if len(s) == 0:
       print(prefix)
    else:
       for i in range(len(s)):
         permutations(s[:i] + s[i+1:], prefix + s[i])

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(num_list):
    prime_list = [num for num in num_list if is_prime(num)]
    return prime_list

def Master_Yoda(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    return word == word[::-1]

def histogram(int_list):
    for num in int_list:
        print("*" * num)

import random

def game():
    print("Hello! What is your name?")
    a = input()
    print(f"Well, {a}, I am thinking of a number between 1 and 20. Take a guess.")
    r = random.randint(1, 20)
    b = int(input())
    count = 0
    while b != r:
        if b < r:
            print("Your guess is too low.", "Take a guess", sep="\n")
            b = int(input())
        else:
            print("Your guess is too big.", "Take a guess", sep="\n")
            b = int(input())
        count += 1
    print(f"Good job, KBTU! You guessed my number in {count} guesses!")

game()