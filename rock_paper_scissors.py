print("Welcom to Rock Paper and Scissors game")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
num = int(input())
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = [rock, paper, scissors]
import random

computer = random.randint(0, 3)
map = [num, computer]
if map == [0, 2] or map == [2, 1] or map == [1, 0]:
    print("user = " + user[num])
    print("computer = \n" + user[computer])
    print("You Win")
elif map == [2, 0] or map == [1, 2] or map == [0, 1]:
    print("user = " + user[num])
    print("computer = " + user[computer])
    print("You Lose")
else:
    print("user = " + user[num])
    print("computer = " + user[computer])
    print("It's a draw")
