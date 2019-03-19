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
    # cv2.imwrite('check %i.png' %check_button_gray.sum(), check_button_gray)
    if check_button_gray.sum() == check_button_sum:
        moves.append("check")
    
    raise_button_np = np.array(screenshot(raise_button))
    raise_button_gray = cv2.cvtColor(raise_button_np, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('raise %i.png' %raise_button_gray.sum(), raise_button_gray)
    if raise_button_gray.sum() == raise_button_sum:
        moves.append("raise")

    fold_button_np = np.array(screenshot(fold_button))
    fold_button_gray = cv2.cvtColor(fold_button_np, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('fold %i.png' %fold_button_gray.sum(), fold_button_gray)
    if fold_button_gray.sum() == fold_button_sum:
        moves.append("fold")

    call_button_np = np.array(screenshot(call_button))
    call_button_gray = cv2.cvtColor(call_button_np, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('call %i.png' %call_button_gray.sum(), call_button_gray)
    if call_button_gray.sum() == call_button_sum:
        moves.append("call")

    bet_button_np = np.array(screenshot(bet_button))
    bet_button_gray = cv2.cvtColor(bet_button_np, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('bet %i.png' %bet_button_gray.sum(), bet_button_gray)
    if bet_button_gray.sum() == bet_button_sum:
        moves.append("bet")

    all_in_button_np = np.array(screenshot(all_in_button))
    all_in_button_gray = cv2.cvtColor(all_in_button_np, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('all_in %i.png' %all_in_button_gray.sum(), all_in_button_gray)
    if all_in_button_gray.sum() == all_in_button_sum:
        moves.append("all_in")
        
    return moves