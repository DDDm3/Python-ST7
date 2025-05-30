import random
def ex():
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
ex()