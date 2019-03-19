### that was reading token position and returning player's position (big blind, late, etc)
### this is pretty important if we want software to stop being useless

from config import in_game, in_game_rgb, token_pos
from screenshot import screenshot
import numpy as np

def players_check():
    #store online players !!! 0 = PLAYER, 1LEFT FROM PLAYER, 2LEFT, 3 LEFT ETC
    #THAT'S WHY GOING FROM 1
    online_players = []
    for i in range(1, len(in_game)):
        in_game_np = np.array(screenshot(in_game[i]))
        for row in in_game_np:
            for pixel in row:
                #if this color is in any pixel of in_game_np picture he is playing
                if (pixel == in_game_rgb).all():
                    online_players.append(i)
                    break
            if i in online_players:
                break
    return online_players

def token_check():
    for i in token_pos:
        token_np = np.array(screenshot(token_pos[i]))
        if token_np.sum() > 40000:
            return i

def who_is_who():
    token = int(token_check())
    players = players_check()
    if token == 0 and len(players) > 1:
        return 'Late'
    elif len(players) == 1:
        if token == 0:
            return 'Small Blind'
        else:
            return 'Big Blind'
    elif len(players) == 2:
        # if token == 0: 
        #     return 'Late'
        if token == players[0]:
            return 'Big Blind'
        elif token == players[1]:
            return 'Small Blind'
    elif len(players) == 3:
        # if token == 0:
        #     return 'Late'
        if token == players[0]:
            return 'Early'
        elif token == players[1]:
            return 'Big Blind'
        elif token == players[2]:
            return 'sb3'
    elif len(players) == 4:
        # if token == 0:
        #     return 'Late'
        if token == players[0]:
            return 'Mid'
        elif token == players[1]:
            return 'Early'
        elif token == players[2]:
            return 'Big Blind'
        elif token == players[3]:
            return 'Small Blind'
    else:
        if token == players[0]:
            return 'Mid'
        elif token == players[1]:
            return 'Early'
        elif token == players[2]:
            return 'Early'
        elif token == players[3]:
            return 'Big Blind'
        elif token == players[4]:
            return 'Small Blind'

        