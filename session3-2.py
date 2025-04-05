"""
Write a program to check a person is eligible for voting or not (saccept age from user)
Write a program to check whether a number entered by user is even or odd.
Write a program to check whether a number is divisible by 7 or not.
Write a program to check the last digit of a  number (entered by user) is divisible by 3 or not.
Write a Python program to guess a number between 1 and 9.
Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
"""
import random

def ex1():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You're ineligible for voting")
    else: print("You are eligible for voting")

def ex2():
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print(f"The {num} is even")
    else: print(f"The {num} is odd")

def ex3():
    num = int(input("Enter the number: "))
    if num % 7 == 0:
        print(f"The {num} is divisible by 7 ")
    else: print(f"The {num} is not divisible by 7 ")

def ex4():
    num = input("Enter the number: ")
    last_digit = int(num[-1])
    if last_digit % 3 == 0:
        print(f"The {last_digit} of {num} is divisible by 3")
    else: print(f"The {last_digit} of {num} is not divisible by 3")

def ex5():
    num = random.randint(range(1,10))
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("You win!")
    else:
        print("You lose!")

def ex6():
    num = input("Enter your number: ")
    if num == '1':
        print("Sunday")
    elif num == '2':
        print("Monday")
    elif num == '3':
        print("Tuesday")
    elif num == '4':
        print("Wednesday")
    elif num == '5':
        print("Thursday")
    elif num == '6':
        print("Friday")
    elif num == '7':
        print("Saturday")

choice = input("Enter your choice: ")
if choice == '1':
    ex1()
elif choice == '2':
    ex2()
elif choice == '3':
    ex3()
elif choice == '4':
    ex4()
elif choice == '5':
    ex5()
elif choice == '6':
    ex6()
else:
    print('Enter wrong, no exercises run')