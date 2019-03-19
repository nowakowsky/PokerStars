
#i think it's not being used atm

from config import opponent_moves
from config import displays
from screenshot import screenshot
import numpy as np
import time

# all moves = [102, 204,255]
# fold = [67,119,151]

moves = [55969, 66115, 64848, 57953, 75972, 82714, 69526, 65456, 94234, 75228, 72190, 98839, 78767, 76302, 85492, 101721, 74192, 73316, 71574, 64967, 64302, 63148, 63045, 62363, 58978, 57297, 56148, 62481, 63112, 64789, 68419, 69817, 75958, 79106]


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
    print (_)