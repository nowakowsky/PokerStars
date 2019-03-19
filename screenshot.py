from PIL import ImageGrab #Used to screenshots

#it takes board number 1-6!! 
def screen_board(board_no):
        grab_displays = ((10,50,630,380),
        (650,50,1270,380),
        (1290,50,1910,380),
        (10,590,630,920),
        (650,590,1270,920),
        (1290,590,1910,920))
        #Screenshot of whole window number board-1
        return ImageGrab.grab(bbox=(grab_displays[board_no-1]))

#takes and returns a screenshot of given coords x1 y1 to x2 y2
def screenshot(xyxy): 
        return ImageGrab.grab(bbox=(xyxy))