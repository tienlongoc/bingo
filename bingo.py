#!/usr/bin/python3

import requests
import random
from time import sleep
import sys

def get_ascii_art(text: str) -> str:
    params = {'text': text}
    r = requests.get('https://artii.herokuapp.com/make', params=params)
    return r.text

def sprint(text: str):
    print(text)
    sleep(1)

def draw_next_ball(game_name: str):
    with open(game_name, 'r') as f:
        balls = f.read().rstrip('\n').split(' ')
    if not balls:
        return
    sprint('The remaining balls are:')
    sprint(' '.join(balls))
    sprint('Drawing next ball...')
    sprint('.')
    sprint('.')
    sprint('.')
    chosen_index = random.randrange(len(balls))
    sprint(get_ascii_art(balls[chosen_index]))
    sprint(f'The chosen ball is {balls[chosen_index]}!')
    del balls[chosen_index]
    sprint(f'There are {str(len(balls))} remaining balls:')
    sprint(' '.join(balls))
    with open(game_name, 'w') as f:
        f.write(' '.join(balls))

def make_new_game(game_name: str, number_of_balls: int = 40):
    sprint(f'Making a new game called {game_name} with {str(number_of_balls)} balls')
    balls_text = ' '.join([str(i) for i in range(1, number_of_balls + 1)])
    with open(game_name, 'w') as f:
        f.write(balls_text)
    sprint('Done!')
    sprint('The available balls are:')
    sprint(balls_text)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:')
        print('Initialise new game: bingo.py make_new_game {game name} {optional: number of balls to use}')
        print('Progress current game: bingo.py draw_next_ball {game name}')
        sys.exit()
    command = sys.argv[1]
    game_name = sys.argv[2]
    if command == 'make_new_game':
        number_of_balls = 40
        if len(sys.argv) > 3 and int(sys.argv[3]):
             number_of_balls = int(sys.argv[3])
        make_new_game(game_name, number_of_balls)
    elif command == 'draw_next_ball':
        draw_next_ball(game_name)

