import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

word = random.choice(word_list)

l = 6
end_game = False
print(logo)

gw = []
for _ in range(len(word)):
    gw += ["_"]

while not end_game:
    char = input("Guess a letter: ").lower()
    if char in gw:
        print("you guessed this letter already")
    for x in range(len(word)):
        letter = word[x]
        if letter == char:
            gw[x] = letter

    if char not in word:
        print(f"You guessed {char}, that's not in the word. You lose a life.")
        l -= 1
        if l == 0:
            end_game = True
            print(word)
            print("You Lose")
    print(f"{' '.join(gw)}")
    if "_" not in gw:
        end_game = True
        print(word)
        print("You Win")

    print(stages[l])
