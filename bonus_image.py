import os
import re
import pyautogui
import time
from pynput.keyboard import Controller, Key
from PIL import Image
import PIL.Image


dd=(360, 130, 420, 300)
san=(790, 130, 420, 300)
rav=(1220, 130, 420, 300)
flo=(360, 450, 420, 300)
inf=(790, 450, 420, 300)
blo=(1220, 450, 420, 300)
#page two
wor=(360, 130, 420, 300)
qua=(790, 130, 420, 300)
dc=(1220, 130, 420, 300)
mud=(360, 450, 420, 300)
ouc=(790, 450, 420, 300)


    
#xddd= pyautogui.screenshot(region=ouc)
#xddd.show()
def reward():
    if pyautogui.locate('reward.png', region=(), confidence=0.8) != None:
        print("BONUS-REWARD")
        time.sleep(1)
    else:
        print("NO")
        time.sleep(1)
def go(): 
    time.sleep(2)
    if pyautogui.locateOnScreen('bonus.png', region=dd, confidence=0.8) != None:
        return 1
    else:
        time.sleep(1)
        if pyautogui.locateOnScreen('bonus.png', region=san, confidence=0.8) != None:
            return 2
        else:
            time.sleep(1)
            if pyautogui.locateOnScreen('bonus.png', region=rav, confidence=0.8) != None:
                return 3
            else:
                time.sleep(1)
                if pyautogui.locateOnScreen('bonus.png', region=flo, confidence=0.8) != None:
                    return 4
                else:
                    time.sleep(1)
                    if pyautogui.locateOnScreen('bonus.png', region=inf, confidence=0.8) != None:
                        return 5
                    else:
                        time.sleep(1)
                        if pyautogui.locateOnScreen('bonus.png', region=blo, confidence=0.8) != None:
                            return 6
    time.sleep(1)
    pyautogui.moveTo(1300, 1000)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(1)
    if pyautogui.locateOnScreen('bonus.png', region=wor, confidence=0.8) != None:
        return 7
    else:
        time.sleep(1)
        if pyautogui.locateOnScreen('bonus.png', region=qua, confidence=0.8) != None:
            return 8
        else:
            time.sleep(1)
            if pyautogui.locateOnScreen('bonus.png', region=dc, confidence=0.8) != None:
                return 9
            else:
                time.sleep(1)
                if pyautogui.locateOnScreen('bonus.png', region=mud, confidence=0.8) != None:
                    return 10
                else:
                    time.sleep(1)
                    if pyautogui.locateOnScreen('bonus.png', region=ouc, confidence=0.8) != None:
                        return 11
                    else:
                        print("NO")

def get_reward():
    if pyautogui.locateOnScreen('reward.png', confidence=0.8) != None:
        return True
    
def get_victory():
    if pyautogui.locateOnScreen('victory.png', confidence=0.8) != None:
        return True