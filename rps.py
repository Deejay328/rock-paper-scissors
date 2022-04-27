"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time
import sys
moves = ['rock', 'paper', 'scissors']


def print_pause(message):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.05)


def play_again():
    while True:
        response = input('Would you like to play again?').lower()
        if response == 'yes':
            game.play_game()
        elif response == 'no':
            print_pause('Okay! Thanks for playing')
            break
        else:
            print_pause('invalid response')


class Player:

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):

    def move(self):
        return "rock"


class RandomPlayer(Player):

    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):

    def move(self):
        while True:
            print_pause("Your turn! Enter \'rock\',"
                        " \'paper\', or \'scissors\'. \n")
            choice = input().lower()
            if choice in moves:
                break
            else:
                print_pause("Please enter valid response\n")
        return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.round = 1

    def move(self):
        if self.round > 1:
            return self.their_move
        else:
            self.round += 1
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.moveNum = 3

    def move(self):
        if self.moveNum % 3 == 0:
            self.moveNum += 1
            return "rock"
        elif self.moveNum % 3 == 1:
            self.moveNum += 1
            return "paper"
        elif self.moveNum % 3 == 2:
            self.moveNum += 1
            return "scissors"

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"You played: {move1}  Computer plays: {move2}\n")
        time.sleep(1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print_pause('You win this round\n')
            self.p1.score += 1
            if self.p1.score == 3:
                print_pause("Final score: " + str(self.p1.score) + " - "
                            + str(self.p2.score) + " You win!\n")
                play_again()
            else:
                print_pause("Score: " + str(self.p1.score) + " - "
                            + str(self.p2.score) + "\n")
                time.sleep(1)
        elif beats(move2, move1):
            print_pause('You lose this round.\n')
            self.p2.score += 1
            if self.p2.score == 3:
                print_pause("Final score: " + str(self.p1.score) + " - "
                            + str(self.p2.score) + " You lose!\n")
                play_again()
            else:
                print_pause("Score: You-" + str(self.p1.score) + " computer"
                            "-" + str(self.p2.score) + "\n")
                time.sleep(1)
        else:
            print_pause("This round is a tie\n")

    def play_game(self):
        print_pause("Game start!\n")
        round = 1
        self.p1.score = 0
        self.p2.score = 0
        while self.p1.score < 3 and self.p2.score < 3:
            print_pause(f"Round {round}:\n")
            self.play_round()
            round += 1


if __name__ == '__main__':
    """create a game object with P1 as HumanPlayer and
    P2 as either RandomPlayer, ReflectPlayer, RockPlayer, or CyclePlayer"""
game = Game(HumanPlayer(), CyclePlayer())
game.play_game()
