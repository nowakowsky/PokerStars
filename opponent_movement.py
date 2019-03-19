
#this was made to grab values of moves (it's not used by software)


from config import opponents_positions #positions of the opponents on screen
from config import displays
from config import moves


from screenshot import screenshot
import numpy as np
import time

#takes a board number and returns (STRING)MOVE and (INT)No of opponent
def moves_on_board(board):
    read_moves = ""
    whole_screen = screenshot(displays[board])
    for opponent, number in zip(opponents_positions[board], range(0,5)):
        # print (opponent)
        img = whole_screen.crop(opponent)
        #num = np.array(img)
        sum = np.array(img).sum()
        if str(sum) in moves:
            read_moves = str(number+1) + moves[str(sum)]
            return read_moves
        return "nomove"
    



def moves_on_all_boards():
    whole_screen = screenshot([0,0,1920,1080])
    
if __name__ == "__main__":
    moves_on_board(0)
'''
            for _ in range(0,1000):
                whole_screen = screenshot([0,0,640,540])
                for i in opponent_moves:

                    pic = whole_screen.crop(i)
                    # pic = screenshot(i)
                    num = np.array(pic)
                    suma = num.sum()
                    if suma not in moves:
                        if [67,119,151] in num or [102, 204,255] in num:
                            pic.save('%i.png' % suma)
                print (_)'''