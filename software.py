from prepare_screen import move_and_resize_windows
from board_cards import cards_on_board #returns list of cards (screenshots!)
from card_info import grab_card_info #takes list of screenshots, returns list of info
from card_info import card_info #takes a single card, return single info
from player_turn import player_turn_check, available_moves_check
from screenshot import screenshot
from tight_agressive import card_power #check hand power
import time, os
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