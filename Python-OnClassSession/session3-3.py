import random
def ex1():
    for _ in range(1,11):
        print(_)

def ex2():
    n = int(input("Enter n loops: "))
    sum = 0
    for _ in range(1,n+1):
        sum += _
    return sum

def ex3():
    n = int(input("Enter n loops: "))
    sum = 0
    print("Do you want to cal sum of even or odd?\n1.even\t2.odd")
    choice = input("Enter your choice: ")

    for _ in range(1,n+1):
        if choice == '1':
            if _ % 2 == 0:
                sum += _
        else:
            if _ % 2 != 0:
                sum += _
    return sum

def ex4():
    vowels = ['a','e','i','o','u']
    vowels_count = [0,0,0,0,0]
    total_count = 0
    string = input("Enter your string: ").strip().lower()
    for i in string:
        for j in range(len(vowels)):
            if i == vowels[j]:
                vowels_count[j] += 1
                total_count += 1

    for _ in range(len(vowels)):
        print(f'{vowels[_]}: {vowels_count[_]}')
    print('Total of vowels in string:',total_count)

def ex5():
    string = input('Enter your string: ')
    string = string
    count = 1
    for _ in string:
        if _ == " ":
            count += 1
    
    return f'Number of words in the sentence: {count}'

def ex6():
    num = random.randint(1,101)
    print("Choose your mode:\n1.easy \t2.medium\t3.hard")
    mode_choice = input("Enter your mode choice: ")

    if mode_choice == '1':
        mode = 10
    elif mode_choice == '2':
        mode = 6
    elif mode_choice == '3':
        mode = 4
    else:
        print("You enter a wrong choice")

    for _ in range(0,mode):
        choice = int(input("Enter your choice: "))
        if choice == num:
            print(f"You are right. You win!. The number is {num}")
            break
        else:
            if choice > num:
                print(f"Wrong, your number: {choice} is greater than the game guess")
            else:
                print(f"Wrong, your number: {choice} is less than the game guess")