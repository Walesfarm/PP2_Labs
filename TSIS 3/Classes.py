import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self):
        self.x = int(input())
        self.y = int(input())
    def dist(self):
        m = (self.y)**2 - (self.x)**2
        print(math.sqrt(m))

class Gwido:
    def getString(self):
      self.string = input()
    def printString(self):
      print(self.string.upper())

class Shape:
    def area(self):
      return 0
class Square(Shape):
    def __init__(self, length):
      self.length = length
    def area(self):
      print(self.length**2)
class Rectangle(Shape):
    def __init__(self, length, width):
      self.length = length
      self.width = width
    def area(self):
      print(self.length * self.width)

class Account:
    def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance
    def deposit(self, amount):
      if amount > 0:
        self.balance += amount
        print(f"Deposited $ {amount}. New balance: $ {self.balance}")
      else:
        print("It is impossible")
    def withdraw(self, amount):
      if amount > 0:
        if amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew $ {amount}. New balance: $ {self.balance}")
        else:
          print("It is impossible")
      else:
        print("It is impossible")

is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers in the list:", prime_numbers)