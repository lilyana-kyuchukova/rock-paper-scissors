import random
import time
from termcolor import colored, cprint
import tkinter as tk


play = True
player_win_count = 0
computer_win_count = 0
draw_count = 0

print("Let's play Rock, Paper, Scissors!")

time.sleep(0.5)
print()
print("Ready...")
time.sleep(0.7)
print()
print("Steady....")
time.sleep(0.9)
print()
print("Gooooo!")
print()

while play:

    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Please enter [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        # raise SystemExit("Invalid Input. Try again..")
        print("Oops, something went wrong! You can only enter R, P or S. Try again..")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = scissors
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = rock

    print(f"The computer chose {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_win_count += 1
        win = "🥳"
        print(colored(f"{player_move} beats {computer_move}\nYou win!", "green") + win)
    elif player_move == computer_move:
        draw_count += 1
        print(colored("Draw!", "yellow"))
    else:
        computer_win_count += 1
        lose = "🤬"
        print(colored(f"{computer_move} beats {player_move}\nYou lose!", "red") + lose)

    time.sleep(0.8)

    carry_on_playing = input("Play Again: [y]es / [n]o: ")

    if carry_on_playing == "n":
        play = False

print()
header = f"You nailed it {player_win_count} times!"\
         f" You lost - {computer_win_count} times"\
         f" Draws - {draw_count}"

time.sleep(0.7)
print(f"Thanks for playing !\n\nYour stats\n{header}")
