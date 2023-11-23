import random
from guess_num_art import logo


def difficulty_level(level):
    if level == 'easy':
        return 10
    elif level == 'hard':
        return 5
    else:
        print("Choose a correct difficulty level.")


random_num = random.randint(1,100)


def check_answer(guess, attempts, answer):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' and 'hard': ").lower()
    attempts = difficulty_level(difficulty)
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, attempts, answer)
        if attempts == 0:
            print("You've run out of guesses, You lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()


