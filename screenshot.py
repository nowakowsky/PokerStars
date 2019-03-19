from PIL import ImageGrab #Used to screenshots

def screen_board(board_no):
        #it takes board number 1-6!!
        #counting from left to right
        #from up to down

        #Central display management TBI
        grab_displays = ((10,50,630,380),
        (650,50,1270,380),
        (1290,50,1910,380),
        (10,590,630,920),
        (650,590,1270,920),
        (1290,590,1910,920))

        #Screenshot of whole window number board-1
        screen = ImageGrab.grab(bbox=(grab_displays[board_no-1]))
        return screen

#takes and returns a screenshot of given coords x1 y1 to x2 y2
def screenshot(xyxy):
        image = ImageGrab.grab(bbox=(xyxy)) 
        return image

#that was used just for dev, can be removed
import random
def screen_all_and_save():
        grab_displays = ((0,0,640,540), #(10,50,630,380)
        (650,50,1270,380),
        (1290,50,1910,380),
        (10,590,630,920),
        (650,590,1270,920),
        (1290,590,1910,920))
        for i in grab_displays:
                screen = ImageGrab.grab(bbox=(i))
                screen.save('screenshots\\%i.png' % random.randint(0,123123))

