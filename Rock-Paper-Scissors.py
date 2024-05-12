# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:58:34 2024

@author: Zia
"""
import random

# rock/paper/scissors

ROCK = 3
PAPER = 1
SCISSORS = 2

def computersChoice():
    number = random.randint(1,3)
    if number == ROCK:
        hand = 'rock'
    elif number == SCISSORS:
        hand = 'scissors'
    elif number == PAPER:
        hand = 'paper'
    return hand

def values(response):
    if response == 'rock' or response == 'Rock':
        return ROCK
    elif response == 'paper' or response == 'Paper':
        return PAPER
    elif response == 'scissors' or response == 'Scissors':
        return SCISSORS
    
def winner(userValue, computerValue):
    if userValue == ROCK and computerValue == PAPER:
        print('Game Over: you lose')
    elif computerValue == ROCK and userValue == PAPER:
        print('Game Over: you win!')
    else:
        if userValue > computerValue:
            print('Game Over: you win :)')
        elif computerValue > userValue:
            print('Game Over: you lose :(')
        elif userValue == computerValue:
            print('Game Over: you tied')
        
def main():
    user = str(input('user one: rock, paper, or scissors\n'))
    userValue = values(user)

    computer = computersChoice()
    computerValue = values(computer)
    print(f'computer: {computer}')
    
    winner(userValue, computerValue)

main()
print()
playAgain = str(input('do you want to play again?\n'))

while playAgain == 'yes': 
    main()
    print()
    playAgain = str(input('do you want to play again?\n'))
print('Good bye\nThank you for playing!')