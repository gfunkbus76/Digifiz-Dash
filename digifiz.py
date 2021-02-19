"""
    Attempting to code the Digifiz dash project cleaner
    Written by Gavin Norquay in 2021

    Opensource and designed from many online projects...
    Copy, paste, run, debug... repeat lol.

"""
from game import Game

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()