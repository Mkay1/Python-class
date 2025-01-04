import sys
import pygame
import random


from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')


while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    pchoice = input("Enter your choice (rock/paper/scissors): ")
    while pchoice not in ['rock', 'paper', 'scissors']:
        pchoice = input("Invalid choice. Enter your choice (rock/paper/scissors): ")
    return pchoice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print("Player chose " + player_choice)
    print("Computer chose " + computer_choice)
    print(determine_winner(player_choice, computer_choice))

play_game()
  