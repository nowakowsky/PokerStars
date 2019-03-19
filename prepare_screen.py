#This function moves and resizes processes with "name" in process name to fit 6 on FullHD Screen

import win32gui #Used to read process info

def move_and_resize_windows(name): #name const part of process name
        displays = [[0,0,640,540], #x1,y1,x2,y2 (X2 = X1 + width!!!! (WEIRD FACT - counts from X1, NOT from 0!!!)
        [640,0,640,540],
        [1280,0,640,540],
        [0,540,640,540],
        [640,540,640,540],
        [1280,540,640,540]] #these are the x1,y1,x2,y2 to corner all 4 videos on fullHD (1920x1080)


        global window_number
        window_number = 0
        def enumHandler(hwnd, lParam):
                if win32gui.IsWindowVisible(hwnd): #hwnd is next process
                        global window_number
                        if name in win32gui.GetWindowText(hwnd): #it checks if the process I'm looking for is running    
                                tab = displays[window_number]
                                win32gui.MoveWindow(hwnd,tab[0],tab[1],tab[2],tab[3],True) #resizes and moves the process
                                window_number += 1
        win32gui.EnumWindows(enumHandler, None) #start run enumHandler

#This is part of process name - showed on Window Bar
# window_name = "Limit"
# move_and_resize_windows(window_name)