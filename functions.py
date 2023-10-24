import os
import re
import pyautogui
import time
from pynput.keyboard import Controller, Key
import pytesseract
from PIL import Image
import PIL.Image
import cv2
import bonus_image
import maps


myconfig =r"--psm 10 --oem 3 "
    
#Image reader
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
def auto_select():
    select_map_local(bonus_image.go())
#Round reader
def select_map(index):
    if index==1:#dd
        pymoveclick(500, 250)
    if index==2:#sanctuary
        pymoveclick(900, 250)
    if index==3:#ravine
        pymoveclick(1300, 250)
    if index==4:#flooded valley
        pymoveclick(500, 500)
    if index==5:#infernal
        pymoveclick(900, 500)
    if index==6:#bloody
        pymoveclick(1300, 500)
    #if index >=7:
    #    pymoveclick(1300, 1000)
    if index==7:#workshop
        pymoveclick(500, 250)
    if index==8:#quad
        pymoveclick(900, 250)
    if index==9:#dc
        pymoveclick(1300, 250)
    if index==10:#muddy
        pymoveclick(500, 500)
    if index==11:#ouch
        pymoveclick(900, 500)
    wait(1)
    start_mode()
    
def select_map_local(index):
    if index==1:#dd
        maps.dark_dungons()
    if index==2:#sanctuary
        maps.heli_Sanctuary()
    if index==3:#ravine
        maps.ravine()
    if index==4:#flooded valley
        maps.flooded_valleey()
    if index==5:#infernal
        maps.infernal()
    if index==6:#bloody
        maps.bloody_puddles()
    #if index >=7:
    #    pymoveclick(1300, 1000)
    if index==7:#workshop
        maps.workshop()
    if index==8:#quad
        maps.quad()
    if index==9:#dc
        maps.dark_castle()
    if index==10:#muddy
        maps.muddy_puddles()
    if index==11:#ouch
        maps.ouch()
        
def select_hero(index):
    pymoveclick(100, 1020)
    wait(0.2)
    if index==1:#quicy
        pymoveclick(120, 200)
    if index==2:#gwendolin
        pymoveclick(270, 200)
    if index==3:#striker jones
        pymoveclick(420, 200)
    if index==4:#obyn
        pymoveclick(120, 400)
    if index==5:#churchill
        pymoveclick(270, 400)
    if index==6:#benjamin
        pymoveclick(420, 400)    
    if index==7:#ezili
        pymoveclick(120, 600)
    if index==8:#pat fusty
        pymoveclick(270, 600)    
    if index==9:#adora
        pymoveclick(420, 600)
    if index==10:#brickell
        pymoveclick(120, 800)
    if index==11:#etienne
        pymoveclick(270, 800)
    if index==12:#sauda
        pymoveclick(420, 800)
    if index==13:#psy
        pymoveclick(120, 1000)
    if index==14:#geraldo
        pymoveclick(270, 1000) 
    wait(0.2)
    pymoveclick(1112, 619)
    wait(0.2)
    pymoveclick(80, 56)     
    
def start_mode():
    wait(1) 
    pymoveclick(1290, 410)
    wait(1) 
    pymoveclick(654, 600) 
    wait(0.5) 
    pymoveclick(1128, 718) 

keyboard = Controller()
placed = []
costs = [215, 300, 565, 300, 540, 245, 360, 335, 515, 820, 1640, 770, 820, 405, 2700, 540, 595, 430, 1325, 1080, 1270, 430, 270]

m_to_c = ['q', 'w', 'e', 'r', 't', 'z', 'y', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'i']

def print_mouse_position():
    for _ in range(1):
        wait(5)
        # Get the current mouse position
        mouse_x, mouse_y = pyautogui.position()
        print(pyautogui.pixel(mouse_x, mouse_y))

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
    
    while i<10:
        wait(0.1)
        why=test
        if get_money()>= costs[m_to_c.index(why)]:
            affordable+=1
        i+=1
    if affordable>=5:
        return bool(True)
    
def check_cost_ability(test, index):
    i=0
    affordable=0
    why=0
    keyboard.press(index)
    wait(0.01)
    keyboard.release(index)
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
        
def place_ability(x, y, Monkey, key):
    while True:
        wait(0.1)
        if check_cost_ability(Monkey, key):
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
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
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
        
def upgrade_ability(index, numOfUpgrades, key):
    nou = 0
    while (1 == 1):
        time.sleep(0.3)
        keyboard.press(key)
        wait(0.01)
        keyboard.release(key)
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

def lock_heli():
    wait(3)
    keyboard.press(Key.tab)
    wait(0.1)
    keyboard.release(Key.tab)

def upgrade_ability2(index, numOfUpgrades, key, key2):
    nou = 0
    while (1 == 1):
        time.sleep(0.3)
        keyboard.press(key)
        wait(0.01)
        keyboard.release(key)
        wait(0.01)
        keyboard.press(key2)
        wait(0.01)
        keyboard.release(key2)
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
    time.sleep(0.1)
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



    
def selectedlr():
    color_1=(128, 74, 36)
    color_2=(255, 255, 255)
    
    pixel_color_1 = pyautogui.pixel(227, 892)
    pixel_color_2 = pyautogui.pixel(303, 909)
    if color_1==pixel_color_1 and color_2==pixel_color_2:
        return 0
    else:
        pixel_color_1 = pyautogui.pixel(1445, 892)
        pixel_color_2 = pyautogui.pixel(1525, 909)
        if color_1==pixel_color_1 and color_2==pixel_color_2:
            return 1
    return 1


def selected(index):
    color_1=(128, 74, 36)
    color_2=(255, 255, 255)
    
    pixel_color_1 = pyautogui.pixel(227, 892)
    pixel_color_2 = pyautogui.pixel(303, 909)
    if color_1==pixel_color_1 and color_2==pixel_color_2 and index == 0:
        return bool(True)
    
    pixel_color_1 = pyautogui.pixel(1445, 892)
    pixel_color_2 = pyautogui.pixel(1525, 909)
    if color_1==pixel_color_1 and color_2==pixel_color_2 and index == 1:
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

def setstrong():
    keyboard.press(Key.tab)
    wait(0.1)
    keyboard.release(Key.tab)
    wait(0.1)
    keyboard.press(Key.tab)
    wait(0.1)
    keyboard.release(Key.tab)
    wait(0.1)
    keyboard.press(Key.tab)
    wait(0.1)
    keyboard.release(Key.tab)