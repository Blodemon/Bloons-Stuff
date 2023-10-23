import os
import re
import pyautogui
import time
from pynput.keyboard import Controller, Key
import pytesseract
from PIL import Image
import PIL.Image
import cv2


#Image reader
myconfig =r"--psm 10 --oem 3 "

#myscreen.show()
#Money reader
def get_money():
    try:
        if selectedlr()==1:
            screenshot = pyautogui.screenshot(region=(350, 15, 220, 55))
            screenshot.save('screens.png')
        else:
            if selectedlr()==0:
                screenshot = pyautogui.screenshot(region=(735, 15, 220, 55))
                screenshot.save('screens.png')
            else:
                return
        myscreen = Image.open('screens.png')
        money=pytesseract.image_to_string(myscreen, config=myconfig)
        print(re.sub('[^\d+]+',"", money))
        print(int(re.sub('[^\d+]+',"", money)))
        return int(re.sub('[^\d+]+',"", money))
    except:
        return 0

#Round reader



keyboard = Controller()
placed = []
costs = [215, 300, 565, 300, 540, 245, 360, 335, 515, 820, 1640, 770, 820, 405, 2700, 540, 595, 430, 1325, 1080, 1270, 430, 270]

m_to_c = ['q', 'w', 'e', 'r', 't', 'z', 'y', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'i']

def print_mouse_position():
    for _ in range(10):
        wait(5)
        # Get the current mouse position
        mouse_x, mouse_y = pyautogui.position()
        
        # Print the mouse position
        print(f"Mouse Position: X={mouse_x}, Y={mouse_y}")

def place(x, y, Monkey):
    pyautogui.moveTo(x, y)
    keyboard.press(Monkey)
    wait(0.1)
    keyboard.release(Monkey)
    time.sleep(0.2)
    pyautogui.click()
    wait(0.5)
    pyautogui.click(x, y)
    wait(0.2)
    placed.append([x, y])
    print(f"Placed {Monkey} as Nr.: {len(placed)}")

def check_cost(test):
    i=0
    affordable=0
    why=0
    
    while i<20:
        wait(0.1)
        why=test
        if get_money()>= costs[m_to_c.index(why)]:
            affordable+=1
        i+=1
    if affordable>=10:
        return bool(True)

def place_cost(x, y, Monkey):
    while True:
        wait(0.1)
        if check_cost(Monkey):
                pyautogui.moveTo(x, y)
                keyboard.press(Monkey)
                wait(0.1)
                keyboard.release(Monkey)
                time.sleep(0.2)
                pyautogui.click()
                wait(0.5)
                pyautogui.click(x, y)
                wait(0.2)
                placed.append([x, y])
                print(f"Placed {Monkey} as Nr.: {len(placed)}")
                return 
        wait(1)


def select_monkey(index):
    wait(0.2)
    pyautogui.moveTo(placed[index])
    pyautogui.click()
    print(f"Selected Monkey Nr.:{index + 1}")


def upgrade_select(x, y, index):
    time.sleep(0.1)
    print(f"Upgrade {x},{y} Path {index + 1}.")
    upgradepath = [Key.f1, Key.f2, Key.f3]
    keyboard.press(upgradepath[index])
    keyboard.release(upgradepath[index])


def upgrade_time(index, numOfUpgrades):
    nou = 0
    while (1 == 1):
        time.sleep(0.3)
        if pixelcheck(index):
            upgradepath = [Key.f1, Key.f2, Key.f3]
            keyboard.press(upgradepath[index])
            keyboard.release(upgradepath[index])
            nou = nou + 1
        if selected(0) == bool(False) and selected(1) == bool(False):
            print("Error: No Monkey selected!")
            return
        if numOfUpgrades == nou:
            print(f"Upgraded Path:{index + 1} x{nou}.")
            return


def replace_trap(x, y):
    # links: 380, 300
    # rechts:1600, 300
    wait(0.1)
    if selectedlr() == 0:
        pyautogui.moveTo(380, 300)
        pyautogui.click()
    else:
        if selectedlr() == 1:
            pyautogui.moveTo(1600, 300)
            pyautogui.click()
    wait(0.5)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def pymoveclick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
def sell_truck():
    wait(0.1)
    pymoveclick(900,700)
    pymoveclick(1010, 760)
    pymoveclick(891, 691)
    pymoveclick(931, 619)
    
def darling_lock():
    pyautogui.moveTo(456, 546)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)


def upgrade(index):
    time.sleep(0.1)
    print(f"Upgrade Path {index + 1}.")
    upgradepath = [Key.f1, Key.f2, Key.f3]
    keyboard.press(upgradepath[index])
    keyboard.release(upgradepath[index])


def start():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(0.2)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("Start:")


def wait(sec):
    time.sleep(sec)


def heli_Sanctuary():
    place(1300, 500, 'b')
    pyautogui.moveTo(850, 400, duration=0.2)
    start()
    upgrade_time(0, 2)
    upgrade_time(1, 2)
    upgrade_time(0, 3)


def infernal():
    place(1580, 520, 'y')
    upgrade_time(1, 2) 
    upgrade_time(2, 1)
    start()
    upgrade_time(2, 3)
    place_cost(1580, 620, 'f')
    upgrade_time(0, 4)
    upgrade_time(2, 1)
    select_monkey(0)
    upgrade_time(2, 1)
    select_monkey(1)
    upgrade_time(0, 1)

def flooded_valleey():
    place(1182, 487, 'u')
    place(1049, 754, 'c')
    start()
    upgrade_time(2, 2)
    upgrade_time(1, 2)
    place_cost(1020, 170, 'c')
    upgrade_time(1, 2)
    upgrade_time(0,4)
    select_monkey(1)
    upgrade_time(1, 2)
    place_cost(916, 86, 'x')
    upgrade_time(0, 3)
    select_monkey(1)
    upgrade_time(1, 1)
    select_monkey(2)
    upgrade_time(0, 1)
    place_cost(1306, 500, 'x')
    upgrade_time(0, 2)
    upgrade_time(1, 5)

def quad():
    place(1260, 560, 'u')
    place(450, 560, 'l')
    upgrade_time(1, 1)
    start()
    upgrade_time(2, 4)
    replace_trap(210, 560)
    wait(10)
    place(1150, 560, 'l')
    upgrade_time(1, 1)
    upgrade_time(2, 4)
    replace_trap(1450, 560)
    wait(10)
    place(820, 460, 'c')
    upgrade_time(1, 2)
    upgrade_time(0, 4)
    wait(10)
    place(970, 380, 'k')
    upgrade_time(1, 2)
    upgrade_time(0, 2)
    select_monkey(3)
    upgrade_time(0, 1)
    wait(5)
    place(1048, 450, 'y')
    upgrade_time(1, 2)
    upgrade_time(2, 5)
    select_monkey(4)
    upgrade_time(1, 1)
    wait(5)
    place(890, 575, 'x')
    upgrade_time(0, 2)
    upgrade_time(1, 5)
    wait(5)
    place(1120, 250, 'j')
    upgrade_time(0, 2)
    upgrade_time(1, 5)

def muddy_puddles():
    place(760, 1040, 'y')
    upgrade_time(1, 2)
    upgrade_time(2, 1)
    start()
    upgrade_time(2, 3)
    wait(20)
    place(888, 1040, 'f')
    upgrade_time(0, 4)
    upgrade_time(2, 1)
    select_monkey(0)
    upgrade_time(2, 1)
    wait(10)
    place(850, 900, 'k')
    upgrade_time(1, 3)
    upgrade_time(0, 2)
    wait(10)
    place(777, 716, 'x')
    upgrade_time(0, 2)
    upgrade_time(1, 5)
    wait(10)
    place(620, 900, 'j')
    upgrade_time(0, 2)
    upgrade_time(1, 5)

def bloody_puddles():
    sell_truck()
    place(1055, 435, 'q')
    start()
    place_cost(808, 687, 'y')
    upgrade_time(1, 2) 
    upgrade_time(2, 3)
    place_cost(723, 561, 'y')
    upgrade_time(0, 1)
    upgrade_time(2, 2)
    place_cost(929, 789, 'f')
    upgrade_time(0, 4)
    upgrade_time(2, 1)
    select_monkey(1)
    upgrade_time(2, 2)
    place_cost(887, 627, 'k')
    upgrade_time(0, 2)
    upgrade_time(1, 3)
    place_cost(666, 663, 'x')
    upgrade_time(0, 2)
    upgrade_time(1, 5)
    place_cost(1008, 543, 'j')
    upgrade_time(0, 2)
    upgrade_time(1, 5)
    
def dark_castle():
    place(546, 472, 'z')
    place(1459, 567, 'm')
    start()
    place(1570, 562, 'j')
    place(1542, 465, 'k')
    place(1563, 686, 'f')
    place(1462, 371, 'y')
    
def selectedlr():
    pixel_color = pyautogui.pixel(390, 900)
    check = (pixel_color == (255, 119, 0)or
        pixel_color == (256, 119, 0)or
        pixel_color == (255, 120, 0)or
        pixel_color == (256, 120, 0)or
        pixel_color == (255, 118, 0)or
        pixel_color == (256, 118, 0))
    if check:
        return 0
    else:
        pixel_color = pyautogui.pixel(1610, 900)
        check = (pixel_color == (255, 119, 0)or
            pixel_color == (256, 119, 0)or
            pixel_color == (255, 120, 0)or
            pixel_color == (256, 120, 0)or
            pixel_color == (255, 118, 0)or
            pixel_color == (256, 118, 0))
        if check:
            return 1
    return 1


def selected(index):
    pixel_color = pyautogui.pixel(390, 900)
    check = (pixel_color == (255, 119, 0)or
        pixel_color == (256, 119, 0)or
        pixel_color == (255, 120, 0)or
        pixel_color == (256, 120, 0)or
        pixel_color == (255, 118, 0)or
        pixel_color == (256, 118, 0))
    if (check or pyautogui.pixel(85, 70) == (111, 21, 221)) and index == 0:
        return bool(True)
    pixel_color = pyautogui.pixel(1610, 900)
    check = (pixel_color == (255, 119, 0)or
        pixel_color == (256, 119, 0)or
        pixel_color == (255, 120, 0)or
        pixel_color == (256, 120, 0)or
        pixel_color == (255, 118, 0)or
        pixel_color == (256, 118, 0))
    if (check or pyautogui.pixel(1340, 70) == (111, 21, 221)) and index == 1:
        return bool(True)


def pixelcheck(index):
    # links:250
    # rechts:1470
    h3 = 790
    h2 = 640
    h1 = 490
    # Upgrade links
    #print(pyautogui.pixel(250, h1))
    if selected(0):
        if index == 0:
            return pyautogui.pixel(250, h1) == (39, 166, 0) or pyautogui.pixel(250, h1) == (
                39, 167, 0) or pyautogui.pixel(250, h1) == (40, 166, 0) or pyautogui.pixel(250, h1) == (40, 167, 0)
        if index == 1:
            return pyautogui.pixel(250, h2) == (39, 166, 0) or pyautogui.pixel(250, h2) == (
                39, 167, 0) or pyautogui.pixel(250, h2) == (40, 166, 0) or pyautogui.pixel(250, h2) == (40, 167, 0)
        if index == 2:
            return pyautogui.pixel(250, h3) == (39, 166, 0) or pyautogui.pixel(250, h3) == (
                39, 167, 0) or pyautogui.pixel(250, h3) == (40, 166, 0) or pyautogui.pixel(250, h3) == (40, 167, 0)
    # Upgrade rechts
    if selected(1):
        if index == 0:
            return pyautogui.pixel(1470, h1) == (39, 166, 0) or pyautogui.pixel(1470, h1) == (
                39, 167, 0) or pyautogui.pixel(1470, h1) == (40, 166, 0) or pyautogui.pixel(1470, h1) == (40, 167, 0)
        if index == 1:
            return pyautogui.pixel(1470, h2) == (39, 166, 0) or pyautogui.pixel(1470, h2) == (
                39, 167, 0) or pyautogui.pixel(1470, h2) == (40, 166, 0) or pyautogui.pixel(1470, h2) == (40, 167, 0)
        if index == 2:
            return pyautogui.pixel(1470, h3) == (39, 166, 0) or pyautogui.pixel(1470, h3) == (
                39, 167, 0) or pyautogui.pixel(1470, h3) == (40, 166, 0) or pyautogui.pixel(1470, h3) == (40, 167, 0)


def useless():
    xd = 1


# (255, 119, 0)
# (39, 166, 0)
# (39, 167, 0)
# (39, 167, 0)
# (255, 119, 0)
# (40, 167, 0)y
# (40, 167, 0)
# (39, 167, 0)

time.sleep(2)

#useless()
#print_mouse_position()
#print(get_money())
#sell_truck()


#infernal()
#heli_Sanctuary()
#quad()
#muddy_puddles()
#flooded_valleey()
#bloody_puddles()
dark_castle()