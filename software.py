import win32gui #used in prepare_screen.py / move_and_resize.py
from PIL import ImageGrab #Used to screenshots.py / board_cards.py
import cv2 #used by card_info.py
import numpy as np #used by card_info.py

from prepare_screen import move_and_resize_windows #move and resize 6 windows to fit fullHD
from board_cards import cards_on_board #takes a board number, grabs all cards from this board, returns list of cards (screenshots!)
from card_info import grab_card_info #takes [6x5 list] containing screenshots of all cards, returns same list of info
from card_info import card_info #takes a single card, return single info
from player_turn import player_turn_check, available_moves_check
from screenshot import screenshot
from ingame import who_is_who

#CONFIG FILES
from config import cards 
from config import not_a_card #used to filter trashes when detecting card values
from config import my_card_1, my_card_2 #hand

#Settings
window_name = "Limit" #This is partial name of game window process

def game_stage(last_checked_cards,stage,table): #returns game stage (new game, pre-floop, floop, river, turn)
    current_cards = cards_on_board(table)
    if stage == "New game!":
        if current_cards == "":
            return "Pre-floop", current_cards
        elif current_cards[4] != "":
            return "River", current_cards
        elif current_cards[3] != "":
            return "Turn", current_cards
        elif current_cards[2] != "":
            return "Floop", current_cards
        else:
            return "Prefloop", current_cards
    else:
        if last_checked_cards[0] != "" and current_cards[0] == "":
            return "New game!", last_checked_cards
        elif last_checked_cards[0] != "" and current_cards == "":
            return "Pre-floop", current_cards
        elif last_checked_cards[0] == "" and current_cards[0] != "":
            return "Floop", current_cards
        elif last_checked_cards[3] == "" and current_cards[3] != "":
            return "Turn", current_cards
        elif last_checked_cards[4] == "" and current_cards[4] != "":
            return "River", current_cards
        else:
            return stage, current_cards
            #this happens when checking state is the same???
            #print ("F up when checking cards. Last checked card 0: {} Current card 0: {}.".format(last_checked_cards[0], current_cards[0]))

from tight_agressive import card_power #check hand power
import time, os
#from opponent_movement import moves_on_board

playing = 0 #playing on board 0
move_and_resize_windows(window_name)
cards = cards_on_board(playing)
stage = "New game!"
print ("---")

lastOutput = "" #store last output
while True:
    output = "" #store output string there
    stage, cards = game_stage(cards,stage,playing)
    if len(cards) == 0:
        output += "No cards on table."
    else:
        output += "Cards on table: "
    for card in cards:
        output += card
        output += " "
    output += "\n"

    output += "Game stage: "
    output += stage
    if output != lastOutput:
        os.system('cls')
        print (output)
    lastOutput = output

    while player_turn_check():
        os.system('cls')
        print (output)
        hand_one = card_info(screenshot(my_card_1))
        #hand_two is checked later to safe some resources
        if hand_one == "00":
            print ("Not in game.")
        else:
            hand_two = card_info(screenshot(my_card_2))
            print ("Player cards: %s %s " % (hand_one, hand_two))
            print ("Tight-agressive rating:", card_power(hand_one, hand_two))
            if player_turn_check():
                print ("Possible moves:", *available_moves_check())
        break
    
    time.sleep(3)

#Player position is always 0! Other players are 1-5 on left    