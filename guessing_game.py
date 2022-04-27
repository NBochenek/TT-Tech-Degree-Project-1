"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
win_count = 0
best_score = 0

def start_game(win_count, best_score):
    goal_number = random.randint(1, 10)
    user_guess = 0
    guess_count = 1
    print("Hello and welcome to the guessing game! A number has been generated between 1 and 10. Can you guess what it is?")
    print(f"Your current win count is {win_count}.")
    print(f"Your best score is {best_score}.")
    
    while user_guess != goal_number:
        try:
            user_guess = int(input("Please guess a number between 1 and 10:     "))
            if (user_guess > 10) or (user_guess < 1):
                print("Sorry, your guess is out of bounds. Please try again.")
            elif user_guess > goal_number:
                print("It's lower.")
                guess_count += 1
    
            elif user_guess < goal_number:
                print("It's higher.")
                guess_count += 1
        except ValueError:
            print("Error! Please enter a number with only Arabic numerals.")

    else:
        print("You win!", f"The number was {goal_number}.", f"You found it in {guess_count} guesses!.")
        if guess_count < best_score:
            print("You've beat the best score!")
        play_again = input("Do you want to play again? Y/N?   ").lower()

        if play_again == "y":
            win_count += 1
            best_score = guess_count
            return start_game(win_count, best_score)
        elif play_again == "n":
            return print("Thank you for playing!")
    
start_game(win_count, best_score)


