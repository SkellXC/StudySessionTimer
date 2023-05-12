import time
import pyautogui
import os

timeOff = 0
timeOn = 0

def movementCheck():
    global timeOff
    global timeOn
    initialPos = pyautogui.position()  # Gets mouse position
    
    time.sleep(0.95)
    secPos = pyautogui.position()  # Gets second position to compare to the first
    diffX = initialPos[0] - secPos[0]
    diffY = initialPos[1] - secPos[1]  # Difference between x coords and y coords
    #if -25 < diffX < 25 or 25 < diffY < 25:  # Movements under 25 pixels do not count
    while -25 < diffX < 25 or 25 < diffY < 25 and pyautogui.keyboard.is_pressed() is False:  # Begins counting
        diffX = initialPos[0] - secPos[0]
        diffY = initialPos[1] - secPos[1]
        timeOff += 1
        time.sleep(0.95)
        os.system('cls') # Clears the console before updating the display
        print(f"Inactive: {timeOff}s\nActive: {timeOn}s")
        secPos = pyautogui.position()  # Checks new position of the mouse to compare to original
        
    else:
        timeOn += 1
        os.system('cls') # Clears the console before updating the display
        print(f"Inactive: {timeOff}s\nActive: {timeOn}s")
        

while True:
    movementCheck()
