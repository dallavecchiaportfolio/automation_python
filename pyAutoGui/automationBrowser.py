import pyautogui
import sys
import time


def operaBrowser():
    # ********************************
    #
    #        OPERA WEB BROWSER
    # Address Bar position x=222 y=80
    #
    # ********************************
    pyautogui.write("opera")
    time.sleep(2) 
    pyautogui.keyDown("enter")
    pyautogui.position(222,80) # Address bar
    time.sleep(3)
    pyautogui.write("https://google.com/calendar")
    pyautogui.press("enter")
    pyautogui.position(561,448)
    time.sleep(3)
    pyautogui.write("dallavecchiacareer")


def safariBrowser():
    # ********************************
    #
    #       SAFARI WEB BROWSER
    # Address Bar position x=405 y=54
    #
    # ********************************
    pyautogui.write("safari")
    time.sleep(2)
    pyautogui.keyDown("enter")
    pyautogui.position(405,54) # Address bar
    time.sleep(3)
    pyautogui.write("https://google.com/calendar")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.position(561,448)
    pyautogui.write("dallavecchiacareer")


def openBrowser(browserName):
    
    if browserName == "opera":
        operaBrowser()
    elif browserName == "safari":
        safariBrowser()
    else:
        print("Browser does not exist!")
        exit()


if len(sys.argv) == 2:

    pyautogui.write("Processing starting...")
    pyautogui.hotkey("command","space") # Open Spotlight on macOS'
    time.sleep(2)
    openBrowser(sys.argv[1])

else:
    
    print("Missing second argument.")
    exit()