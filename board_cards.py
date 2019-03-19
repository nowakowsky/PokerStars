import random
from PIL import Image
#screenshot(card) takes screenshot of specific card, screen_board(board)[counting from 0 to 5] takes  screenshot of whole board
from screenshot import screenshot, screen_board
from card_info import grab_card_info
from config import displays, card_on_first_display

#This should be easy to fix, atm works only for the first table
def cards_on_board(table):
        cards = []
        cards_on_each_board = card_on_first_display

        #This loop changes a board
        for card in range(len(cards_on_each_board)): #cards 0-4
                for each in range(2):
                        cards_on_each_board[card][each] += displays[table][each]
                cards_on_each_board[card][2] = cards_on_each_board[card][0] + 10
                cards_on_each_board[card][3] = cards_on_each_board[card][1] + 14

        for each_card in cards_on_each_board:
                image = screenshot(each_card)
                cards.append(image)
                
        return grab_card_info(cards)
