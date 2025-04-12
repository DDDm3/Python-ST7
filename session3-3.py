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
    mode = choose_mode()
    win = 0
    played = 1

    print("\nTry to guess the number now!")
    if game_engine(num, mode):
        win += 1
        played += 1
    
    print("\nDo you want to play again?\n1. Yes\n2. No")
    retry_choice = int(input("Enter your option: "))
    
    while retry_choice == 1 or retry_choice == 2:
        if retry_choice == 1:
            print("\nNew game go!")
            r_mode = choose_mode()
            num = random.randint(1,101)
            if game_engine(num, r_mode):
                win += 1
                played += 1
        
        elif retry_choice == 2:
            print("Thanks for playing!")
            break
        
        else:
            retry_choice = int(input("Enter your option again: "))
        
        print("\nDo you want to play again?\n1. Yes\n2. No")
        retry_choice = int(input("Enter your option: "))

    print(f"You have played {played} rounds:\nwin {win} times\nlose {played-win} times")

def choose_mode():
    print("Choose your mode:\n1.easy \t2.medium\t3.hard")
    mode_choice = int(input("Enter your mode choice: "))

    while mode_choice >= 1 and mode_choice <= 3:
        if mode_choice == 1:
            mode = 9
            break
        elif mode_choice == 2:
            mode = 6
            break
        elif mode_choice == 3:
            mode = 4
            break
        else:
            print("You enter a wrong choice")
            mode_choice = int(input("Enter your mode choice again: "))
    
    return mode

def game_engine(num, mode):
    is_win = False
    mode_count = 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"You are right. You win!. The number is {num}")
        is_win = True
    else:
        if guess > num:
            print(f"Wrong, your number: {guess} is greater than the game guess")
        else:
            print(f"Wrong, your number: {guess} is less than the game guess")

        while guess != num and mode_count < mode:
            mode_count += 1
            guess = int(input("Enter your guess: "))
            
            if guess == num:
                print(f"You are right. You win!. The number is {num}. You have count {mode_count} times.")
                is_win = True
                break
            else:
                if guess > num:
                    print(f"Wrong, your number: {guess} is greater than the game guess")
                else:
                    print(f"Wrong, your number: {guess} is less than the game guess")
                
            if mode_count == mode:
                print("You have reached the maximum guess!")
                print("You lose T.T")
    
    return is_win
ex6()