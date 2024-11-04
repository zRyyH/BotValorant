import pyautogui
import random
import time

pyautogui.FAILSAFE = False

class AutoGUI():
    def __init__(self):
        pass
    
    def click(self, x, y):
        pyautogui.moveTo(x=x, y=y)
        time.sleep(random.random())
        pyautogui.click()
        
    def press(self, key, interval = False):
        pyautogui.keyDown(key)
        time.sleep(interval or random.random())
        pyautogui.keyUp(key)
        
    def press_random(self, keys):
        key = random.choice(keys)
        pyautogui.keyDown(key)
        time.sleep(random.randint(0, 5))
        pyautogui.keyUp(key)