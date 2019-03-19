from screenshot import screenshot
from config import green_bar, green, check_button, raise_button, bet_button, call_button, fold_button, all_in_button
from config import raise_button_sum, fold_button_sum, check_button_sum, call_button_sum, bet_button_sum, all_in_button_sum
import cv2
import numpy as np

def player_turn_check():
    
    green_bar_np = np.array(screenshot(green_bar))
    green_bar_gray = cv2.cvtColor(green_bar_np, cv2.COLOR_RGB2BGR)
    if green in green_bar_gray:
        return True
    else:
        return False

def available_moves_check():
    moves = []
    check_button_np = np.array(screenshot(check_button))
    check_button_gray = cv2.cvtColor(check_button_np, cv2.COLOR_RGB2GRAY)
    # print (check_button_gray.sum())
    # print (check_button_sum)
    # cv2.imwrite('check %i.png' %check_button_gray.sum(), check_button_gray)
    if check_button_gray.sum() == check_button_sum:
        moves.append("check")
    
    raise_button_np = np.array(screenshot(raise_button))
    raise_button_gray = cv2.cvtColor(raise_button_np, cv2.COLOR_RGB2GRAY)
    # print (raise_button_gray.sum())
    # print (raise_button_sum)
    # cv2.imwrite('raise %i.png' %raise_button_gray.sum(), raise_button_gray)
    if raise_button_gray.sum() == raise_button_sum:
        moves.append("raise")

    fold_button_np = np.array(screenshot(fold_button))
    fold_button_gray = cv2.cvtColor(fold_button_np, cv2.COLOR_RGB2GRAY)
    # print (fold_button_gray.sum())
    # print (fold_button_sum)
    # cv2.imwrite('fold %i.png' %fold_button_gray.sum(), fold_button_gray)
    if fold_button_gray.sum() == fold_button_sum:
        moves.append("fold")

    call_button_np = np.array(screenshot(call_button))
    call_button_gray = cv2.cvtColor(call_button_np, cv2.COLOR_RGB2GRAY)
    # print (call_button_gray.sum())
    # print (call_button_sum)
    # cv2.imwrite('call %i.png' %call_button_gray.sum(), call_button_gray)
    if call_button_gray.sum() == call_button_sum:
        moves.append("call")

    bet_button_np = np.array(screenshot(bet_button))
    bet_button_gray = cv2.cvtColor(bet_button_np, cv2.COLOR_RGB2GRAY)
    # print (bet_button_gray.sum())
    # print (bet_button_sum)
    # cv2.imwrite('bet %i.png' %bet_button_gray.sum(), bet_button_gray)
    if bet_button_gray.sum() == bet_button_sum:
        moves.append("bet")

    all_in_button_np = np.array(screenshot(all_in_button))
    all_in_button_gray = cv2.cvtColor(all_in_button_np, cv2.COLOR_RGB2GRAY)
    # print (all_in_button_gray.sum())
    # print (all_in_button_sum)
    # cv2.imwrite('all_in %i.png' %all_in_button_gray.sum(), all_in_button_gray)
    if all_in_button_gray.sum() == all_in_button_sum:
        moves.append("all_in")


    return moves
    # bet_button_np = np.array(screenshot(bet_button))
    # bet_button_gray = cv2.cvtColor(bet_button_np, cv2.COLOR_RGB2GRAY)
    # if bet_button_gray.sum() == bet_button_sum:
    #     moves.append("bet")

    # all_in_button_np = np.array(screenshot(all_in_button))
    # all_in_button_gray = cv2.cvtColor(all_in_button_np, cv2.COLOR_RGB2GRAY)
    # if all_in_button_gray.sum() == all_in_button_sum:
    #     moves.append("all_in")

    # screenshot(bet_button)
    # raise0 = cv2.imread('raise.png',0)
    # raise1 = cv2.imread('raise1.png',0)
    # check = cv2.imread('check1.png',0)
    # fold = cv2.imread('fold.png',0)
    # bet = cv2.imread('bet.png',0)

    # # cv2.imwrite("raise0 %i.png" % raise0.sum(), raise0)
    # # cv2.imwrite('check %i.png' %check.sum(), check)
    # cv2.imwrite('bet %i.png' %bet.sum(), bet)
    # cv2.imwrite('call %i.png' %call.sum(), call)
    # cv2.imwrite('raise1 %i.png' %raise1.sum(), raise1)


# raise_button_sum = 68249
# fold_button_sum = 56251
# check_button_sum = 53827
# call_button_sum = 40056
# print (player_turn_check())
# # available_moves_check()
# print (available_moves_check())
#print (player_turn_check())
# import time
# for i in range(30):
#     if player_turn_check():
#         print (available_moves_check())
#     time.sleep(5)