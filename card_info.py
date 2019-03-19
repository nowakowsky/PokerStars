import os, os.path
import cv2
import numpy as np
from config import cards, colors #card list, color names
#from config import not_a_card

#returns color -> green/red/black/blue
#checks color settings in config.py/colors{}
def color(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #change bgr image to rgb

    red = np.array([202,16,16])
    green = np.array([39,132,8])
    black = np.array([0,0,0])
    blue = np.array([8,8,238])

    color = ""
    for i in rgb:
        for j in i:    
            if (j == green).all():
                color = "Green"
                return colors[color]
            if (j == red).all():
                color = "Red"
                return colors[color]
            if (j == black ).all():
                color = "Black"
                return colors[color]
            if (j == blue).all():
                color = "Blue"
                return colors[color]
    return "0"

#takes grayscale image and returns it black and white [(0,0,0) or (255,255,255)] pixels only
#this is very important to makes sure that close images have equal sums and let recude card list
#so it reduces numbers of operations 
def black_white(pic):
        for row in range(len(pic)):
            for pixel in range(len(pic[row])):
                if pic[row,pixel] != 0:
                    pic[row,pixel] = 255
        return pic

#When you take a card, you need to convert it to GtayScale
#Then you need to reverse GrayScale (to make sum lower much)
#Then you change it to black and white (all non 0 pixels set to 255) and count sum
#Then you feed this function with sum_blackwhite (int) and blackwhite(cv2 numpy array - picture)
#Finally it returns value of card (defined in config.py)
def card_value(sum_blackwhite, blackwhite):
    card_checked = "0"
    if str(sum_blackwhite) in cards:
        card_checked = cards[str(sum_blackwhite)]
        #sums 6 and 9 are equal so they have the same sum. If pixel [row4:col4] is black it's a nine! 
        if cards[str(sum_blackwhite)] == "6":
            if (blackwhite[4,4] == [0,0,0]).all():
                card_checked = "9"
        #same problem with ace and 3 (seems to only happen in hand)
        if cards[str(sum_blackwhite)] == "3":
            if (blackwhite[13,4] == [0,0,0]).all():
                card_checked = "A"      
        return card_checked
    else:
        #This one can be useful
        #cv2.imwrite("cards_to_add\\%i.png" % sum_blackwhite, blackwhite)
        return "0"
            
def card_info(card):
    #convert card to numpy array
    card_np = np.array(card)
    #cv2 works on BGR, not RGB
    img_color = cv2.cvtColor(card_np, cv2.COLOR_RGB2BGR)
    #GRAYSCALE for checking card value
    img_gray = cv2.cvtColor(card_np, cv2.COLOR_BGR2GRAY)
    #reverse grayscale for smaller sum of pixels 
    img_gray_reversed = cv2.bitwise_not(img_gray)

    #change reversed grayscale image to black and white
    #reversed to make sum smaller (0,0,0) < (255,255,255)
    blackwhite = black_white(img_gray_reversed)

    #sum of black white image, this is used to check value of card
    sum_blackwhite = blackwhite.sum()
    
    #Check value
    value = card_value(sum_blackwhite, blackwhite)

    #Check color
    info = color(img_color) + value

    #return color+value
    return info

from screenshot import screenshot
from config import not_a_card

def grab_card_info(card_screenshots, skip=not_a_card):
    cards_boards_all = ["", "", "", "", ""]
    for each_card,i in zip(card_screenshots, range(5)):
        current_card = card_info(each_card)
        if current_card not in skip:
            cards_boards_all[i] =  current_card
    return cards_boards_all
